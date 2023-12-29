import openai
import gradio

from openai import OpenAI

client = OpenAI(api_key = "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")


messages = [{"role": "system", "content": "You are a deep learning education expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)