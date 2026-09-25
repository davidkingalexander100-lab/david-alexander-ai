import gradio as gr
import os

ARTICLES = """
[1] THE SPEAKER: I set myself ablaze for the world to watch me burn.
[2] MONEY: Money is a tool, not a master.
[3] BELIEF: Belief must be challenged daily.
[4] GROWTH: Growth is painful but necessary.
[5] PAIN: Pain is data. Use it.
[6] LEGACY: Legacy is what remains when you are gone.
"""

def chat(message, history):
    return f"🔥 DAVID ALEXANDER AI Twin 🔥\n\nYou said: '{message}'\n\nFrom my writings:\n{ARTICLES}\n\nMy take: Belief is the foundation. Challenge every whisper."

with gr.Blocks(title="David Alexander AI") as demo:
    gr.Markdown("# DAVID ALEXANDER AI 🔥\nI set myself ablaze for the world to watch me burn")
    gr.ChatInterface(fn=chat)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
