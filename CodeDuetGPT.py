import os
import re
import time
import json
import sys
import traceback
from colorama import Fore
from openai import OpenAI

# Emulating colored text without external libraries
COLORS = {
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
}

def colored(text, color=None):
    if color in COLORS:
        return f"{COLORS[color]}{text}{COLORS['reset']}"
    return text

def type_out(text, color=None, delay=0.025):
    for char in text:
        sys.stdout.write(colored(char, color) if color else char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

class Documents:
    def __init__(self, generated_content=None):
        print("[Debug] Initializing EnhancedDebugDocuments...")

        self.directory = os.path.expanduser("~") + "/Downloads/AutoCodeFiles"
        if not os.path.exists(self.directory):
            try:
                os.mkdir(self.directory)
                print(f"[Debug] Directory {self.directory} created successfully.")
            except Exception as e:
                print(f"[Debug] Error creating directory: {e}")
        else:
            print(f"[Debug] Directory {self.directory} already exists.")

        if generated_content:
            print(f"[Debug] Set generated content to: {generated_content[:100]}...")
            self.generated_content = generated_content
            self.docbooks = self._parse_content()
        else:
            print("[Debug] Generated content is None!")
            self.generated_content = ""
            self.docbooks = {}

    def _parse_content(self):
        class_pattern = re.compile(r"(class\s+\w+\s*\(?.*\)?\s*:.*?)(?=class\s+\w+\s*\(?.*\)?\s*:|$)", re.DOTALL)
        matches = class_pattern.findall(self.generated_content)
    
        docs = {}
        for match in matches:
            classname_match = re.search(r'class\s+(\w+)', match)
            if classname_match:
                classname = classname_match.group(1)
                docs[f"{classname}.txt"] = match
        return docs

    def update_docs(self, generated_content):
        print("[Debug] Updating documents...")
        self.generated_content = generated_content
        new_docs = self._parse_content()
        for key, value in new_docs.items():
            if key not in self.docbooks.keys() or self.docbooks[key] != value:
                self.docbooks[key] = value

    def rewrite_docs(self):
        print("[Debug] Rewriting documents...")
        for filename, content in self.docbooks.items():
            filepath = os.path.join(self.directory, filename)
            try:
                if os.path.exists(filepath):
                    with open(filepath, "r+", encoding="utf-8") as file:
                        existing_content = file.read()
                        if existing_content != content:
                            file.seek(0)
                            file.truncate()
                            file.write(content)
                            print(f"[Debug] Updated file: {filepath}")
                        else:
                            print(f"[Debug] Content for {filepath} has not changed. Skipping write.")
                else:
                    with open(filepath, "w", encoding="utf-8") as writer:
                        writer.write(content)
                        print(f"[Debug] Written to new file: {filepath}")
            except IOError as e:
                print(f"[Debug] IO Error writing to file {filepath}: {e}")
                print(traceback.format_exc())
            except Exception as e:
                print(f"[Debug] General error writing to file {filepath}: {e}")
                print(traceback.format_exc())

class ChatEnvironment:
    def __init__(self):
        self.state = {}
        self.context = []

    def update_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        return self.state.get(key, None)

    def update_context(self, message):
        self.context.append(message)

    def get_context(self):
        return self.context

class ChatLogic:
    def __init__(self, env, config):
        self.env = env
        self.config = config
        self.model = self.config.get("model", "gpt-4o-mini")
        self.temperature = self.config.get("temperature", 0.3)
        self.max_tokens = self.config.get("max_tokens", 16384)
        self.top_p = self.config.get("top_p", 1)
        self.frequency_penalty = self.config.get("frequency_penalty", 0)
        self.presence_penalty = self.config.get("presence_penalty", 0)
        self.client = OpenAI()

    def get_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a panel of expert software architects. Your task is to understand the requirements, design the program structure, and sequentially generate code for each section.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

class ChatSession:
    def __init__(self, config_filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, config_filename)

        with open(config_path, "r") as file:
            self.config = json.load(file)

        self.env1 = ChatEnvironment()
        self.env2 = ChatEnvironment()
        self.logic1 = ChatLogic(self.env1, self.config)
        self.logic2 = ChatLogic(self.env2, self.config)

        self.endcap = "You are a panel of senior software engineers with diverse expertise. Your role is to review the code generated by the Planning Agent, identify improvements, and refine the code to ensure quality, efficiency, and maintainability. Always ensure the code is functional with no placeholder code. After 2 revisions, continue with the next class."

        self.documents = None

    def get_prompt_from_user_or_file(self):
        choice = input("Write your prompt on a txt file.  Copy and paste the file's directory now.  ​Click on the file, then for MacOS Option-Command-C, Windows Ctrl + Shift + C.  Then paste here: ")
        if choice.strip().lower() == 'n':
            initial_prompt = input(colored("Please provide the initial prompt (cannot be empty): ", "cyan"))
            while not initial_prompt.strip():
                initial_prompt = input(colored("Prompt cannot be empty. Please provide the initial prompt: ", "red"))
            return initial_prompt
        else:
            try:
                with open(choice, 'r') as file:
                    content = file.read().strip()
                    if content:
                        return content
                    else:
                        print(colored("File is empty. Please provide the prompt manually.", "red"))
                        return self.get_prompt_from_user_or_file()
            except Exception as e:
                print(colored(f"Error reading the file: {e}. Please provide the prompt manually.", "red"))
                return self.get_prompt_from_user_or_file()

    def process_chat(self, chat):
        """This method processes the chat, printing it out and managing the document updates."""
        print(colored(f"Chat {self.env1.get_state('turns')}:", "cyan"), chat)

        if "class" in chat:
            if not self.documents:
                self.documents = Documents(chat)
            else:
                self.documents.update_docs(chat)
            self.documents.rewrite_docs()

    def initialize(self):
        type_out(
            "Welcome to CodeDuetGPT, where we take two separate conversations of GPT-4 and have them work together recursively to build you code. This doubles the context length, you're welcome. Write out your prompt on a TXT file, you'll be prompted to upload it soon.",
            "green",
        )

        type_out(
            "So how many back and forth rounds you want to do before the party ends and you're asked if you want to export your conversation history? Keep in mind it's $0.03 every 1000 words that is inputted and outputted:",
            "yellow",
        )
        self.config["max_turns"] = int(input())

        api_key = input(colored("\nPlease enter your OpenAI API key: ", "cyan"))
        self.client = OpenAI(api_key=api_key)  # Ensure this line is correct

        prompt = self.get_prompt_from_user_or_file()
        print(f"Prompt accepted: {prompt[:100]}...")

        self.env1.update_context({"role": "user", "content": prompt})
        self.env2.update_context({"role": "user", "content": prompt})

        for _ in range(self.config["max_turns"]):
            prompt1 = self.logic1.get_response(prompt)
            self.process_chat(prompt1)
            prompt2 = self.logic2.get_response(prompt)
            self.process_chat(prompt2)
            prompt = f"{prompt1}\n{prompt2}\n{self.endcap}"

        print("All done!")

if __name__ == "__main__":
    session = ChatSession("config.json")
    session.initialize()
