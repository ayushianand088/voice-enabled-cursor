import speech_recognition as sr
from langgraph.checkpoint.mongodb import MongoDBSaver
from graph import create_chat_graph
import pyttsx3

MONGODB_URI = "mongodb://admin:admin@localhost:27017"
config = {"configurable": {"thread_id": "5"}}

def main():
    with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
        graph = create_chat_graph(checkpointer=checkpointer)
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # noise cancellation
            r.adjust_for_ambient_noise(source)
           
            while True:
                print("Say Something!")
                audio = r.listen(source)
                
                # recognize speech and convert to text
                print("Processing audio...")
                sst = r.recognize_google(audio)
                print("You said: ", sst)
                for event in graph.stream({"messages": [{"role": "user", "content": sst}]}, config, stream_mode="values"):
                    if "messages" in event:
                        event["messages"][-1].pretty_print()
                        pyttsx3.speak(event["messages"][-1].content)
        
main()