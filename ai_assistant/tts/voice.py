import io
from pydub import AudioSegment
from pydub.playback import play
import edge_tts
import speech_recognition as sr

async def speak(text, voice="en-US-EmmaMultilingualNeural", rate="+0%"):
    tts = edge_tts.Communicate(text, voice=voice, rate=rate)

    # Collect audio stream in memory
    mp3_stream = io.BytesIO()
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            mp3_stream.write(chunk["data"])

    # Rewind the stream for playback
    mp3_stream.seek(0)

    # Convert MP3 stream to playable audio
    audio = AudioSegment.from_file(mp3_stream, format="mp3")
    play(audio)


def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            return query
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Some error occurred. Sorry from Jarvis"
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "Could not understand audio"
