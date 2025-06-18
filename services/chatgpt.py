import openai

def ask_gpt(client: openai.OpenAI, user_input: str) -> str:
    # https://github.com/openai/openai-python#:~:text=from%20openai%20import%20OpenAI%0A%0Aclient%20%3D%20OpenAI(),choices%5B0%5D.message.content)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are an AI interviewer. Keep your answers short and to the point."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()
