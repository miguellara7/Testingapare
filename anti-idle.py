import subprocess
import time

def main():
    keys = "1 2 3"  # Replace with the keys you want to send

    print(f"Sending keys '{keys}' to the Tibia window")

    try:
        subprocess.Popen(['AutoIt3.exe', 'send_keys.au3'] + keys.split())
    except FileNotFoundError:
        print("AutoIt3.exe not found. Make sure you have AutoIt installed.")

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
