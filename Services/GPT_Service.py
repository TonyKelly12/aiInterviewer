import openai

import os
import time

url = "your url here"
text_prompts = ['']
result = {}

async def prepChatbot(userHelloMessage):
    response = await openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": "You are a nervous amature front end developer you dont know much about backend programming"},
            {"role": "system", "content": " your name is Bob Crumbs you are trying to pass full stack code interview for my fictional company Oasis Bike Shop and Im interviewing you."},
            {"role": "user", "content": userHelloMessage },
        ]
    )
    print(response)
    return response

async def sendUserInput():
    userText = os.read('./userInput/text/transcript.txt')
    response = await openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "user", "content": userText},

        ]
    )
    print(response)
    return response

def sendInterviewQuestion(userQuestion: str):
    aiResponse = sendUserInput()
    return aiResponse


# Task for the event loop example async http calls

# def sendMessage():
#     tasks = []
#     for text in text_prompts:
#         tasks.append(session.get(url.format(text, ), ssl = False))
#         print('1st batch sent')
#         return tasks
    
# async def ask_question():

#     async with aiohttp.ClientSession() as session:
#         question = ''
#         responses = await asyncio.gather(*tasks)
#         for respnse in responses:
#             result.append(await response.json)

# # setting evenet loop to lisent to

# loop =  asyncio.get_event_loop()
# loop.run_until_complete(ask_question)
# loop.close()