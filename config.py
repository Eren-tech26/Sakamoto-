import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 14457171

API_HASH = "a65975d31ab29dce12992cb1f78688de"

BOT_TOKEN = "7616480254:AAFwqQ4CfuEENBvnhYzmgTHbLNsuld8XB_0"

BOT_ID = 7616480254

BOT_USERNAME = "@Aethonixmusicbot"

OWNER_USERNAME = "@eren_aethonix"

BOT_NAME = "˹𝐀ᴇᴛʜᴏɴɪ𝐱 ꭙ 𝐌ᴜ𝐬ɪᴄ ˼™"

ASSUSERNAME = "@batmanplayzz"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", "30DxNexGenBots107029")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", "-1002812568647"))

DISASTER_LOG = -1002346695101

OWNER_ID = 7774827065

SPECIAL_USER = 7774827065

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/aethonixsupport"

SUPPORT_CHAT = "https://t.me/igrischatsupport"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "AQDcmVMAQ6U-pUX8DCPf55dv9SzXnERzwOhQ0Z2SgBqcAHmNa4JYrugy7QPLujrYMpX2Ms2oaibjV1EJCOaCdrGqbiRqfm6fYs943WeNSW2zp-cCUjDiTF14psir4oAJmQgn2_WD59LXe-dMkQK21w81TIW2QbGQNsHKv0-Y-So-3rHtyQ2Z1q1BSThrWvIQH_I6sVckr017NUDOY3TmHUwH3EX0Awjm4OQIlykyeeaMRe9bRGOEzsCzOQZsPgfJU9jmk0nuH8ZeizsO4gN3ACkq4HooOkpQbnYrLjGfoEdPLHVjCMuv4YPVkbHhhzTmz18ccjDYwKe1EoDTg6niXdPssQNByAAAAAGzshfkAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL =  "https://i.ibb.co/Xr3J7Kv3/photo-2025-10-13-10-24-24-7560650262243704856.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
STATS_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
STREAM_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/kgvX7FPC/photo-2025-10-13-10-24-24-7560650262243704836.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
