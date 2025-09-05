# Task.py
import os
import subprocess
import time
import logging
import psutil
import pyautogui as gui
import pygetwindow as gw
import webbrowser
from google import genai
from Head.Mouth import speak

# ---------------- Logging ---------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Helper ---------------- #
def _is_process_running(process_name: str) -> bool:
    """Check if a process is already running."""
    try:
        process_name = process_name.lower()
        if not process_name.endswith(".exe"):
            process_name += ".exe"

        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == process_name:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return False
    except Exception:
        return False


# ---------------- Open App ---------------- #
def open_app(app_name: str):
    """
    Open an application with fallback methods:
    - Direct launch for known apps
    - Start UWP or websites
    - Fallback: use Win key search
    """
    app_name = app_name.lower()

    apps = {
        "notepad": "notepad.exe",
        "chrome": "chrome.exe",
        "vscode": "code.exe",
        "cmd": "cmd.exe",
        "calculator": "calc.exe",
        "settings": "ms-settings:",
        "camera": "microsoft.windows.camera:",
        "controlpanel": "control.exe",
    "youtube": "www.youtube.com",
    "facebook": "www.facebook.com",
    "github": "www.github.com",
    "youtube studio": "studio.youtube.com",
    "twitter": "www.twitter.com",
    "instagram": "www.instagram.com",
    "linkedin": "www.linkedin.com",
    "wikipedia": "www.wikipedia.org",
    "reddit": "www.reddit.com",
    "pinterest": "www.pinterest.com",
    "quora": "www.quora.com",
    "tumblr": "www.tumblr.com",
    "flickr": "www.flickr.com",
    "snapchat": "www.snapchat.com",
    "tiktok": "www.tiktok.com",
    "vimeo": "www.vimeo.com",
    "dropbox": "www.dropbox.com",
    "onedrive": "www.onedrive.com",
    "google drive": "drive.google.com",
    "icloud": "www.icloud.com",
    "amazon": "www.amazon.com",
    "ebay": "www.ebay.com",
    "alibaba": "www.alibaba.com",
    "netflix": "www.netflix.com",
    "hulu": "www.hulu.com",
    "disney plus": "www.disneyplus.com",
    "hbo max": "www.hbomax.com",
    "spotify": "www.spotify.com",
    "soundcloud": "www.soundcloud.com",
    "apple music": "www.apple.com/apple-music",
    "pandora": "www.pandora.com",
    "deezer": "www.deezer.com",
    "bandcamp": "www.bandcamp.com",
    "bbc": "www.bbc.com",
    "cnn": "www.cnn.com",
    "nytimes": "www.nytimes.com",
    "the guardian": "www.theguardian.com",
    "forbes": "www.forbes.com",
    "bloomberg": "www.bloomberg.com",
    "reuters": "www.reuters.com",
    "espn": "www.espn.com",
    "fox news": "www.foxnews.com",
    "nbc news": "www.nbcnews.com",
    "cbs news": "www.cbsnews.com",
    "abc news": "www.abcnews.go.com",
    "msnbc": "www.msnbc.com",
    "npr": "www.npr.org",
    "wsj": "www.wsj.com",
    "yahoo news": "news.yahoo.com",
    "buzzfeed": "www.buzzfeed.com",
    "huffpost": "www.huffpost.com",
    "canva": "www.canva.com",
    "chatgpt": "chat.openai.com",
    "slack": "www.slack.com",
    "trello": "www.trello.com",
    "asana": "www.asana.com",
    "zoom": "www.zoom.us",
    "skype": "www.skype.com",
    "microsoft teams": "www.microsoft.com/microsoft-teams",
    "google meet": "meet.google.com",
    "webex": "www.webex.com",
    "jira": "www.atlassian.com/software/jira",
    "notion": "www.notion.so",
    "airtable": "www.airtable.com",
    "monday": "www.monday.com",
    "clickup": "www.clickup.com",
    "dropbox paper": "www.dropbox.com/paper",
    "confluence": "www.atlassian.com/software/confluence",
    "figma": "www.figma.com",
    "adobe xd": "www.adobe.com/products/xd.html",
    "invision": "www.invisionapp.com",
    "microsoft word": "www.microsoft.com/microsoft-365/word",
    "google docs": "docs.google.com",
    "medium": "www.medium.com",
    "wordpress": "www.wordpress.com",
    "wix": "www.wix.com",
    "squarespace": "www.squarespace.com",
    "bigcommerce": "www.bigcommerce.com",
    "weebly": "www.weebly.com",
    "godaddy": "www.godaddy.com",
    "namecheap": "www.namecheap.com",
    "bluehost": "www.bluehost.com",
    "siteground": "www.siteground.com",
    "hostgator": "www.hostgator.com",
    "dreamhost": "www.dreamhost.com",
    "a2 hosting": "www.a2hosting.com",
    "inmotion hosting": "www.inmotionhosting.com",
    "digitalocean": "www.digitalocean.com",
    "linode": "www.linode.com",
    "aws": "aws.amazon.com",
    "azure": "azure.microsoft.com",
    "google cloud": "cloud.google.com",
    "heroku": "www.heroku.com",
    "gitlab": "www.gitlab.com",
    "bitbucket": "bitbucket.org",
    "codepen": "codepen.io",
    "jsfiddle": "jsfiddle.net",
    "repl.it": "repl.it",
    "stack overflow": "stackoverflow.com",
    "stackoverflow careers": "stackoverflow.com/jobs",
    "glassdoor": "www.glassdoor.com",
    "indeed": "www.indeed.com",
    "linkedin jobs": "www.linkedin.com/jobs",
    "monster": "www.monster.com",
    "simplyhired": "www.simplyhired.com",
    "angel.co": "angel.co",
    "github jobs": "jobs.github.com",
    "ziprecruiter": "www.ziprecruiter.com",
    "careerbuilder": "www.careerbuilder.com",
    "snagajob": "www.snagajob.com",
    "dice": "www.dice.com",
    "jobs": "www.jobs.com",
    "bamboohr": "www.bamboohr.com",
    "workday": "www.workday.com",
    "adp": "www.adp.com",
    "sap successfactors": "www.sap.com/products/hcm.html",
    "oracle hcm": "www.oracle.com/applications/human-capital-management",
    "zenefits": "www.zenefits.com",
    "paycor": "www.paycor.com",
    "paycom": "www.paycom.com",
    "gusto": "www.gusto.com",
    "square": "squareup.com",
    "stripe": "www.stripe.com",
    "paypal": "www.paypal.com",
    "venmo": "www.venmo.com",
    "cash app": "cash.app",
    "robinhood": "www.robinhood.com",
    "etrade": "www.etrade.com",
    "fidelity": "www.fidelity.com",
    "charles schwab": "www.schwab.com",
    "vanguard": "investor.vanguard.com",
    "td ameritrade": "www.tdameritrade.com",
    "coinbase": "www.coinbase.com",
    "binance": "www.binance.com",
    "kraken": "www.kraken.com",
    "blockchain": "www.blockchain.com",
    "gemini": "www.gemini.com",
    "bitfinex": "www.bitfinex.com",
    "bitstamp": "www.bitstamp.net",
    "bittrex": "www.bittrex.com",
    "okex": "www.okex.com",
    "poloniex": "www.poloniex.com",
    "coindesk": "www.coindesk.com",
    "cointelegraph": "www.cointelegraph.com",
    "decrypt": "www.decrypt.co",
    "cryptoslate": "www.cryptoslate.com",
    "cryptonews": "www.cryptonews.com",
    "coinmarketcap": "www.coinmarketcap.com",
    "coingecko": "www.coingecko.com",
    "messari": "www.messari.io",
    "icodrops": "www.icodrops.com",
    "tokenmarket": "www.tokenmarket.net",
    "coinpaprika": "www.coinpaprika.com",
    "cryptocompare": "www.cryptocompare.com",
    "coincheckup": "www.coincheckup.com",
    "cryptobriefing": "www.cryptobriefing.com",
    "blockonomi": "www.blockonomi.com",
    "coininsider": "www.coininsider.com",
    "newsbtc": "www.newsbtc.com",
    "bitcoin.com": "www.bitcoin.com",
    "ethereum.org": "www.ethereum.org",
    "litecoin.com": "www.litecoin.com",
    "ripple.com": "www.ripple.com",
    "cardano.org": "www.cardano.org",
    "stellarlumens.com": "www.stellarlumens.com",
    "tezos.com": "www.tezos.com",
    "eos.io": "www.eos.io",
    "neo.org": "www.neo.org",
    "iota.org": "www.iota.org",
    "monero.org": "www.monero.org",
    "zcash.org": "www.zcash.org",
    "dash": "www.dash.org",
    "dogecoin": "www.dogecoin.com",
    "gpt": "www.chatgpt.com/",
    "ope": "https://openai.com/",
    "wiki": "https://en.wikipedia.org/wiki/Wiki",
    "insta": "https://www.instagram.com/accounts/login/?hl=en",
    "studio": "https://studio.youtube.com/",
    "youtubestudio": "https://studio.youtube.com/",
    "telegram": "https://telegram.org/",
    "aajtak": "https://www.aajtak.in/",
    "openai": "https://openai.com/",
    "google": "https://www.google.co.in/",
    "googleaistudio": "https://aistudio.google.com/"

    }

    try:
        if app_name in apps:
            target = apps[app_name]
            speak(f"Please wait sir, I am opening {app_name}")
            time.sleep(5)
            # Skip if already running
            if _is_process_running(os.path.basename(target)):
                logging.info(f"{app_name} is already running")
                speak(f"{app_name} is already running on Background")
                return True

                       # Handle UWP or websites
            if target.endswith(":") or target.startswith("http") or "www." in target:
                os.system(f"start {target}")
            else:
                subprocess.Popen(target)

            logging.info(f"✅ Opened {app_name}")
            speak(f"Hello sir, I opened {app_name}")
            return 

        else:
            # Fallback: use Win+Search
            logging.warning(f"Unknown app {app_name}, using Win+Search fallback")
            gui.press("win")
            time.sleep(0.3)
            gui.write(app_name)
            time.sleep(0.3)
            gui.press("enter")

            if app_name in ["word","excel","powerpoint"]:
                time.sleep(2)
                gui.press("enter")
            return True

    except Exception as e:
        logging.error(f"❌ Failed to open {app_name}: {e}")
        return False


# ---------------- Close App ---------------- #
def close_app(app_name: str):
    """
    Close an application with multiple strategies:
    - psutil terminate()
    - taskkill (Windows native)
    - Alt+F4 for UWP windows
    """
    app_name = app_name.lower()
    closed = False
    speak(f"Yes sir, I'm just closing {app_name}")
    time.sleep(5)
    # 1. Try psutil
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if app_name in proc.info['name'].lower():
                proc.terminate()
                proc.wait(timeout=3)
                logging.info(f"🛑 Closed {proc.info['name']} (PID: {proc.info['pid']})")
                closed = True
                speak(f"Sir, i successfully close {app_name}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
            continue

    # 2. Try taskkill
    if not closed:
        try:
            result = subprocess.run(
                ["taskkill", "/f", "/im", f"{app_name}.exe"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            if result.returncode == 0:
                logging.info(f"✅ Closed {app_name} via taskkill")
                closed = True
                speak(f"Sir, i successfully close {app_name}")
        except Exception as e:
            logging.error(f"taskkill failed for {app_name}: {e}")

    # 3. Try Alt+F4 (UWP apps or unnamed processes)
    if not closed:
        try:
            windows = gw.getWindowsWithTitle(app_name)
            if windows:
                logging.info(f"⚠️ Closing UWP app window: {windows[0].title}")
                windows[0].activate()
                time.sleep(0.5)
                gui.hotkey("alt", "f4")
                closed = True
                speak(f"Sir, i successfully close {app_name}")
        except Exception as e:
            logging.error(f"Alt+F4 fallback failed for {app_name}: {e}")

    if not closed:
        logging.warning(f"❌ Could not close {app_name}")

    return closed


# ---------------- Write On App ---------------- #


# ---------------- Initialize Gemini Client ---------------- #
client = genai.Client(api_key="AIzaSyDign3hYl4k9IkV_24uptUGFgx6oTIOWvg")  # Replace with your key

# ---------------- Function to type slowly ---------------- #
def type_slowly(text, delay=0.05):
    """Types text character by character with a delay."""
    for char in text:
        gui.write(char)
        time.sleep(delay)

# ---------------- Write On App with Gemini & Auto File ---------------- #
def write_on(app: str, topic: str):
    app = app.lower()

    # Language -> file extension mapping
    language_mapping = {
        "python": ".py",
        "c": ".c",
        "c++": ".cpp",
        "java": ".java",
        "javascript": ".js",
        "html": ".html",
        "css": ".css",
        "json": ".json",
        "xml": ".xml",
        "markdown": ".md",
        "yaml": ".yaml",
        "text": ".txt",
    }

    # Default file name and extension
    file_name = "demo"
    file_extension = ".txt"

    # Detect language from user topic
    topic_lower = topic.lower()
    for lang, ext in language_mapping.items():
        if lang in topic_lower:
            file_extension = ext
            break

    # Create folder on Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop_path, "JarvisFiles")
    os.makedirs(folder_path, exist_ok=True)

    # Unique file name
    timestamp = int(time.time())
    file_path = os.path.join(folder_path, f"{file_name}_{timestamp}{file_extension}")

    try:
        # 1️⃣ Generate content with Gemini
        prompt = f"Write a professional, clean version of this: {topic}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        generated_text = response.text.strip()

        # 2️⃣ Open the app
        if app == "vscode":
            # VSCode supports new tab with -n
            subprocess.Popen(["code", "-n", file_path])
            time.sleep(2)  # wait for new tab
        elif app in ["notepad", "word"]:
            # Open or focus the app
            open_app(app)
            time.sleep(2)  # wait for app to open
            gui.hotkey('ctrl', 't')
            gui.write(os.path.basename(file_path))
            gui.press("enter")
        else:
            open_app(app)
            time.sleep(2)

        # 3️⃣ Type the generated text slowly
        time.sleep(4)
        type_slowly(generated_text, delay=0.05)

        return f"📝 File '{os.path.basename(file_path)}' created and written in {app}."

    except Exception as e:
        return f"❌ Failed to write on {app}: {e}"




def search_on(user_text:str,app:str):
    """
    1. Ask the user what to write
    2. Listen to voice input
    3. Slowly type it on screen
    """
    if app == "youtube":
        gui.hotkey('tab')
        gui.hotkey('tab')
        gui.hotkey('tab')
        gui.hotkey('tab')

    if user_text:
        speak(f"Writing sir")
        gui.hotkey('ctrl','a')
        type_slowly(user_text)
        time.sleep(2)
        gui.hotkey("enter")
    else:
        speak("I didn't hear anything.")