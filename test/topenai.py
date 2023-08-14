import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

system_content = \
"""
python code.

def f(a:int, b:int, c:int, d:int):
    //code to generate
    return rtn
"""
user_content = \
"""
rtn can't be larger than d.
if b + c > a then rtn must be less than d/2.
complete "code to generate" area as you want to compose.

answer only code.
"""
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
        ]
    )
print(chat_completion['choices'][0]['message']['content'])