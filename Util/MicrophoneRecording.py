import pyaudio
import wave


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def askInterviewQuestion():
    

    audioInst = pyaudio.PyAudio()

    stream = audioInst.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

    print('recording started.......')

    frames = []
    seconds = 8
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording Stopped")

    stream.stop_stream()
    stream.close()
    audioInst.terminate()


    wf = wave.open("../Outputs/UserOutputs/audio/userAudioInput.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audioInst.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

def userHello():
    audioInst = pyaudio.PyAudio()

    stream = audioInst.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

    print('Say Hello.......')

    frames = []
    seconds = 5
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording Stopped")

    stream.stop_stream()
    stream.close()
    audioInst.terminate()


    wf = wave.open("../Outputs/UserOutputs/audio/userAudioInput.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audioInst.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()
