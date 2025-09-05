# # from Intent import parse_intent

# # def main():
# #     print("🧠 Brain active. Type 'exit' to quit.")
    
# #     while True:
# #         user_input = input("You: ")
# #         if user_input.lower() in ["exit", "quit"]:
# #             print("🧠 Brain shutting down...")
# #             break
        
# #         intent_json = parse_intent(user_input)
# #         print("Intent:", intent_json)

# # if __name__ == "__main__":
# #     main()
# # Brain.py

# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from Intent import parse_intent
# from TaskHandel.Task import handle_task
# from Head.Ear import listen
# import google.generativeai as genai

# # Gemini setup for answering general questions
# genai.configure(api_key="AIzaSyC4zncReO3mGixZU0b6m75I9AWP3FDbrE8")
# qa_model = genai.GenerativeModel("gemini-1.5-flash")

# def main():
#     print("🧠 Brain active. Type 'exit' to quit.")

#     while True:
#         user_input = listen()
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
#     main()
