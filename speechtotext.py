from gtts import gTTS
from playsound import playsound
tts = gTTS('Ram ji kaha hi ghoomne gaye hi')
tts.save('techsrijan.mp3')
playsound('techsrijan.mp3')
