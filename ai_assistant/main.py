from tts.voice import speak, recognize
#from hug.chat import ai_process
import asyncio
from browser.links import open_url
from llm.olama import call_llama

# r = recognize()

# asyncio.run(speak(r))
async def main():
  while True:
    text = recognize()  # Make recognize() async

    llama_response = await call_llama(text)  # Call llama async
    await speak(llama_response)  

asyncio.run(main())
# while True:
#   text = recognize()
#   # asyncio.run(speak(text))
#   t = asyncio.run(call_llama(text))
#   asyncio.run(speak(t))
#   if text.lower() == "open url":
#     asyncio.run(speak("what url do you want to open?"))
#     url = recognize()
#     asyncio.run(speak("Opening "+url))
#     open_url(url.lower())
#   if text.lower() == "exit":
#     break
#   else: 
#    asyncio.run(speak("Looks like your are "))
#    continue
