import os
import multiprocessing
import tkinter as tk
from Services import prepChatbot, sendInterviewQuestion
from Util import userHello, askInterviewQuestion
from Watchers import StartAITextWatcher, StartUserAudioHelloWatcher,StartUserAudioWatcher,StartUserTextWatcher, UserHelloTextWatcher, UserTextWatcher,AITextWatcher,UserAudioHelloWatcher,UserAudioWatcher
from Outpputs import getUserAudio, getUserText, getAiAudio, getAiText

class InterviewGUI:
    def __init__(self):

        self.root = tk.Tk()
        font = "Arial"
        # App window size

        self.root.geometry("800x1000")
        self.root.title("AI Interview")

        # Widgets

        self.content = tk.Frame(self.root)
        self.frame = tk.Frame(self.content, borderwidth=5, relief="ridge", width=100, height=100)
        self.namelbl = tk.Label(self.content, text="Name")

        self.videoButton = tk.Button(self.content, text="Start Chat", command=self.startChat)
        self.Mic = tk.Button(self.content, text="ASk Interview Question", command=self.askInterviewQuestion)

        # Style

      

        # Layout

        self.content.grid(column=0, row=0)
        self.frame.grid(column=4, row=1, columnspan=2, rowspan=2)
        self.namelbl.grid(column=4, row=0, columnspan=2)
        self.videoButton.grid(column=1, row=2)
        self.Mic.grid(column=2, row=2)

        self.root.mainloop()
    
    
    def startWatchers(event):
        if __name__ == "__main__":
            AITextWatcher.process = multiprocessing.Process(target=AITextWatcher.StartAITextWatcher)
            AITextWatcher.process.start()

            UserAudioHelloWatcher.process = multiprocessing.Process(target=UserAudioHelloWatcher.StartUserAudioHelloWatcher)
            UserAudioHelloWatcher.process.start()

            UserAudioWatcher.process = multiprocessing.Process(target=UserAudioWatcher.StartUserAudioWatcher)
            UserAudioWatcher.process.start()

            UserHelloTextWatcher.process = multiprocessing.Process(target=UserHelloTextWatcher.StartUserHelloTextWatcher)
            UserHelloTextWatcher.process.start()

            UserTextWatcher.process = multiprocessing.Process(target=UserTextWatcher.StartUserTextWatcher)
            UserTextWatcher.process.start()

    def stopWatchers(event):
        AITextWatcher.process.terminate()
        UserAudioHelloWatcher.process.terminate()
        UserAudioWatcher.process.terminate()
        UserHelloTextWatcher.process.terminate()
        UserTextWatcher.process.terminate()

    def startChat(event):

        
        InterviewGUI.startWatchers(event)

        userHello()

        if UserHelloTextWatcher.textCreated == True:
            userHelloText = getUserText()
            print(userHelloText)
    
            aiResponse = prepChatbot(userHelloText)
            print(aiResponse)
        else:
            print("No text file created")

    def askInterviewQuestion(event):
        print("Ask Interview Question")
        askInterviewQuestion()

        if UserTextWatcher.textCreated == True:
            userText = getUserText()
            print(userText)
    
            aiResponse = sendInterviewQuestion(userText)
            print(aiResponse)
        else:
            print("No text file created")
    

InterviewGUI()