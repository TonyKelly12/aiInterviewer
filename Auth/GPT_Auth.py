import os
import openai

def getGPTTokens():
    # openai.organization = os.getenv('gptOrgId')
    # openai.api_key = os.getenv("chatGPTkey")
    openai.organization = ''
    openai.api_key = ''
    openai.Model.list()

