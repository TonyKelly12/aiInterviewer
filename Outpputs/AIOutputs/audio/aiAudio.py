import os

def getAiAudio():
    print('getting ai audio')
    #to run app not locally setup auth service and call here
    aiAudio = os.read('./aiResponse.wav')
    return aiAudio