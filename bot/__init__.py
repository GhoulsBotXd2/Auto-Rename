import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv

api_id = int(os.environ.get("26019444"))
api_hash = os.environ.get("a308fac723905cdbd836414b18f3b3d6")
bot_token = os.environ.get("6030548386:AAGv8q8mr1xbcS9a2dJQjc1GBlRtrst68IA")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("5860097723 5925926828 6046532356").split()))
ffmpeg = os.environ.get("FFMPEG", "")
suffix = os.environ.get("SUFFIX")

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
