# Example:reuse your existing OpenAI setup
#from openai import OpenAI
import openai # Import the OpenAI library

# Point to the local server
client = OpenAI(base_ur1="http://localhost:1234/v1", api_key="lm-studio")
completion = client.chat.completions.create(
    model="lmstudio-community/gemma-2-9b-it-GGUF", 
    messages=[
        {"role": "system", "content": "Always answer in rhymes. "}, 
        {"role": "user", "content": "Introduce yourself. "}
    ],
    temperature=0.7,
)
print(completion.choices [0].message)