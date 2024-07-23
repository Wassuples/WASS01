import assemblyai as aai

aai.settings.api_key = "INSERT ASSEMBLYAI API KEY HERE"

# file to transcribe
FILE_URL = "output.wav"

print("Transcribing... ")
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

OUTPUT_FILE = "transcript.txt"

with open(OUTPUT_FILE, 'a') as f:
    if transcript.status == aai.TranscriptStatus.error:
        f.write(f"\nError: {transcript.error}")
    else:
        f.write(f"\n{transcript.text}")
        print("Finished transcribing! ")
