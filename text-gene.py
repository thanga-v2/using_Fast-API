import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('HFTOKEN')

client = InferenceClient(model="gpt2", token=token)
prompts = []

print(client)

prompt = "anymore context?"
prompts.append(prompt)

# Call the text generation API - calling the hugging face API locally.
response = client.text_generation(prompt, max_new_tokens=30)

print(response)
print(prompts)


