import locale
import gradio as gr
locale.getpreferredencoding = lambda: "UTF-8"
print(gr.__version__)
def predict(message, history):
    output = str(llm_ans(message)).replace("\n", "<br/>")
    return output

demo = gr.ChatInterface(
    predict,
    title = f' Open-Source LLM ({CFG.model_name}) for Harry Potter Question Answering'
)

demo.queue()
demo.launch()