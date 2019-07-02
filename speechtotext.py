from gtts import gTTS
from playsound import playsound
tts = gTTS('Hello how r u ? I am fine thanku')
tts.save('techsrijan.mp3')
playsound('techsrijan.mp3')
