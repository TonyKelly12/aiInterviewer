import os
import openai

def getGPTTokens():
    # openai.organization = os.getenv('gptOrgId')
    # openai.api_key = os.getenv("chatGPTkey")
    openai.organization = 'org-6wpeAfQvGl3akIgcIDepYjxB'
    openai.api_key = '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'
    openai.Model.list()

