import openai
import os

# set up OpenAI API credentials
openai.api_key = os.environ["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"]

# define the prompt and user input
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
user_input = "Hello, can you help me with my math homework?"

# generate a response using ChatGPT
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt + "\nUser: " + user_input + "\nAI:",
    max_tokens=1024,
    temperature=0.7,
)

# print the AI's response
print(response.choices[0].text.strip())
