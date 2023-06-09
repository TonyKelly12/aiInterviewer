import os

def getAiText():
    print('getting ai text')
    #to run app not locally setup auth service and call here
    aiText = os.read('./aiResponse.txt')
    return aiText