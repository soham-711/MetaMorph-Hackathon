# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from IntentsCreation.Intent import parse_intent
# from TaskHandel.Task import handle_task
# from Head.Ear import listen
# import google.generativeai as genai

# # Gemini setup for answering general questions
# genai.configure(api_key="AIzaSyC4zncReO3mGixZU0b6m75I9AWP3FDbrE8")
# qa_model = genai.GenerativeModel("gemini-1.5-flash")

# def brain():
#     print("🧠 Brain active. Type 'exit' to quit.")
#     user_input = listen()
#     while True:
#         if user_input.lower() in ["exit", "quit"]:
#             print("🧠 Brain shutting down...")
#             break

#         intent_json = parse_intent(user_input)
#         print("🧐 Intent detected:", intent_json)

#         if intent_json.get("intent") == "general_question":
#             response = qa_model.generate_content(user_input)
#             print("🤖 Jarvis:", response.text.strip())
#         else:
#             result = handle_task(intent_json)
#             print("🤖 Jarvis:", result)

# if __name__ == "__main__":
#     brain()



# # Head/Brain.py
# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from IntentsCreation.Intent import parse_intent
# from TaskHandel.Task import handle_task
# from Head.Ear import listen
# from Head.Mouth import speak
# import google.generativeai as genai

# # Gemini setup
# genai.configure(api_key="AIzaSyArl6e1AkGWn53blXONGLj-KeH3aGKbl2w")
# qa_model = genai.GenerativeModel("gemini-1.5-flash")

# def brain():
#     print("🧠 Brain active. Say 'exit' to quit.")

#     while True:
#         # 🎤 Listen from mic
#         user_input = listen()

#         # If STT failed → skip instead of crashing
#         if not user_input or user_input.strip() == "":
#             print("❌ No speech detected. Trying again...")
#             continue

#         if user_input.lower() in ["exit", "quit"]:
#             print("🧠 Brain shutting down...")
#             speak("Goodbye, shutting down.")
#             break

#         # Parse intent
#         intent_json = parse_intent(user_input)
#         print("🧐 Intent detected:", intent_json)

#         # Handle intent
#         if intent_json.get("intent") == "general_question":
#             try:
#                 response = qa_model.generate_content(user_input)
#                 answer = response.text.strip()
#                 print("🤖 Jarvis:", answer)
#                 speak(answer)
#             except Exception as e:
#                 print("⚠️ Gemini error:", e)
#                 speak("Sorry, I couldn't process that.")
#         else:
#             result = handle_task(intent_json)
#             print("🤖 Jarvis:", result)
#             speak(result)



# Head/Brain.py
from IntentsCreation.Intent import parse_intent
from TaskHandel.Task import handle_task
from Head.Ear import listen
from Head.Mouth import speak
import google.generativeai as genai
from Config.Config import GEMINI_API_KEY

# Gemini setup
genai.configure(api_key=GEMINI_API_KEY)
qa_model = genai.GenerativeModel("gemini-1.5-flash")

def brain():
    print("🧠 Brain active. Say 'exit' to stop this session.")

    while True:
        user_input = listen()

        if not user_input or user_input.strip() == "":
            print("❌ No speech detected. Trying again...")
            continue

        if user_input.lower() in ["exit", "quit", "stop"]:
            print("🧠 Brain shutting down for now...")
            speak("Okay, going back to sleep.")
            return  # 👈 returns to main.py instead of breaking everything

        # Parse intent
        intent_json = parse_intent(user_input)
        print("🧐 Intent detected:", intent_json)

        if intent_json.get("intent") == "general_question":
            try:
                response = qa_model.generate_content(user_input)
                answer = response.text.strip()
                print("🤖 Jarvis:", answer)
                speak(answer)
            except Exception as e:
                print("⚠️ Gemini error:", e)
                speak("Sorry, I couldn't process that.")
        else:
            result = handle_task(intent_json)
            print("🤖 Jarvis:", result)
            speak(result)



