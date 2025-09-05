import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # auto-calibration
        recognizer.pause_threshold = 1.0        # how long silence before stop (sec)
        recognizer.non_speaking_duration = 0.5  # extra silence padding
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("🗣️ You said:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand speech")
        return ""
    except sr.RequestError:
        print("⚠️ API request failed")
        return ""

def main():
    while True:
        result = listen()
        if result:
            if "stop" in result.lower():
                print("👋 Exiting...")
                break

if __name__ == "__main__":
    main()
