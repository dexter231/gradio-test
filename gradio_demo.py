import gradio as gr
import time
import sys

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

local_url, share_url = demo.launch(share=True)

print("Share URL:", share_url)
sys.stdout.flush()  # Force output buffer to flush

time.sleep(21600)
