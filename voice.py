import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices  = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize(voice)
            command = command.lower()
            if 'baba' in command:
                command = command.replace('baba', '')
               # talk(command)
    except:
        pass
    return command
def run_baba():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'net' in  command:
        person = command.replace('net', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk('Please do not judge me on my joke but i will try ')
        talk(pyjokes.get_joke())
    else:
        talk('plz say the command again.')

run_baba()