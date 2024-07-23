import requests
import pygame
import time

pygame.mixer.init()


def download_file(voice, message, output_filename):
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully and saved as {output_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")



# Generate and play the voice file
voiceType = input("Whose voice do you want? (check voiceTypes.txt for a full list of all voices): ")
filename = "speech.mp3"
with open("transcript.txt", "r") as file:
    lines = file.readlines()
    userMessage = lines[-1].strip() if lines else ""

download_file(voiceType, userMessage, filename)

# Play the voice file
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

# Wait until the audio playback is finished
while pygame.mixer.music.get_busy():
    time.sleep(1)

time.sleep(3)
