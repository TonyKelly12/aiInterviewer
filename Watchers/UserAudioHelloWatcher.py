import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Services import runGPTService


openFilePath = "../Outpputs/UserOutputs/audio/userAudioInput.wav"
writeFilePath = "../Outpputs/UserOutputs/text/userTextInput.txt"
class UserAudioHelloWatcher(FileSystemEventHandler):
 

    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')
        print('file has been created')
        runGPTService(openFilePath, writeFilePath)
    
    def startAudioHelloWatcher():
        print('watching for user Hello input')
        # put the path to the directory you want to monitor here


def StartUserAudioHelloWatcher():
    print('watching for user Hello input')
    # put the path to the directory you want to monitor here
    path_to_watch = "../Outpputs/UserOutputs/audio"
    event_handler = UserAudioHelloWatcher()
    userAudioHelloObserver = Observer()
    userAudioHelloObserver.schedule(event_handler, path=path_to_watch, recursive=True)
    userAudioHelloObserver.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        userAudioHelloObserver.stop()

    userAudioHelloObserver.join()