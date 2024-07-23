import os

def run_script(script_name):
    exit_code = os.system(f"python {script_name}")
    if exit_code != 0:
        print(f"Error running {script_name} with exit code {exit_code}")

def main():
    scripts = ["audioRecording.py", "speechRecognizer.py", "se.py"]

    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
