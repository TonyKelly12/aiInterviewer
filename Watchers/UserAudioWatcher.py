import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Services import runGPTService

openFilePath = "C:/Users/Tony/Documents/Repos/pythonEnvironments/AiInterview/Outpputs/UserOutputs//audio/userAudioInput.wav"
writeFilePath = "C:/Users/Tony/Documents/Repos/pythonEnvironments/AiInterview/Outpputs/UserOutputs//text/userTextInput.txt"

class UserAudioWatcher(FileSystemEventHandler):
  
    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        runGPTService(openFilePath, writeFilePath)

    def startAudioUserInputWatcher():
        print('watching for user audio input')
        

def StartUserAudioWatcher():
    # put the path to the directory you want to monitor here
    path_to_watch = "C:/Users/Tony/Documents/Repos/pythonEnvironments/AiInterview/Outpputs/UserOutputs/audio"
    event_handler = UserAudioWatcher()
    
    userInputAudioObserver = Observer()
    userInputAudioObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    userInputAudioObserver.start()
    print('user audio watcher started')       
            
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        userInputAudioObserver.stop()
    
    userInputAudioObserver.join()
