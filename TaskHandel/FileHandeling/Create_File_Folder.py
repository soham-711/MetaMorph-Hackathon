import os
import re

FILE_EXTENSIONS = {
    "python file": ".py",
    "java file": ".java",
    "text file": ".txt",
    "html file": ".html",
    "css file": ".css",
    "javascript file": ".js",
    "json file": ".json",
    "xml file": ".xml",
    "csv file": ".csv",
    "markdown file": ".md",
    "yaml file": ".yaml",
    "image file": ".jpg",
    "video file": ".mp4",
    "audio file": ".mp3",
    "pdf file": ".pdf",
    "word file": ".docx",
    "excel file": ".xlsx",
    "powerpoint file": ".pptx",
    "zip file": ".zip",
    "tar file": ".tar",
}

def get_file_extension(text: str) -> str:
    for key, ext in FILE_EXTENSIONS.items():
        if key in text:
            return ext
    return ".txt"

def clean_text(text: str) -> str:
    text = text.lower()

    # Remove "create", "named", "with name"
    text = re.sub(r"\b(create|named|with name)\b", "", text)

    # Remove all file type keywords (python file, text file, etc.)
    for key in FILE_EXTENSIONS.keys():
        text = text.replace(key, "")

    # Remove "file" word alone
    text = re.sub(r"\bfile\b", "", text)

    # Clean extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def create_file_on_desktop(user_text: str) -> str:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = "JarvisFiles"
    folder_path = os.path.join(desktop_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    extension = get_file_extension(user_text)
    file_name = clean_text(user_text)
    if not file_name:
        file_name = "demo"

    file_path = os.path.join(folder_path, f"{file_name}{extension}")

    try:
        with open(file_path, "w", encoding="utf-8"):
            pass
        return f"✅ Your file is created successfully on Desktop in '{folder_name}'\n📂 File name: {file_name}{extension}"
    except Exception as e:
        return f"❌ Failed to create file: {str(e)}"


import os

def create_folder(slots):
    try:
        # Extract folder name from slots
        topic = slots.get("topic", "")
        
        # Clean folder name (remove "create a folder named" etc.)
        folder_name = topic.replace("create a folder named", "").strip()
        
        if not folder_name:
            return "❌ I couldn't detect the folder name."

        # Get Desktop path
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = os.path.join(desktop, folder_name)

        # Create folder if not exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            return f"✅ Folder '{folder_name}' created successfully on Desktop."
        else:
            return f"⚠️ Folder '{folder_name}' already exists on Desktop."

    except Exception as e:
        return f"❌ Error creating folder: {str(e)}"


