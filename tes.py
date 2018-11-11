import speech_recognition as sr
import pyttsx3

voices = []
speech=sr.Recognizer



try:
    engine = pyttsx3.init()

except ImportError:
    print('Driver is not found')
except RuntimeError:
    print('Driver is not installed')
else:
  voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate=engine.setProperty('rate')
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd(cmd):
    voice_text=''
    with sr.Microphone() as source:
        audio=speech.listen(source)
        try:
            voice_text = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print('network error.')
            return voice_text



if __name__ == '__main__':
    speak_text_cmd('Hello Mr.Waleed. This is Alice as your Artificial intelligence')