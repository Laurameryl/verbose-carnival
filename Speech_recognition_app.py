# speech_recognition_simple.py
import speech_recognition as sr
import os

def simple_speech_recognition():
    """Simplified speech recognition function"""
    r = sr.Recognizer()
    
    # Use a different approach to avoid PyAudio issues
    try:
        # Method 1: Use with statement properly
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Speak now!")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        
        print("Processing...")
        
        # Try Google recognition
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Google API error: {e}")
            
    except Exception as e:
        print(f"Error: {e}")
        print("PyAudio might not be installed correctly")
        
        # Alternative: Use audio file instead of microphone
        print("Trying with audio file instead...")
        return recognize_from_file(r)

def recognize_from_file(recognizer):
    """Recognize speech from an audio file"""
    try:
        # Use an existing audio file
        audio_file = sr.AudioFile('test_audio.wav')
        with audio_file as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio)
        print(f"From file: {text}")
        return text
    except FileNotFoundError:
        print("No audio file found. Please create 'test_audio.wav'")
    except Exception as e:
        print(f"File recognition error: {e}")
    
    return None

if __name__ == "__main__":
    print("Speech Recognition Test")
    result = simple_speech_recognition()
    
    if result:
        print(f"Success! Recognized: {result}")
    else:
        print("Recognition failed")