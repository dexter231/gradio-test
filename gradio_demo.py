import gradio as gr
import time

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

local_url, share_url = demo.launch(share=True)

print("::set-output name=share_url::" + share_url)  # GitHub Actions output

time.sleep(21600)
