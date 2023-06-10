import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UserTextWatcher(FileSystemEventHandler):
    userTextCreated = False 
    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        UserTextWatcher.userTextCreated = True

def StartUserTextWatcher():
    print('watching for user text input')
    # put the path to the directory you want to monitor here
    path_to_watch = "C:/Users/Tony/Documents/Repos/pythonEnvironments/AiInterview/Outpputs/UserOutputs/text"
    event_handler = UserTextWatcher()
    
    userTextObserver = Observer()
    userTextObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    userTextObserver.start()
    print('user text watcher started')
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        userTextObserver.stop()
    
    userTextObserver.join()
