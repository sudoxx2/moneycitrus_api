import openai

openai.api_key = ''


def get_openai_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

user_input = input("User: ")
response = get_openai_response(user_input)
print("ChatGPT: " + response)
