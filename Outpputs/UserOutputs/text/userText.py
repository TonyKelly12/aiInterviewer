import os

def getUserText():
    print('getting ai text')
    #to run app not locally setup auth service and call here
    userText = os.read('./userTextResponse.txt')
    return userText