import time
from Services.GoogleTextToSpeechService import runText2SpeachService
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AITextWatcher(FileSystemEventHandler):
          
    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        runText2SpeachService()

def StartAITextWatcher():
    path_to_watch = "./Outpputs/AIOutputs/text"
    event_handler = AITextWatcher()
    aiTextObserver = Observer()
    aiTextObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    aiTextObserver.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        aiTextObserver.stop()
    aiTextObserver.join()