![GitHub Logo](CodeDuetGPT_Logo.jpg
)

# CodeDuetGPT

Dual Independent-Agent Conversation Model for Enhanced Contextual and Creative Capacity for Automated Self-Recursive Code Generation

## Overview

(Update 7/23/24: I have updated this script to utilize the GPT-4-Mini model with 16,384 token output. Incredible how the models astronogmically improved improved since I wrote this almost a year ago. Enjoy this dinosaur of a script.  Readme below remains the same for record purposes)

In the world of AI-driven automated code generation, the desire for consistent conversational understanding is ever-present. The ability to retain and leverage context is key to successful automated code generation. 

CodeDuetGPT's unique dual-agent model harnesses the power of two separate GPT-4 iterations engaging in a dynamic code building session. This approach stands in contrast to the alternate method of using a single GPT-4 32k model simulating two agents conversing. By employing two distinct GPT-4 agents, we achieve a notable advancement in contextual understanding.

"But what about the GPT-4 32K API! Simulate two agents on there!"

According to the research paper "Lost in the Middle: How Language Models Use Long Contexts", it states that "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts"

Therefore, a single GPT-4 32K model simulating two agents will likely encounter limitations in retaining and recalling prior parts of the conversation regardless of its lengthy context length.  This will compromise the automated agents' focus and ability to build relevant code. 

However, the use of two independent GPT-4 iterations allows for a more seamless and comprehensive contextual flow for reasonably long code building sessions. This improved, separated contextual memory ensures that past dialogue segments remain readily accessible to each iteration, leading to enhanced coherence and relevance in code generation. It enables CodeDuetGPT to excel in scenarios where intricate, multi-step discussions and precise contextual referencing are imperative for generating high-quality code.

[Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)



## Quick Start

- Ensure you have Git installed on your machine. You can download it from [Git Downloads](https://git-scm.com/downloads).
- You need an OpenAI key

## Clone the Repository

1. Open a terminal or command prompt.
2. Install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3. Install Python3:
   ```bash
   brew install python3
4. Navigate to the directory where you want to clone the repository.
5. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/PixelPoser/CodeDuetGPT.git
6. Install Required Libraries
   ```bash
   pip3 install openai
   pip3 install colorama
7. Then run this:
   ```bash
   cd codeduetgpt
8. Run the following command:
   ```bash
   python3 codeduetgpt.py
9. Follow the instructions. You need to write your prompt on a txt or rtf file.

10. Then you will input the directory of that prompt txt file when asked (MacOS Option-Command-C, Windows Ctrl + Shift + C).
   
11. Then you input how many rounds you want it to run for.
   
12. After it finishes running the coding conversations, you will be prompted to export your conversation history as a txt file.
    
13. Now you have a transcript with all your code!
    
14. Understand that I have no idea how to code, and I wrote this whole program using endless prompting into GPT-4 Code Interpreter and haphazardly copying and pasting into Visual Studio Code.
    
15. The irony of not knowing how to code and building a code-building program to accelerate my laziness is not lost on me.
    
16. CodeDuetGPT was funded in part by legally prescribed Adderall and white Monster Energy drinks I bought in bulk.
