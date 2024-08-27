import gradio as gr
import time

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

local_url, share_url = demo.launch(share=True)

print("Share URL:", share_url)

time.sleep(21600)
