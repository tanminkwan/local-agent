import subprocess
import asyncio
import os

initial_param = {
    "env_params":{
    "agent_name":"kim",
    "agent_roles":"betting_agent"
    }
}

for item, value in list(initial_param['env_params'].items()):

    os.environ[item.upper()] = f""+value
    subprocess.run(["bash","-c","export "+item.upper()+"="+value], stdout=subprocess.DEVNULL)

subprocess.run(["bash","-c","python3 betting_agent.kim.py &"], stdout=subprocess.DEVNULL)