import time
import os
import sys
from Services.GoogleTextToSpeechService import runText2SpeachService
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AITextWatcher(FileSystemEventHandler):
          
    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        runText2SpeachService()
    
    def startAudioHelloWatcher():
        print('watching for AI input')
        # put the path to the directory you want to monitor here

def StartAITextWatcher():
    print('sys ' + sys.argv[0])
    path_to_watch = 'C:/Users/Tony/Documents/Repos/pythonEnvironments/AiInterview/Outpputs/AIOutputs/text'
    event_handler = AITextWatcher()
    aiTextObserver = Observer()
    aiTextObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    aiTextObserver.start()
    print('AI Watcher started')
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        aiTextObserver.stop()
    aiTextObserver.join()