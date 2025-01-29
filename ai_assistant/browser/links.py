import webbrowser
import requests

domains = [".com", ".org", ".edu", ".gov", ".net", ".int", ".mil"]

hedears = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

def check_url_status(url):
  for domain in domains:
    url = "https://www."+url+domain
    # print("Checking: \n",url)
    req = requests.get(url, headers=hedears)
    if req.status_code == 200:
      return [True, url]
    else:
      return False

def open_url(url):
  status,u = check_url_status(url)
  if status:
    webbrowser.open(u)
  else:
        return False
# from tts.voice import speak,recognize
# import webbrowser
# import requests
# import speech_recognition as sr

# domains = [".com", ".org", ".edu", ".gov", ".net", ".int", ".mil"]

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

# def check_url_status(base_url):
 
#     prefixes = ["https://", "https://www."]
    
#     for prefix in prefixes:
#         for domain in domains:
#             full_url = f"{prefix}{base_url}{domain}"
#             try:
#                 response = requests.get(full_url, headers=headers, timeout=5)
#                 if response.status_code == 200:
#                     return [True, full_url]
#             except requests.RequestException:
#                 pass  # Ignore exceptions and continue checking other URLs

#     return False  # No valid URL found

# def open_domain(domain_name):
   
#     result = check_url_status(domain_name)
#     if result:
#         _, valid_url = result
#         webbrowser.open(valid_url)  # Open in the default web browser
#         return f"Opened URL: {valid_url}"
#     else:
#         return 

# def get_speech_input():
   
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for a domain name (say 'exit' to quit)...")
#         try:
#             audio = recognizer.listen(source, timeout=5)
#             speech_text = recognizer.recognize_google(audio).strip()
#             print(f"You said: {speech_text}")
#             return speech_text
#         except sr.UnknownValueError:
#             print("Sorry, I didn't understand that.")
#         except sr.RequestError as e:
#             print(f"Speech recognition service error: {e}")
#         except sr.WaitTimeoutError:
#             print("Listening timed out.")
#     return None

# while True:
#     user_input = get_speech_input()
#     if user_input is None:
#         continue 
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting AI Assistance.")
#         break
#     else:
#         print(open_domain(user_input))
