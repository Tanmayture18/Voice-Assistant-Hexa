
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("i am hexa sir please tell me how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
           # print(e)

            print("say that again please...")
            return "None"
        return query    


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia'in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")  

        elif 'open facebook'in query:
            webbrowser.open("facebook.com")  

        elif 'play songs'in query:
            music_dir='C:\\Users\\admin\\Desktop\\mysongs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'open email'in query:
            webbrowser.open("gmail.com")  

        elif'open classroom'in query:
            webbrowser.open("classroom.google.com")      

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"sir,the time is {strTime}")

        elif 'open code'in query:
            codepath="C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif'open chrome'in query:
            chromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"  
            os.startfile(chromepath) 

        elif 'open amazon'in query:
            webbrowser.open("amazon.in")    

        elif 'the weather'in query:
            webbrowser.open("weather.com")   

        elif 'the score' in query:
            webbrowser.open("cricbuzz.com")      
                   

    
