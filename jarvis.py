import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak('Good Morning')
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    
    else:
        speak('Good Evening')

    speak('I am friday sirPlease tell me hoe may I help you')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print('say that again please...')
        return "None"
    return query 


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace(wikipedia)
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dr = 'C:\\Users\\Nishu\\OneDrive\\Desktop\\MUSIC'
            songs = os.listdir(music_dr)
            os.startfile(os.path.join(music_dr,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:&M:%S')
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = '"C:\\Users\\Nishu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'quit' in query:
            speak('Thank you for all your time sir. Have a nice day')
            exit()

