import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

hf_key = os.getenv('HFTOKEN')
#print(hf_key)

test = InferenceClient(model="gpt2", token=hf_key)

print("test object", test)

prompt = "beautifull pollachi road, sunshine after rain, both sides are covered with trees"

response = test.text_to_image(prompt)

print(response)



