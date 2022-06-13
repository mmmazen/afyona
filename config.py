## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAA0iB-wXm6QYJdyveZIB0yDnstWDFjL3v0pGFMsFpJea79J-yjGf1CN-_m7eobORBV0unoEbIINtEmoEj0Cj-HJo6BEpTjpgXXRq_NC5wa5-DoAgghTjuci3SD0Vek6BXx2L20CtqEKMdxfHQY_kmnwSd40to0MdCAz8EobBkGOPi75QrbPItiYSW9_K01oEV_BlvhGYg0G0hTP00v-i_ZxSDwL1gpyttTeqffGVpgRl9Pm-81eND5tHYYpVSJ1nGsqyY7NurEGHbLWF84HCL4FZfuISes0Q91aJraKEY-8qOHf0YGMR0o5L1tfmtLpfs-L1xw3Pw3yuEfG9UZ4uLyBAAAAAULL5YcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5311669922:AAFEDNdIrbfG7Kwacl2iSKHmMJTsLuSiyJk")
BOT_NAME = getenv("BOT_NAME", "𝐌𝐔𝐒𝐈𝐂 | 𓆩𝄠⃝—͟͟͞͞🖤𝑪𝑯𝑰𝑻𝑶𝑺𝑬࿐⁽ ͢ᵛᵎᵖ᭄𓆪")
API_ID = int(getenv("API_ID", "12081576"))
API_HASH = getenv("API_HASH", "5390fdb0c3d15fc9025ede65d6ccdb96")
OWNER_NAME = getenv("OWNER_NAME", ".")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xx_A_f_y_o_n_a_xX")
ALIVE_NAME = getenv("ALIVE_NAME", ".")
BOT_USERNAME = getenv("BOT_USERNAME", "MuSiC_mazen_bot")
OWNER_ID = getenv("OWNER_ID", "5139632128")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "xXA_f_y_o_n_aXx")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "G_afyona")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CH_afyona")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5139632128").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
