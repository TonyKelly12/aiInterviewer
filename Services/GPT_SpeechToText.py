# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../Auth')
sys.path.insert(2, '../Watchers')
import Auth

basePath = "C:/Users/Tony/Documents/Repos/ai-interviwer"
def speechToText(FilePathToOpen: str, OutputFilePath: str):
    # audio_file= open("./userInput/audio/micRecord.wav", "rb")
    print(FilePathToOpen)
    print(OutputFilePath)
    audio_file= open(basePath + FilePathToOpen, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript)
    with open(OutputFilePath, 'w') as f:
        f.write(transcript.text)
        # Delete audio file after transcript
        if os.path.exists(OutputFilePath):
            os.remove(basePath + FilePathToOpen)

# Note: This file is used to take users voice and translate to text to send to chat gpt
def runGPTService(FilePathToOpen: str, OutputFilePath: str):
    print(FilePathToOpen)
    print(OutputFilePath)
    Auth.getGPTTokens()
    speechToText(FilePathToOpen, OutputFilePath)

