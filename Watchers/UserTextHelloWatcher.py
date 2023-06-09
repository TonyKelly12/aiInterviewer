import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class UserHelloTextWatcher(FileSystemEventHandler):
    textCreated = False
    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        UserHelloTextWatcher.textCreated = True
               
    def startTextHelloWatcher():
        print('watching for hello text input')

def StartUserHelloTextWatcher():
    print('watching for hello text input')
    # put the path to the directory you want to monitor here
    path_to_watch = "../Outpputs/UserOutputs/text"
    event_handler = UserHelloTextWatcher()
    
    userHelloTextObserver = Observer()
    userHelloTextObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    userHelloTextObserver.start()
            
            
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        userHelloTextObserver.stop()
    
    userHelloTextObserver.join()
