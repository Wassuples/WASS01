import pyaudio
import wave
import numpy as np

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 500  # Minimum amplitude threshold to detect audio
SILENCE_DURATION = 3  # Time in seconds to wait before stopping recording after silence


def is_silent(data):
    audio_data = np.frombuffer(data, dtype=np.int16)
    return np.max(np.abs(audio_data)) < THRESHOLD


def main():
    audio = pyaudio.PyAudio()

    # Open the microphone stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=1,
                        frames_per_buffer=CHUNK)

    frames = []
    silent_counter = 0
    recording = True

    print("Recording...")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

        if is_silent(data):
            silent_counter += CHUNK / RATE
            if silent_counter > SILENCE_DURATION:
                recording = False
        else:
            silent_counter = 0

    print("Finished recording! ")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data to a WAV file
    with wave.open("output.wav", 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


if __name__ == "__main__":
    main()
