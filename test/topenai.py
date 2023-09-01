import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

system_content = \
"""
python code.

def f( bet_seq:int=0, 
       bet_amount:int=0, 
       deposit_amount:int=0, 
       deposit_balance:int=0, 
       
       tot_deposit_amount:int=0,
       tot_deposit_balance:int=0, 
       avg_bet_amount_per_account:int=0, 
       avg_bet_amount_per_round:int=0, 
       tot_bet_amount:int=0, 
       tot_bet_count:int=0, 
       avg_deposit_amount_per_account:int=0, 
       account_count:int=0):
    bool rtn = False

    //code to generate

    return rtn
"""
user_content = \
"""
if bet_amount larger than deposit_balance then rtn is True.
if bet_amount > avg_bet_amount_per_account then rtn is True.
In other cases, rtn is False

complete "code to generate" area as you want to compose.

answer only code.
"""
user_content_k = \
"""
bet_amount 가 deposit_balance 보다 크면 rtn 은 True.
bet_amount 가 avg_bet_amount_per_account 보다 크면 rtn 은 True.
나머지 경우에는 rtn 은 False

"code to generate" 영역을 완성하여라.


please print only "code to generate" area.
answer only code.
"""
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
        ]
    )
print(chat_completion['choices'][0]['message']['content'])