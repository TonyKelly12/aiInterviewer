from google.cloud import texttospeech 

import os


credentials = ''


def synthesize_speech(text, output_file):
    client = texttospeech.TextToSpeechClient(credentials=credentials)

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-D'
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        effects_profile_id=['telephony-class-application']
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_file, 'wb') as out:
        out.write(response.audio_content)

def runText2SpeachService():
    #to run app not locally setup auth service and call here
   aiText = os.read('./aiOutput/text/transcript.txt')
   outputFile = 'aiResponse.wav'
   synthesize_speech(aiText, outputFile)
   