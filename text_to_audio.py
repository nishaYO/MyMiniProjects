import pyttsx3
text_to_audio = pyttsx3.init()
my_text = "Welcome to Nisha's repository. I am a text to audio convering program."
text_to_audio.say(my_text)
text_to_audio.runAndWait()