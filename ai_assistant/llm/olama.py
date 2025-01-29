# from fastapi import FastAPI
import requests
import json
import sseclient
import asyncio
import sys
import os
# from tts.voice import speak



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tts.voice import speak
# url = "http://localhost:11434/api/generate/"


# def call_llama(prompt):
#     payload = { 
#         "model": "llama3.2",
#         "prompt": prompt,
#         "stream": True
#     }

#     response = requests.post(url, json=payload, stream=True)
#     r =""
#     for res in response.iter_lines():
#         if res:
#             j = json.loads(res.decode('utf-8'))
#             # print(j['response'])
#             r += j['response']
#             print("text: ", r,"len: ",len(r))
#     return r


import aiohttp
import asyncio
import json

url = "http://localhost:11434/api/generate/"

async def call_llama(prompt):
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": True
    }

    r = ""
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            async for line in response.content:
                if line:
                    j = json.loads(line.decode('utf-8'))
                    r += j['response']
                    # print("text:", r, "len:", len(r))
    return r

# To call the function
# a = asyncio.run(call_llama("whats your name?"))
# asyncio.run(speak(a))