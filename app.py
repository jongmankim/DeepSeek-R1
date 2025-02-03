# Example:reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
completion = client.chat.completions.create(
    model="lmstudio-community/gemma-2-9b-it-GGUF", 
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, 
        {"role": "user", "content": "우리는 무엇을 위해 살아가나요?"}
    ],
    temperature=0.7,
)
print(completion.choices [0].message)

###
#This environment is externally managed
#[출처] [python]pip3 install 커맨드 실행 안 되는 오류 해결 errer: externally-managed-environment (mac)|작성자 엎질
#다음과 같은 명ㅕ령어를 실행하면 해결된다.
#python3 -m pip config set global.break-system-packages true
