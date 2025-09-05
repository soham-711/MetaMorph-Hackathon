# Intent.py
import google.generativeai as genai
import json
import re
import os
#New: AIzaSyArl6e1AkGWn53blXONGLj-KeH3aGKbl2w
#OLd: AIzaSyDdACIU3h59herh6ZjZnNw0oav4xRe8gK8
# 1. Configure API key (make sure it's set as ENV variable first)
genai.configure(api_key="AIzaSyBwCAiptjgLM6egMvVnR5TR-GjmxBj7YV8")

# 2. Create model instance
model = genai.GenerativeModel("gemini-2.0-flash")

# 3. Prompt template (forcing strict JSON output)
PROMPT_TEMPLATE = """
You are an intent classification system.
Classify the following user input into a JSON structure.

Rules:
- Always return ONLY valid JSON (no explanations, no markdown).
- Check the word (spelling mistake, auto detection from part of word like: notpat-> notepad, corom-> chorom,vs code -> vscode, cs -> css ).
INSTRUCTION
 1. where key should be "app" and "topic"
 2. if the user prompt about write/generate something but there missing where to write(on which app) the topic then by default set app to    "notepad"  (   ex:
   User: "please write a leave  application"
   Output:{{"type":"command","intent":"write_on","slots": {{"app": "notepad","topic":"write a leave application"}} }}
     )
  3.Intent must be "open_app" or "write_on" or "general_question" or "close_app" or "check_battery"or "set_brightness" (for "set_brightness" topic should be in integer like 30,60 no '30' or '60') or "create_file" (fir intent "create_file", "topic" should be like "create python file named test" ) or "create_folder"("app": should be desktop ,"topic": create a folder named/name with test) or "set_volume" (for "volume" topic should be in integer like 30,60 no '30' or '60') or "take_photo" or "scroll_up" or "scroll_down" or "scroll_to_top" or "scroll_to_bottom" or "open_new_tab" or "close_tab" or "open_browser_menu" or "zoom_in" or "zoom_out" or "refresh_page" or "switch_to_next_tab" or "switch_to_previous_tab" or "open_history" or "open_bookmarks" or "go_back" or "go_forward" or "open_dev_tools" or "toggle_full_screen" or "open_private_window" or "send_message"(for "send_message" "app": should be social media platform(whatsapp/facebook), "topic": "What message user want to send", "to": "recipient name that user will provide" ) or "run_code" or "on_wifi" or "off_wifi" or "on_bluetooth" or "off_bluetooth" or "search_on"(topic should be that user want to search and app: if user say any thing or null) or "minimize_tab" or "maximize_tab" or "separate_tab" based on the user command
  
  5. User:"Bye||hello||ok||hi" all should be go on general_question 
- JSON format must be:
  {{
    "type": "<command|qa>",
    "intent": "<string>",
    "slots": {{ "key": "value" }} OR {{"key":null}}
  }}
  6. Some times when user say "Please open Word then some text..." then it comes "open what" like somethings so please maanage this.

Examples:

User: "Can you open Chrome?"
Output: {{"type": "command", "intent": "open_app", "slots": {{"app": "chrome"}}}}

User: "create a html file?"
Output: {{"type": "command", "intent": "create_file", "slots": {{"app": "Desktop","topic":"create html file named test"}}}}


User: "please write/genarate a python calculator programm on vscode"
Output:{{"type":"command","intent":"write_on","slots": {{"app": "vscode","topic":"calculator programm in python"}} }}

User: "please write a leave  application"
Output:{{"type":"command","intent":"write_on","slots": {{"app": "notepad","topic":"write a leave application"}} }}

User: "What is recursion?"
Output: {{"type": "qa", "intent": "general_question", "slots": {{}}}}

Now classify this input:
"{user_input}"
"""

def parse_intent(user_input: str) -> dict:
    try:
        prompt = PROMPT_TEMPLATE.format(user_input=user_input)
        response = model.generate_content(prompt)

        # Extract only JSON from response
        text = response.text.strip()
        json_match = re.search(r"\{.*\}", text, re.DOTALL)

        if json_match:
            json_str = json_match.group(0)
            return json.loads(json_str)
        else:
            return {"type": "other", "intent": "unknown", "slots": {}}

    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    tests = [
      "Please close corom"
    ]
    for t in tests:
        print(f"User: {t}")
        print("Intent:", parse_intent(t))
        print("-" * 50)



