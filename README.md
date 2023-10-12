# CodeDuetGPT

Dual Independent-Agent Conversation Model for Enhanced Contextual and Creative Capacity for Automated Self-Recursive Code Generation

## Overview
In the world of AI-driven automated code generation, the desire for constent converstaional understanding is ever-present. The ability to retain and leverage context is key to successful automated code generation. 

CodeDuetGPT's unique dual-agent model harnesses the power of two seperate GPT-4 iterations engaging in a dynamic code building session. This approach stands in contrast to the alternate method of using a single GPT-4 32k model simulating two agents conversing. By employing two distinct GPT-4 agents, we achieve a notable advancement in contextual understanding.

"But what about the GPT4 32K API! Simulate two agents on there!"

According to the paper [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)) it states that "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts"

Therefore, a single GPT-4 32K model simulating two agents will likely encounter limitations in retaining and recalling prior parts of the conversation regardless of its lengthy context length.  This will compromise the automated agents' focus and ability to build relevant code. 

However, the use of two independent GPT-4 iterations allows for a more seamless and comprehensive contextual flow for reasonably long code building sessions. This improved, seperated contextual memory ensures that past dialogue segments remain readily accessible to each iteration, leading to enhanced coherence and relevance in code generation. It enables CodeDuetGPT to excel in scenarios where intricate, multi-step discussions and precise contextual referencing are imperative for generating high-quality code.
