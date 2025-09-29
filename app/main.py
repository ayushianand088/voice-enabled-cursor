import speech_recognition as sr

def main():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # noise cancellation
        r.adjust_for_ambient_noise(source)
        print("Say Something!")
        audio = r.listen(source)
        
        # recognize speech and convert to text
        print("Processing audio...")
        sst = r.recognize_google(audio)
        print("You said: ", sst)
    
main()