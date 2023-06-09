import os

def getUserAudio():
    print('getting ai audio')
    #to run app not locally setup auth service and call here
    userAudio = os.read('./userAudioInput.wav')
    return userAudio