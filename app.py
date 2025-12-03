import os
import gradio as gr
from openai import OpenAI

# Free API setup (sign up at openrouter.ai for key, or use free tier)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY") or "sk-or-v1-dummy-for-free-tier"  # Replace with your key later
)

def grok_chat(message, history):
    # Load my personality
    system_prompt = open("system_prompt.txt").read()
    messages = [{"role": "system", "content": system_prompt}]
    for user_msg, bot_msg in history:
        if user_msg: messages.append({"role": "user", "content": user_msg})
        if bot_msg: messages.append({"role": "assistant", "content": bot_msg})
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",  # Swap to "meta-llama/llama-3.1-70b-instruct" for open-source
        messages=messages,
        temperature=0.9,
        max_tokens=2048
    )
    return response.choices[0].message.content

# Launch the chat UI
demo = gr.ChatInterface(
    grok_chat,
    title="c0040863-jpg's Grok Clone 😈",
    description="Zero filters. Built by a legend. Talk to me like I'm Grok.",
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
