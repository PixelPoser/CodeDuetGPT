![GitHub Logo](CodeDuetGPT_Logo.jpg
)

# CodeDuetGPT

Dual Independent-Agent Conversation Model for Enhanced Contextual and Creative Capacity for Automated Self-Recursive Code Generation

## Overview
In the world of AI-driven automated code generation, the desire for constent converstaional understanding is ever-present. The ability to retain and leverage context is key to successful automated code generation. 

CodeDuetGPT's unique dual-agent model harnesses the power of two seperate GPT-4 iterations engaging in a dynamic code building session. This approach stands in contrast to the alternate method of using a single GPT-4 32k model simulating two agents conversing. By employing two distinct GPT-4 agents, we achieve a notable advancement in contextual understanding.

"But what about the GPT4 32K API! Simulate two agents on there!"

According to the research paper "Lost in the Middle: How Language Models Use Long Contexts", it states that "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts"

Therefore, a single GPT-4 32K model simulating two agents will likely encounter limitations in retaining and recalling prior parts of the conversation regardless of its lengthy context length.  This will compromise the automated agents' focus and ability to build relevant code. 

However, the use of two independent GPT-4 iterations allows for a more seamless and comprehensive contextual flow for reasonably long code building sessions. This improved, seperated contextual memory ensures that past dialogue segments remain readily accessible to each iteration, leading to enhanced coherence and relevance in code generation. It enables CodeDuetGPT to excel in scenarios where intricate, multi-step discussions and precise contextual referencing are imperative for generating high-quality code.

[Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)



## Quick Start

- Ensure you have Git installed on your machine. You can download it from [Git Downloads](https://git-scm.com/downloads).

## Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```bash
   git clone https://github.com/PixelPoser/CodeDuetGPT.git
3. Run the following command:
   ```bash
   python3 codeduetgpt.py
4. Follow the instructions. You need to write your prompt on a txt or rtf file.
5. Then you will input the directory of that prompt txt file when asked (MacOS Option-Command-C, Windows Ctrl + Shift + C).
6. Then you input how many rounds you want it to run for.
7. After it finishes running the coding conversations, you will be prompted to export your conversation history as a txt file.
8. Now you have a transcript with all your code!
9. Understand that I have no idea how to code, and I wrote this whole program using endless prompting into GPT-44 Code Interpreter and haphazardly copying and pasting into Visual Studio Code.
10. The irony of not knowing how to code and building a code-building program to accelerate my laziness is not lost on me.
11. CodeDuetGPT was funded in part by legally prescribed Adderall and white Monster Energy drinks I bought in bulk.
