import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  #py file created for for music library
import requests
import os
import google.generativeai as genai

# Integrated with generative ai
# Requires your generativeai api key for running ai part.

# voice input recognization
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):  #voice output
    engine.say(text)
    engine.runAndWait()


def aiprocess(command): #ai setup
    ak = "Your generativeai(gemini) api key here"  #API key

    genai.configure(api_key = ak)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    response = model.generate_content(command + "in short")

    return response.text


def processCommand(c):  #command processing
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open creators github" in c.lower() or "open creator's github" in c.lower() or "open creator github" in c.lower():
        webbrowser.open("https://www.github.com/tarakbandhara")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    else:  #ai generated result

        # Let Gemini ai handle the request

        # Asking and getting answer from AI : 
        output = aiprocess(c)
        speak(output)
   
        with open("ai_log.txt", "a") as l :  
            l.write (f" Question : {c} \n\n Answer : {output} \n\n\n")  # here : c is question and output is answer
     



if (__name__ == "__main__") : 
    speak("Initializing Argus...")
    while True : 

        # Listen for then wake word "assistant"
        # obtain audio from the microphone

        r = sr.Recognizer()
        
        
        print("recognizing...")
        try : 
            with sr.Microphone() as source :  
                print("Listening...")
                audio = r.listen(source, timeout = 7, phrase_time_limit = 5)
            word = r.recognize_google(audio)
            
            if(word.lower() == "assistant"):
                speak("Ya")
                print("Ya")
            

                # Listen for command 
                with sr.Microphone() as source :  
                    print("Argus Active...")
                    speak("Argus Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Processing...")

                    processCommand(command)
                    print("END")
        
        except Exception as e:
            print("Error; {0}".format(e))
            
            


