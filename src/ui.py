import gradio as gr

from .retrieve import retrieve_from_agent

with gr.Blocks(
    title="Web Content Summariser", theme="JohnSmith9982/small_and_pretty@>=1.0.0"
) as demo:
    chatbot = gr.Chatbot(
        label="Summarise a Web Page", show_copy_button=True, layout="panel"
    )
    msg = gr.Textbox(
        placeholder="Please provide the URL of the web page to extract information from."
    )
    clear = gr.ClearButton([msg, chatbot])

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def get_response(history):
        resp = retrieve_from_agent(history[-1][0])
        history[-1][1] = ""
        history[-1][1] = resp
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        get_response, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
