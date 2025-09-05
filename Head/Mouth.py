import asyncio
import os
import threading
import edge_tts
import pygame
import time
from queue import Queue

# Voice configuration - using a natural female voice
VOICE = "en-US-AriaNeural"  # More natural female voice

# Initialize pygame once (not on every call)
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
print("Pygame mixer initialized")

# File management
AUDIO_QUEUE = Queue()
CURRENTLY_PLAYING = False

# Function to safely remove a file
def remove_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing file: {e}")

# Audio player thread function
def audio_player():
    global CURRENTLY_PLAYING
    while True:
        file_path = AUDIO_QUEUE.get()
        if file_path is None:  # Sentinel value to stop the thread
            break
            
        CURRENTLY_PLAYING = True
        try:
            sound = pygame.mixer.Sound(file_path)
            channel = sound.play()
            while channel and channel.get_busy():
                pygame.time.delay(10)
            remove_file(file_path)
        except Exception as e:
            print(f"Error during audio playback: {e}")
        finally:
            CURRENTLY_PLAYING = False
            AUDIO_QUEUE.task_done()

# Start audio player thread
audio_thread = threading.Thread(target=audio_player, daemon=True)
audio_thread.start()

# Async function to generate TTS with faster rate
async def generate_tts(TEXT, output_file) -> None:
    try:
        # Increased rate for faster speech
        communicator = edge_tts.Communicate(TEXT, VOICE, rate="-10%")
        await communicator.save(output_file)
        AUDIO_QUEUE.put(output_file)
    except Exception as e:
        print(f"Error during TTS generation: {e}")

# High-level function to speak text
def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), f"speak_{int(time.time()*1000)}.mp3")
    
    # Run TTS generation in a separate thread to avoid blocking
    tts_thread = threading.Thread(
        target=lambda: asyncio.run(generate_tts(TEXT, output_file)),
        daemon=True
    )
    tts_thread.start()

# Check if speech is currently playing
def is_speaking():
    return CURRENTLY_PLAYING or not AUDIO_QUEUE.empty()

# Pre-warm the TTS system by generating a small audio file upfront
def pre_warm_tts():
    """Generate a small audio file to warm up the TTS system"""
    warmup_file = os.path.join(os.getcwd(), "warmup.mp3")
    if not os.path.exists(warmup_file):
        print("Pre-warming TTS system...")
        asyncio.run(generate_tts("Hi", warmup_file))
        # Wait a moment for the file to be generated
        time.sleep(0.5)

# Pre-warm the TTS system when module is imported
# pre_warm_tts()

# Cleanup function
def cleanup():
    """Clean up any remaining audio files and stop the audio thread"""
    # Wait for current playback to finish
    while is_speaking():
        time.sleep(0.1)
    
    # Signal thread to stop
    AUDIO_QUEUE.put(None)
    
    # Remove any remaining audio files
    for file in os.listdir(os.getcwd()):
        if (file.startswith("speak_") and file.endswith(".mp3")) or file == "warmup.mp3":
            remove_file(file)

# Register cleanup on exit
import atexit
atexit.register(cleanup)

# Example usage
if __name__ == "__main__":
    speak("India, officially the Republic of India,[j][20] is a country in South Asia. It is the seventh-largest country by area; the most populous country since 2023;[21] and, since its independence in 1947, the world's most populous democracy.[22][23][24] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[k] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is near Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Myanmar, Thailand, and Indonesia.")
    time.sleep(4)  # Wait a bit for the first message to process
