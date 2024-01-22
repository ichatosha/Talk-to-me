import file
import csv
import os

#speech to text
import speech_recognition as sr
#text to speech
import pyttsx3                      
import sys
import time

engine = pyttsx3.init()
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d/%m/%Y, %H:%M", named_tuple)

#print(time_string)

# name = input("enter your name : ")
#engine.say(f"hello hesham welcome to computer science course")
#engine.runAndWait()



rec = sr.Recognizer()

with sr.Microphone() as srm:
        #engine.say("say somthing")
        
        #engine.runAndWait()
        while True:
            print("say somthing...")
            #engine.say("say somthing")
            #engine.runAndWait()
            audio = rec.listen(srm)
            text = rec.recognize_google(audio)
            print(text)
            
            if text in [ "are you here", "good morning", "hello"]:
                    engine.say("hello hesham how are you")
                    engine.runAndWait()
                
            elif text in ["time","what's the time now", "tell me time now"]:
                    
                    print(time_string)
                    engine.say(time_string)
                    engine.runAndWait()

            elif text in["done go away" , "close", "ok" , "okay"]:
                    engine.say("ok see you soon")
                    engine.runAndWait()
                    sys.exit()
                        
            elif text in "how are you":
                    engine.say("iam fine thanks")
                    engine.runAndWait()
                    
            elif text in ["Google Chrome" , "chrome" , "google"]:
                    #with open("C:\Program Files\Google\Chrome\Application\chrome.exe", "r+") as file:
                            #print(file)             
                    res = os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                    print(res)      
                    
            elif text in ["calculator" , "Calc" ]:
                    res = os.startfile(r"C:\Windows\System32\calc.exe")    
              
              # To run this op. >> create shortcut of youtube website and save it in Downloads folder      
            elif text in ["YouTube" , "youtube" , "you tube"]:
                    res = os.startfile(r"C:\Users\HESHAM\Downloads\www_youtube_default.html") 
                    print(res)            
            else :   
                engine.say("i don't understand you")
                engine.runAndWait()
            
            

    
























    