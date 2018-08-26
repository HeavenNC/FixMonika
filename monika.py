
# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import wikipedia
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit

#client = LINE()
client = LINE("EwJ5ZGjuQT3v5mGfJ6Y1.iqPpPFnwvkad61U6Am51Oq.Gf347c5IgpwMPLPHEogWnVQ6LOmsfhk7zdC7Y5xOpPc=")
admin = ["u9e36c0029c31e1c1d6c36a8a7c13ff37"]
mid = client.getProfile().mid
Bots = [mid]
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()

msg_dict = {}

welcome = []

settings = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": True,
    "autoRespon": True,
    "autoJoinTicket": True,
    "checkContact": True,
    "checkPost": True,
    "checkSticker": False,
    "timeRestart": "18000",
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "setKey": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait = {
    "Sider":True,
    "selfbot":True,
    "welcome": "Selamat Datang Semoga Betah (^_^)\n\nSupport By:\n\n????F?????\n??? ? J?????????????\n??????????\n??? ? J??SHOP?\n????????????\n? t?????????\n? t?????????Public\n???? ????? ???\n\nCreator : http://line.me/ti/p/~syifaabyananta",
    "leave": "Good Bye, See You Next Time\n\nSupport By:\n\n????F?????\n??? ? J?????????????\n??????????\n??? ? J??SHOP?\n????????????\n? t?????????\n? t?????????Public\n???? ????? ???\n\nCreator : http://line.me/ti/p/~syifaabyananta"
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        time.sleep(5)
        restartBot()
    
gkey = 'AIzaSyCL0E6vt3nun4BAJ-P8_HC61sTsqEnlqUw'

def urlshortener(url, googleapi_key):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + \
        googleapi_key
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        return r.json().get('id')
    elif r.status_code == 400:
        raise KeyError('Can not generate minified url, Reason:', r.json().get('error', {}).get('errors')[0].get('reason'))
    raise KeyError('Invalid Google Api Key or url')

def urlexpander(short_url, googleapi_key):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key=' + \
        googleapi_key
    payload = {'shortUrl': short_url}
    try:
        r = requests.get(post_url, params=payload)
        return r.json()['longUrl']
    except:
        raise Exception('The shorturl does not exist')

def qrcode(url):
    return 'http://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=' + url

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def welcomeMessage(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ╰══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n  ╰══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ╰══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n  ╰══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@irenebot "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMessage1 =	"╔══[ Help Message ]" + "\n" + \
					"╠ " + key + "Help" + "\n" + \
					"╠ " + key + "Translate" + "\n" + \
					"╠ " + key + "TTS" + "\n" + \
					"╠ " + key + "Help setting" + "\n" + \
					"╠ " + key + "Help admin" + "\n" + \
					"╠ " + key + "List alquran" + "\n" + \
					"╠ " + key + "Memelist" + "\n" + \
					"╠ " + key + "Welcome「On/Off」" + "\n" + \
					"╠ " + key + "Bye Irene (Untuk Mengeluarkan BOT" + "\n" + \
					"╠══[ BOT Command ]" + "\n" + \
					"╠ " + key + "Me" + "\n" + \
					"╠ " + key + "MyMid" + "\n" + \
					"╠ " + key + "MyName" + "\n" + \
					"╠ " + key + "MyBio" + "\n" + \
					"╠ " + key + "MyPicture" + "\n" + \
					"╠ " + key + "MyVideoProfile" + "\n" + \
					"╠ " + key + "MyCover" + "\n" + \
					"╠ " + key + "StealContact「Mention」" + "\n" + \
					"╠ " + key + "StealMid「Mention」" + "\n" + \
					"╠ " + key + "StealName「Mention」" + "\n" + \
					"╠ " + key + "StealBio「Mention」" + "\n" + \
					"╠ " + key + "StealPicture「Mention」" + "\n" + \
					"╠ " + key + "StealVideoProfile「Mention」" + "\n" + \
					"╠ " + key + "StealCover「Mention」" + "\n" + \
					"╠══[ Group Command ]" + "\n" + \
					"╠ " + key + "GroupCreator" + "\n" + \
					"╠ " + key + "GroupId" + "\n" + \
					"╠ " + key + "GroupName" + "\n" + \
					"╠ " + key + "GroupPicture" + "\n" + \
					"╠ " + key + "GroupTicket" + "\n" + \
					"╠ " + key + "GroupTicket「On/Off」" + "\n" + \
					"╠ " + key + "GroupList" + "\n" + \
					"╠ " + key + "GroupMemberList" + "\n" + \
					"╠ " + key + "GroupInfo" + "\n" + \
					"╠ " + key + "ChangeGroupPicture" + "\n" + \
					"╠══[ Special Command ]" + "\n" + \
					"╠ " + key + "Mention" + "\n" + \
					"╠ " + key + "Lurking「On/Off/Reset」" + "\n" + \
					"╠ " + key + "Lurking" + "\n" + \
					"╠ " + key + "Sider「On/Off」" + "\n" + \
                    "╠══[ Media Command ]" + "\n" + \
                    "╠ " + key + "CheckDate「Date」" + "\n" + \
                    "╠ " + key + "CheckWebsite「url」" + "\n" + \
                    "╠ " + key + "CheckPraytime「Location」" + "\n" + \
                    "╠ " + key + "CheckWeather「Location」" + "\n" + \
                    "╠ " + key + "CheckLocation「Location」" + "\n" + \
                    "╠ " + key + "InstaInfo 「UserName」" + "\n" + \
                    "╠ " + key + "InstaPost 「UserName」|「Number」" + "\n" + \
                    "╠ " + key + "InstaStory 「UserName」|「Number」" + "\n" + \
                    "╠ " + key + "SearchYoutube「Search」" + "\n" + \
                    "╠ " + key + "SearchMusic 「Search」" + "\n" + \
                    "╠ " + key + "SearchLyric 「Search」" + "\n" + \
                    "╠ " + key + "SearchImage 「Search」" + "\n" + \
                    "╚══[ Copyright Irene BOT ]"
    return helpMessage1

def settingmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
        settingMessage = "╔══[ Settings Command ]" + "\n" + \
									 "╠ " + key + "AutoAdd「On/Off」" + "\n" + \
									 "╠ " + key + "AutoJoin「On/Off」" + "\n" + \
									 "╠ " + key + "AutoJoinTicket「On/Off」" + "\n" + \
									 "╠ " + key + "AutoLeave「On/Off」" + "\n" + \
									 "╠ " + key + "AutoRead「On/Off」" + "\n" + \
									 "╠ " + key + "AutoRespon「On/Off」" + "\n" + \
									 "╠ " + key + "CheckContact「On/Off」" + "\n" + \
									 "╠ " + key + "CheckPost「On/Off」" + "\n" + \
									 "╠ " + key + "CheckSticker「On/Off」" + "\n" + \
									 "╠ " + key + "UnsendChat「On/Off」" + "\n" + \
									 "╠ MyKey" + "\n" + \
									 "╠ SetKey「On/Off」" + "\n" + \
									 "╚══[ Copyright Irene BOT ]"
        return settingMessage

def adminmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
        adminMessage = 	"╔══[ Admin Command (Khusus Admin) ]" + "\n" + \
					"╠ " + key + "Restart" + "\n" + \
					"╠ " + key + "Runtime" + "\n" + \
					"╠ " + key + "Speed" + "\n" + \
					"╠ " + key + "Status" + "\n" + \
					"╠ " + key + "ChangePictureProfile" + "\n" + \
					"╠ " + key + "ChangeName:「Query」" + "\n" + \
					"╠ " + key + "ChangeBio:「Query」" + "\n" + \
					"╚══[ Copyright Irene BOT ]"
        return adminMessage
	
alquranMessage = """
「 List Al-Qur'an 」
   1. Al-Faatiha
   2. Al-Baqara
   3. Aal-i-Imraan
   4. An-Nisaa
   5. Al-Maaida
   6. Al-An'aam
   7. Al-A'raaf
   8. Al-Anfaal
   9. At-Tawba
   10. Yunus
   11. Hud
   12. Yusuf
   13. Ar-Ra'd
   14. Ibrahim
   15. Al-Hijr
   16. An-Nahl
   17. Al-Israa
   18. Al-Kahf
   19. Maryam
   20. Taa-Haa
   21. Al-Anbiyaa
   22. Al-Hajj
   23. Al-Muminoon
   24. An-Noor
   25. Al-Furqaan
   26. Ash-Shu'araa
   27. An-Naml
   28. Al-Qasas
   29. Al-Ankaboot
   30. Ar-Room
   31. Luqman
   32. As-Sajda
   33. Al-Ahzaab
   34. Saba
   35. Faatir
   36. Yaseen
   37. As-Saaffaat
   38. Saad
   39. Az-Zumar
   40. Ghafir
   41. Fussilat
   42. Ash-Shura
   43. Az-Zukhruf
   44. Ad-Dukhaan
   45. Al-Jaathiya
   46. Al-Ahqaf
   47. Muhammad
   48. Al-Fath
   49. Al-Hujuraat
   50. Qaaf
   51. Adh-Dhaariyat
   52. At-Tur
   53. An-Najm
   54. Al-Qamar
   55. Ar-Rahmaan
   56. Al-Waaqia
   57. Al-Hadid
   58. Al-Mujaadila
   59. Al-Hashr
   60. Al-Mumtahana
   61. As-Saff
   62. Al-Jumu'a
   63. Al-Munaafiqoon
   64. At-Taghaabun
   65. At-Talaaq
   66. At-Tahrim
   67. Al-Mulk
   68. Al-Qalam
   69. Al-Haaqqa
   70. Al-Ma'aarij
   71. Nooh
   72. Al-Jinn
   73. Al-Muzzammil
   74. Al-Muddaththir
   75. Al-Qiyaama
   76. Al-Insaan
   77. Al-Mursalaat
   78. An-Naba
   79. An-Naazi'aat
   80. Abasa
   81. At-Takwir
   82. Al-Infitaar
   83. Al-Mutaffifin
   84. Al-Inshiqaaq
   85. Al-Burooj
   86. At-Taariq
   87. Al-A'laa
   88. Al-Ghaashiya
   89. Al-Fajr
   90. Al-Balad
   91. Ash-Shams
   92. Al-Lail
   93. Ad-Dhuhaa
   94. Ash-Sharh
   95. At-Tin
   96. Al-Alaq
   97. Al-Qadr
   98. Al-Bayyina
   99. Az-Zalzala
   100. Al-Aadiyaat
   101. Al-Qaari'a
   102. At-Takaathur
   103. Al-Asr
   104. Al-Humaza
   105. Al-Fil
   106. Quraish
   107. Al-Maa'un
   108. Al-Kawthar
   109. Al-Kaafiroon
   110. An-Nasr
   111. Al-Masad
   112. Al-Ikhlaas
   113. Al-Falaq
   114. An-Naas
Usage: alquran num
"""

    
def memelist():
    memeList = "╔═════[ Kode Meme ]" + "\n" + \
               "╠Tenguy = 10 Guy" + "\n" + \
               "╠Afraid = Afraid to Ask Andy" + "\n" + \
               "╠Older = An Older Code Sir, But It Checks Out" + "\n" + \
               "╠Aag = Ancient Aliens Guy" + "\n" + \
               "╠Tried = At Least You Tried" + "\n" + \
               "╠Biw = Baby Insanity Wolf" + "\n" + \
               "╠Stew = Baby, You've Got a Stew Going" + "\n" + \
               "╠Blb = Bad Luck Brian" + "\n" + \
               "╠Kermit = But That's None of My Business" + "\n" + \
               "╠Bd = Butthurt Dweller" + "\n" + \
               "╠Ch = Captain Hindsight" + "\n" + \
               "╠Cbg = Comic Book Guy" + "\n" + \
               "╠Wonka = Condescending Wonka" + "\n" + \
               "╠Cb = Confession Bear" + "\n" + \
               "╠Keanu = Conspiracy Keanu" + "\n" + \
               "╠Dsm = Dating Site Murderer" + "\n" + \
               "╠Live = Do It Live!" + "\n" + \
               "╠Ants = Do You Want Ants?" + "\n" + \
               "╠Doge = Doge" + "\n" + \
               "╠Drake = Drakeposting" + "\n" + \
               "╠Ermg = Ermahgerd" + "\n" + \
               "╠Facepalm = Facepalm" + "\n" + \
               "╠Firsttry = First Try!" + "\n" + \
               "╠Fwp = First World Problems" + "\n" + \
               "╠Fa = Forever Alone" + "\n" + \
               "╠Fbf = Foul Bachelor Frog" + "\n" + \
               "╠Fmr = Fuck Me, Right?" + "\n" + \
               "╠Fry = Futurama Fry" + "\n" + \
               "╠Ggg = Good Guy Greg" + "\n" + \
               "╠Hipster = Hipster Baristaelif" + "\n" + \
               "╠Icanhas = I Can Has Cheezburger?" + "\n" + \
               "╠Crazypills = I Feel Like I'm Taking Crazy Pills " + "\n" + \
               "╠Mw = I Guarantee It" + "\n" + \
               "╠Noidea = I Have No Idea What I'm Doing" + "\n" + \
               "╠Regret = I Immediately Regret This Decision!" + "\n" + \
               "╠Boat = I Should Buy a Boat Cat" + "\n" + \
               "╠Hagrid = I Should Not Have Said That" + "\n" + \
               "╠Sohappy = I Would Be So Happy" + "\n" + \
               "╠Captain = I am the Captain Now" + "\n" + \
               "╠Bender = I'm Going to Build My Own Theme Park" + "\n" + \
               "╠Inigo = Inigo Montoya" + "\n" + \
               "╠Iw iw = Insanity Wolf" + "\n" + \
               "╠Ackbar = It's A Trap!" + "\n" + \
               "╠Happening = It's Happening" + "\n" + \
               "╠Joker = It's Simple, Kill the Batman" + "\n" + \
               "╠Ive = Jony Ive Redesigns Things" + "\n" + \
               "╠Ll = Laughing Lizard" + "\n" + \
               "╠Away = Life... Finds a Way" + "\n" + \
               "╠Morpheus = Matrix Morpheus" + "\n" + \
               "╠Mb = Member Berries" + "\n" + \
               "╠Badchoice = Milk Was a Bad Choice" + "\n" + \
               "╠Mmm = Minor Mistake Marvin" + "\n" + \
               "╠Jetpack = Nothing To Do Here" + "\n" + \
               "╠Imsorry = Oh, I'm Sorry, I Thought This Was America" + "\n" + \
               "╠Contoh: Meme Kode meme|Kata|Kata" + "\n" + \
               "╚═════════════════"
    return memeList

def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔══[ Help TextToSpeech ]" + "\n" + \
                        "╠ " + key + "af : Afrikaans" + "\n" + \
                        "╠ " + key + "sq : Albanian" + "\n" + \
                        "╠ " + key + "ar : Arabic" + "\n" + \
                        "╠ " + key + "hy : Armenian" + "\n" + \
                        "╠ " + key + "bn : Bengali" + "\n" + \
                        "╠ " + key + "ca : Catalan" + "\n" + \
                        "╠ " + key + "zh : Chinese" + "\n" + \
                        "╠ " + key + "zhcn : Chinese (Mandarin/China)" + "\n" + \
                        "╠ " + key + "zhtw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "╠ " + key + "zhyue : Chinese (Cantonese)" + "\n" + \
                        "╠ " + key + "hr : Croatian" + "\n" + \
                        "╠ " + key + "cs : Czech" + "\n" + \
                        "╠ " + key + "da : Danish" + "\n" + \
                        "╠ " + key + "nl : Dutch" + "\n" + \
                        "╠ " + key + "en : English" + "\n" + \
                        "╠ " + key + "enau : English (Australia)" + "\n" + \
                        "╠ " + key + "enuk : English (United Kingdom)" + "\n" + \
                        "╠ " + key + "enus : English (United States)" + "\n" + \
                        "╠ " + key + "eo : Esperanto" + "\n" + \
                        "╠ " + key + "fi : Finnish" + "\n" + \
                        "╠ " + key + "fr : French" + "\n" + \
                        "╠ " + key + "de : German" + "\n" + \
                        "╠ " + key + "el : Greek" + "\n" + \
                        "╠ " + key + "hi : Hindi" + "\n" + \
                        "╠ " + key + "hu : Hungarian" + "\n" + \
                        "╠ " + key + "is : Icelandic" + "\n" + \
                        "╠ " + key + "id : Indonesian" + "\n" + \
                        "╠ " + key + "it : Italian" + "\n" + \
                        "╠ " + key + "ja : Japanese" + "\n" + \
                        "╠ " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "╠ " + key + "ko : Korean" + "\n" + \
                        "╠ " + key + "la : Latin" + "\n" + \
                        "╠ " + key + "lv : Latvian" + "\n" + \
                        "╠ " + key + "mk : Macedonian" + "\n" + \
                        "╠ " + key + "no : Norwegian" + "\n" + \
                        "╠ " + key + "pl : Polish" + "\n" + \
                        "╠ " + key + "pt : Portuguese" + "\n" + \
                        "╠ " + key + "ro : Romanian" + "\n" + \
                        "╠ " + key + "ru : Russian" + "\n" + \
                        "╠ " + key + "sr : Serbian" + "\n" + \
                        "╠ " + key + "si : Sinhala" + "\n" + \
                        "╠ " + key + "sk : Slovak" + "\n" + \
                        "╠ " + key + "es : Spanish" + "\n" + \
                        "╠ " + key + "eses : Spanish (Spain)" + "\n" + \
                        "╠ " + key + "esus : Spanish (United States)" + "\n" + \
                        "╠ " + key + "sw : Swahili" + "\n" + \
                        "╠ " + key + "sv : Swedish" + "\n" + \
                        "╠ " + key + "ta : Tamil" + "\n" + \
                        "╠ " + key + "th : Thai" + "\n" + \
                        "╠ " + key + "tr : Turkish" + "\n" + \
                        "╠ " + key + "uk : Ukrainian" + "\n" + \
                        "╠ " + key + "vi : Vietnamese" + "\n" + \
                        "╠ " + key + "cy : Welsh" + "\n" + \
                        "╚══[ Copyright @Zero-Cool404 ]" + "\n" + "\n\n" + \
                        "Contoh : " + key + "say-id Zero"
    return helpTextToSpeech

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "╔══[ Help Translate ]" + "\n" + \
                    "╠ " + key + "af : afrikaans" + "\n" + \
                    "╠ " + key + "sq : albanian" + "\n" + \
                    "╠ " + key + "am : amharic" + "\n" + \
                    "╠ " + key + "ar : arabic" + "\n" + \
                    "╠ " + key + "hy : armenian" + "\n" + \
                    "╠ " + key + "az : azerbaijani" + "\n" + \
                    "╠ " + key + "eu : basque" + "\n" + \
                    "╠ " + key + "be : belarusian" + "\n" + \
                    "╠ " + key + "bn : bengali" + "\n" + \
                    "╠ " + key + "bs : bosnian" + "\n" + \
                    "╠ " + key + "bg : bulgarian" + "\n" + \
                    "╠ " + key + "ca : catalan" + "\n" + \
                    "╠ " + key + "ceb : cebuano" + "\n" + \
                    "╠ " + key + "ny : chichewa" + "\n" + \
                    "╠ " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "╠ " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "╠ " + key + "co : corsican" + "\n" + \
                    "╠ " + key + "hr : croatian" + "\n" + \
                    "╠ " + key + "cs : czech" + "\n" + \
                    "╠ " + key + "da : danish" + "\n" + \
                    "╠ " + key + "nl : dutch" + "\n" + \
                    "╠ " + key + "en : english" + "\n" + \
                    "╠ " + key + "eo : esperanto" + "\n" + \
                    "╠ " + key + "et : estonian" + "\n" + \
                    "╠ " + key + "tl : filipino" + "\n" + \
                    "╠ " + key + "fi : finnish" + "\n" + \
                    "╠ " + key + "fr : french" + "\n" + \
                    "╠ " + key + "fy : frisian" + "\n" + \
                    "╠ " + key + "gl : galician" + "\n" + \
                    "╠ " + key + "ka : georgian" + "\n" + \
                    "╠ " + key + "de : german" + "\n" + \
                    "╠ " + key + "el : greek" + "\n" + \
                    "╠ " + key + "gu : gujarati" + "\n" + \
                    "╠ " + key + "ht : haitian creole" + "\n" + \
                    "╠ " + key + "ha : hausa" + "\n" + \
                    "╠ " + key + "haw : hawaiian" + "\n" + \
                    "╠ " + key + "iw : hebrew" + "\n" + \
                    "╠ " + key + "hi : hindi" + "\n" + \
                    "╠ " + key + "hmn : hmong" + "\n" + \
                    "╠ " + key + "hu : hungarian" + "\n" + \
                    "╠ " + key + "is : icelandic" + "\n" + \
                    "╠ " + key + "ig : igbo" + "\n" + \
                    "╠ " + key + "id : indonesian" + "\n" + \
                    "╠ " + key + "ga : irish" + "\n" + \
                    "╠ " + key + "it : italian" + "\n" + \
                    "╠ " + key + "ja : japanese" + "\n" + \
                    "╠ " + key + "jw : javanese" + "\n" + \
                    "╠ " + key + "kn : kannada" + "\n" + \
                    "╠ " + key + "kk : kazakh" + "\n" + \
                    "╠ " + key + "km : khmer" + "\n" + \
                    "╠ " + key + "ko : korean" + "\n" + \
                    "╠ " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "��� " + key + "ky : kyrgyz" + "\n" + \
                    "╠ " + key + "lo : lao" + "\n" + \
                    "╠ " + key + "la : latin" + "\n" + \
                    "╠ " + key + "lv : latvian" + "\n" + \
                    "╠ " + key + "lt : lithuanian" + "\n" + \
                    "╠ " + key + "lb : luxembourgish" + "\n" + \
                    "╠ " + key + "mk : macedonian" + "\n" + \
                    "╠ " + key + "mg : malagasy" + "\n" + \
                    "╠ " + key + "ms : malay" + "\n" + \
                    "╠ " + key + "ml : malayalam" + "\n" + \
                    "╠ " + key + "mt : maltese" + "\n" + \
                    "╠ " + key + "mi : maori" + "\n" + \
                    "╠ " + key + "mr : marathi" + "\n" + \
                    "╠ " + key + "mn : mongolian" + "\n" + \
                    "╠ " + key + "my : myanmar (burmese)" + "\n" + \
                    "╠ " + key + "ne : nepali" + "\n" + \
                    "╠ " + key + "no : norwegian" + "\n" + \
                    "╠ " + key + "ps : pashto" + "\n" + \
                    "╠ " + key + "fa : persian" + "\n" + \
                    "╠ " + key + "pl : polish" + "\n" + \
                    "╠ " + key + "pt : portuguese" + "\n" + \
                    "╠ " + key + "pa : punjabi" + "\n" + \
                    "╠ " + key + "ro : romanian" + "\n" + \
                    "╠ " + key + "ru : russian" + "\n" + \
                    "╠ " + key + "sm : samoan" + "\n" + \
                    "╠ " + key + "gd : scots gaelic" + "\n" + \
                    "╠ " + key + "sr : serbian" + "\n" + \
                    "╠ " + key + "st : sesotho" + "\n" + \
                    "╠ " + key + "sn : shona" + "\n" + \
                    "╠ " + key + "sd : sindhi" + "\n" + \
                    "╠ " + key + "si : sinhala" + "\n" + \
                    "╠ " + key + "sk : slovak" + "\n" + \
                    "╠ " + key + "sl : slovenian" + "\n" + \
                    "╠ " + key + "so : somali" + "\n" + \
                    "╠ " + key + "es : spanish" + "\n" + \
                    "╠ " + key + "su : sundanese" + "\n" + \
                    "╠ " + key + "sw : swahili" + "\n" + \
                    "╠ " + key + "sv : swedish" + "\n" + \
                    "╠ " + key + "tg : tajik" + "\n" + \
                    "╠ " + key + "ta : tamil" + "\n" + \
                    "╠ " + key + "te : telugu" + "\n" + \
                    "╠ " + key + "th : thai" + "\n" + \
                    "╠ " + key + "tr : turkish" + "\n" + \
                    "╠ " + key + "uk : ukrainian" + "\n" + \
                    "╠ " + key + "ur : urdu" + "\n" + \
                    "╠ " + key + "uz : uzbek" + "\n" + \
                    "╠ " + key + "vi : vietnamese" + "\n" + \
                    "╠ " + key + "cy : welsh" + "\n" + \
                    "╠ " + key + "xh : xhosa" + "\n" + \
                    "╠ " + key + "yi : yiddish" + "\n" + \
                    "╠ " + key + "yo : yoruba" + "\n" + \
                    "╠ " + key + "zu : zulu" + "\n" + \
                    "╠ " + key + "fil : Filipino" + "\n" + \
                    "╠ " + key + "he : Hebrew" + "\n" + \
                    "╚══[ Copyright @Zero-Cool404 ]" + "\n" + "\n\n" + \
                    "Contoh : " + key + "tr-id Zero"
    return helpTranslate

def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                client.findAndAddContactsByMid(op.param1)
                sendMessage(op.param1, "Terimakasih Telah Add Irene (^_^)\n\nSupport By:\n🔰ᴿᴬFᴀᴍɪʟʏ\n✍『₮ ₭ J̶』『ᵀᴱᴬᴹᴮᴼᵀˢ』✈\n🔰ᵏᵃᵐⁱᵏᵃᶻᵉ\n✍『₮ ₭ J̶』SHOP✈\n✍Ħ₮Ƀ✈ᴛᴇᴀᴍʙᴏᴛ\n♔ tєค๓ᴿᴼᵞᴬᴸ♔\n♔ tєค๓ᴿᴼᵞᴬᴸ♔Public\nㄒ乇卂爪 丂卂几Ꮆ乇 乃ㄖㄒ\n\nCreator : http://line.me/ti/p/~syifaabyananta")

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if clientMid in op.param3:
                if settings["autoJoin"] == True:
                    client.acceptGroupInvitation(op.param1)
                    client.sendMessage(op.param1, "Terima Kasih Telah Invite Irene (^_^)\n\nSupport By:\n🔰ᴿᴬFᴀᴍɪʟʏ\n✍『₮ ₭ J̶』『ᵀᴱᴬᴹᴮᴼᵀˢ』✈\n🔰ᵏᵃᵐⁱᵏᵃᶻᵉ\n✍『₮ ₭ J̶』SHOP✈\n✍Ħ₮Ƀ✈ᴛᴇᴀᴍʙᴏᴛ\n♔ tєค๓ᴿᴼᵞᴬᴸ♔\n♔ tєค๓ᴿᴼᵞᴬᴸ♔Public\nㄒ乇卂爪 丂卂几Ꮆ乇 乃ㄖㄒ\n\nCreator : http://line.me/ti/p/~syifaabyananta")
                    
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
         
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                welcomeMessage(op.param1, [op.param2])

        if op.type in [22, 24]:
            print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                sendMention(op.param1, "@!,ngapain invite saya")
                client.leaveRoom(op.param1)

        if op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                client.sendMessage(to, str(helpMessage))
                            elif cmd == "help setting":
                                settingMessage = settingmessage()
                                client.sendMessage(to, str(settingMessage))
                            elif cmd == "help admin":
                                adminMessage = adminmessage()
                                client.sendMessage(to, str(adminMessage))
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                client.sendMessage(to, str(helpTextToSpeech))
                            elif cmd == "memelist":
                                memeList = memelist()
                                client.sendMessage(to, str(memeList))
                            elif cmd == "list alquran":
                                client.sendMessage(to, alquranMessage)
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                client.sendMessage(to, str(helpTranslate))
                            elif cmd == "sprespon":
                               if msg._from in admin:
                                   get_profile_time_start = time.time()
                                   get_profile = client.getProfile()
                                   get_profile_time = time.time() - get_profile_time_start
                                   get_group_time_start = time.time()
                                   get_group = client.getGroupIdsJoined()
                                   get_group_time = time.time() - get_group_time_start
                                   get_contact_time_start = time.time()
                                   get_contact = client.profile.mid
                                   get_contact_time = time.time() - get_contact_time_start
                                   client.sendMessage(msg.to, "Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n%.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
                            elif 'sticker:' in msg.text.lower():
                                query = msg.text.lower().replace("sticker:", "")
                                query = int(query)
                                if type(query) == int:
                                    client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png')
                                else:
                                    client.sendMessage(receiver, 'gunakan key sticker angka bukan huruf')
                            elif cmd.startswith ('invitegroupcall '):
                               if msg.toType == 2:
                                   sep = text.split(" ")
                                   strnum = text.replace(sep[0] + " ","")
                                   num = int(strnum)
                                   client.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                                   for var in range(0,num):
                                       group = client.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       client.acquireGroupCallRoute(to)
                                       client.inviteIntoGroupCall(to, contactIds=members)
                            elif cmd.startswith("meme "):
                                data = msg.text.lower().replace("meme ","")
                                meme = data.split('|')
                                meme = meme[0].replace(' ','_')
                                atas = data.split('|')
                                atas = atas[1].replace(' ','_')
                                bawah = data.split('|')
                                bawah = bawah[2].replace(' ','_')
                                memes = 'https://memegen.link/'+meme+'/'+atas+'/'+bawah+'.jpg?watermark=none'
                                client.sendImageWithURL(msg.to,memes)
                            elif text.lower().startswith("wiki "):
                                try:
                                    wiki = msg.text.lower().replace("wiki ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=3)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    client.sendMessage(msg.to, pesan)
                                except:
                                       try:
                                           pesan="Over Text Limit! Please Click link\n"
                                           pesan+=wikipedia.page(wiki).url
                                           client.sendMessage(msg.to, pesan)
                                       except Exception as error:
                                           client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("spaminvid"):
                	            dan = text.split("|")
                	            userid = dan[1]
                	            namagrup = dan[2]
                	            jumlah = int(dan[3])
                	            grups = client.groups
                	            tgb = client.findContactsByUserid(userid)
                	            client.findAndAddContactsByUserid(userid)
                	            if jumlah <= 100:
                	                for var in range(0,jumlah):
                	                  try:
                	                      client.createGroup(str(namagrup), [tgb.mid])
                	                      for i in grups:
                	                          grup = client.getGroup(i)
                	                          if grup.name == namagrup:
                	                              client.inviteIntoGroup(grup.id, [tgb.mid])
                	                              client.leaveGroup(grup.id)
                	                              sendMention(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                	                  except Exception as Nigga:
                	                      client.sendMessage(to, str(Nigga))
                            elif text.lower().startswith("alquran "):
                                try:
                                    search = msg.text.replace("alquran ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        for quran in data["data"]["ayahs"]:
                                            ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                            no+=1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        client.sendMessage(msg.to, str(ret_))
                                        client.sendAudioWithURL(msg.to, str(quran["audio"])) 
                                except Exception as error:
                                    client.sendMessage(msg.to, "error\n" + str(error))
                            elif text.lower().startswith("token"):
                                try:
                                    spl = text.lower().split('|')
                                    data = {}
                                    url = 'https://boteater.com/sniff/'
                                    if spl[1] == '1':data['nama'],data['submit1'] = spl[2],' '
                                    elif spl[1] == '2':data['nama'],data['submit2'] = spl[2],' '
                                    elif spl[1] == '3':data['nama'],data['submit3'] = spl[2],' '
                                    elif spl[1] == '4':data['nama'],data['submit4'] = spl[2],' '
                                    else:data['nama'],data['submit6'] = spl[2],' '
                                    r = requests.post(url=url, data=data)
                                    text = str(r.text).replace('INI LINK QR NYA: ', '')
                                    client.sendMessage(sender, 'Please enter link below in 2 minutes\n'+text)
                                except Exception as error:
                                    client.sendMessage(receiver, str(error))
                            elif text.lower().startswith("done"):
                                try:
                                    spl = text.lower().split('|')
                                    a = {'nama': spl[1],'submit5': ' '}
                                    url = 'https://boteater.com/sniff/'
                                    r = requests.post(url=url, data=a)
                                    text = str(r.text).replace('INI TOKENYA : ', '')
                                    client.sendMessage(sender, 'This Your Token :\n'+text)
                                    client.sendMessage(sender, 'If you done take this token, Please Logout from devices\nline://nv/connectedDevices')
                                except Exception as error:
                                    client.sendMessage(receiver, str(error))
                            elif text.lower().startswith("waktu wib"):
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.now(tz=tz)
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): blan = bulan[k-1]
                                rst = "[Auto Respond]\n" + hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                                client.sendMessage(to, rst)
                            elif text.lower().startswith("top kaskus"):
                                user = msg.text.replace("top kaskus","")
                                link = "http://apisora.herokuapp.com/kaskus/ht/?limit=20"
                                data = requests.get(link).text
                                data = json.loads(data)
                                for res_ in data['result']['Hari ini'][0:1]: 
                                    ret_ = "\nJudul : " + str(res_["title"])
                                    ret_ += "\nUrl : " + str(res_["url"])
                                    ret_ += "\nImage : " + str(res_["image"])
                                    ret_ += "\nTime Posted : " + str(res_["time_posted"])
                                    ret_ += "\nDeskripsi : " + str(res_["description"])
                                    ret_ += "\nUsername : " + str(res_["username"])
                                client.sendMessage(to, str(ret_))
                            elif text.lower().startswith("waktu wita"):
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.now(tz=tz)
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): blan = bulan[k-1]
                                rst = "[Auto Respond]\n" + hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                                client.sendMessage(to, rst)
                            elif text.lower().startswith("spam "):
                                txt = msg.text.split(" ")
                                jmlh = int(txt[2])
                                teks = msg.text.replace("spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 60:
                                        for x in range(jmlh):
                                            client.sendMessage(to, teks)
                                        else:
                                            client.sendMessage(to, "Kelebihan batas:v")
                                elif txt[1] == "off":
                                            if jmlh <= 100:
                                                client.sendMessage(to, tulisan)
                                            else:
                                                client.sendMessage(to, "Kelebihan batas :v")
                            elif text.lower().startswith("waktu wit"):
                                tz = pytz.timezone("Asia/Jayapura")
                                timeNow = datetime.now(tz=tz)
                                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                inihari = datetime.now(tz=tz)
                                hr = inihari.strftime('%A')
                                bln = inihari.strftime('%m')
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): blan = bulan[k-1]
                                rst = "[Auto Respond]\n" + hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                                client.sendMessage(to, rst)
                            elif text.lower().startswith("cari "):
                                a = msg.text.replace("cari ","")
                                b = urlshortener("http://lmgtfy.com/?q="+a, gkey)
                                client.sendMessage(to, "Result: \n\n"+b)
                            elif text.lower().startswith("balikkalimat"):
                                sep = text.split(" ")
                                sebelum = text.replace(sep[0]+" ","")
                                sesudah = sebelum[::-1]
                                client.sendMessage(to, "Sebelum : "+sebelum+"\nSesudah : "+sesudah )
                            elif text.lower().startswith("binary"):
                                sep = text.split(" ")
                                string = text.replace(sep[0]+" ","")
                                string_bytes = bytes(string, "ascii")
                                a = (' '.join(["{0:b}".format(x) for x in string_bytes]))  
                                client.sendMessage(to, str(a))
                            elif text.lower().startswith("murrotal"):
                                try:
                                    sep = text.split(" ")
                                    ayat = text.replace(sep[0] + " ","")
                                    path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                                    client.sendAudioWithURL(to, path)
                                except Exception as error:
                                    client.sendMessage(to, "error\n"+str(error))
                                    logError(error)
                            elif text.lower().startswith("ytdl "):
                                url = msg.text.replace("ytdl ","")
                                params = {"url": url}
                                r = requests.get("http://www.saveitoffline.com/process/?url="+url)
                                data = r.text
                                if data.startswith("Error: "):
                                    ret_ = msg.text.replace("Error: ","")
                                    client.sendMessage(msg.to,"[Auto Respond] error:\n" + str(ret_))
                                else:
                                    data = json.loads(data)
                                    ret_ = "[Ytdl Sukses]"
                                    try:
                                        client.sendImageWithURL(msg.to,str(data["thumbnail"]))
                                    except:
                                        pass
                                    ret_ += "\nResult for " + str(data["title"]) +"\n"
                                    i=0
                                    for res_ in data["urls"]:
                                        ret_ += "\nQuality : " + res_["label"]+"\n"
                                        ret_ += urlshortener(res_["id"], gkey)+"\n"
                                        i = i+1
                                        if i == 4:
                                           break
                                    client.sendMessage(msg.to, str(ret_))
                                    client.sendMessage(msg.to, "Proccess Mp3")
                                    client.sendAudioWithURL(msg.to, str(res_["id"]))
                                    client.sendMessage(msg.to, "Proccess Ma4")
                                    client.sendVideoWithURL(msg.to, str(res_["id"]))
                            elif text.lower().startswith("imagetext "):
                                sep = text.split(" ")
                                textnya = text.replace(sep[0] + " ","")
                                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt="+textnya+"&chts=FFFFFF,70&chf=bg,s,000000"
                                client.sendImageWithURL(msg.to, urlnya)
                            elif text.lower().startswith("quote"):
                                try:
                                    response = requests.get("https://talaikis.com/api/quotes/random/")
                                    data = response.json()
                                    author = str(data['author'])
                                    cat = str(data['cat'])
                                    quote = str(data['quote'])
                                    text = "══════「Random Quote 」════\nTipe : Quote\nPenulis : "+author+"\nKategori : " +cat+"\nKutipan : "+"\n"+quote+"\n══════════════════════"
                                    client.sendMessage(msg.to, str(text))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("1cak"):
                                try:
                                    path = 'http://api-1cak.herokuapp.com/random'
                                    r = requests.get(path)
                                    data = r.json()
                                    result = 'Title : %s\nID : %s\nUrl : %s\nVote : %s\nNfsw : %s' % (data['title'],data['id'],data['url'],data['votes'],data['nsfw'])
                                    client.sendMessage(msg.to, result)
                                    client.sendImageWithURL(msg.to, data['img'])
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    client.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    client.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd.startswith("short "):
                                url = msg.text.lower().replace("short ", '')
                                short = urlshortener(url, gkey)
                                client.sendMessage(to, short)
                            elif cmd.startswith("long "):
                                url = msg.text.lower().replace("long ", '')
                                short = urlexpander(url, gkey)
                                client.sendMessage(to, short)
                            elif cmd.startswith("qrcode "):
                                url = msg.text.lower().replace("qrcode ", '')
                                short = qrcode(url)
                                client.sendImageWithURL(msg.to, short)
                            elif text.lower() == 'bye irene':
                                client.sendMessage(to, "Byee Jangan Kangen Ya (^_^)\n\nSupport By:\n🔰ᴿᴬFᴀᴍɪʟʏ\n✍『₮ ₭ J̶』『ᵀᴱᴬᴹᴮᴼᵀˢ』✈\n🔰ᵏᵃᵐⁱᵏᵃᶻᵉ\n✍『₮ ₭ J̶』SHOP✈\n✍Ħ₮Ƀ✈ᴛᴇᴀᴍʙᴏᴛ\n♔ tєค๓ᴿᴼᵞᴬᴸ♔\n♔ tєค๓ᴿᴼᵞᴬᴸ♔Public\nㄒ乇卂爪 丂卂几Ꮆ乇 乃ㄖㄒ\n\nCreator : http://line.me/ti/p/~syifaabyananta")
                                client.leaveGroup(to)
                            elif text.lower() == 'announce':
                               if msg._from in admin:
                                   gett = client.getChatRoomAnnouncements(receiver)
                                   for a in gett:
                                       aa = client.getContact(a.creatorMid).displayName
                                       bb = a.contents
                                       cc = bb.link
                                       textt = bb.text
                                       client.sendMessage(receiver, 'Link: ' + str(cc) + '\nText: ' +str(textt) + '\nMaker: ' + str(aa))
                            elif cmd == "speed":
                               if msg._from in admin:
                                   start = time.time()
                                   client.sendMessage(to, "Proccess...")
                                   elapsed_time = time.time() - start
                                   client.sendMessage(to, "Kecepatan mengirim pesan {} detik".format(str(elapsed_time)))
                            elif cmd == "speed":
                               if msg._from in admin:
                                   client.sendMessage(to, "Proccess...")
                                   sp = int(round(time.time() *1000))
                                   client.sendMessage(receiver,"my speed : %sms" % (sp - op.createdTime))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd == "restart":
                               if msg._from in admin:
                                   client.sendMessage(to, "Berhasil merestart Bot")
                                   restartBot()
# Pembatas Script #
                            elif cmd == "autoadd on":
                               if msg._from in admin:
                                    settings["autoAdd"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                               if msg._from in admin:
                                    settings["autoAdd"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                               if msg._from in admin:
                                    settings["autoJoin"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                               if msg._from in admin:
                                    settings["autoJoin"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoleave on":
                               if msg._from in admin:
                                    settings["autoLeave"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                               if msg._from in admin:
                                    settings["autoLeave"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                               if msg._from in admin:
                                    settings["autoRespon"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "autorespon off":
                               if msg._from in admin:
                                    settings["autoRespon"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                               if msg._from in admin:
                                    settings["autoRead"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                               if msg._from in admin:
                                    settings["autoRead"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                               if msg._from in admin:
                                    settings["autoJoinTicket"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autojointicket off":
                               if msg._from in admin:
                                    settings["autoJoinTicket"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                               if msg._from in admin:
                                    settings["checkContact"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                               if msg._from in admin:
                                    settings["checkContact"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                               if msg._from in admin:
                                    settings["checkPost"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                               if msg._from in admin:
                                    settings["checkPost"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                               if msg._from in admin:
                                    settings["checkSticker"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                               if msg._from in admin:
                                    settings["checkSticker"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                                if msg._from in admin:
                                     settings["unsendMessage"] = True
                                     client.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                                if msg._from in admin:
                                     settings["unsendMessage"] = False
                                     client.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif 'Welcome ' in msg.text:
                                    spl = msg.text.replace('Welcome ','')
                                    if spl == 'on':
                                        if msg.to in welcome:
                                             msgs = "Welcome Msg sudah aktif"
                                        else:
                                            welcome.append(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                            client.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                                    if spl == 'off':
                                         if msg.to in welcome:
                                              welcome.remove(msg.to)
                                              ginfo = client.getGroup(msg.to)
                                              msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                         else:
                                              msgs = "Welcome Msg sudah tidak aktif"
                                              client.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            elif cmd == "status":
                               if msg._from in admin:
                                    try:
                                        ret_ = "╔══[ Status ]"
                                        if settings["autoAdd"] == True: ret_ += "\n╠══[ ON ] Auto Add"
                                        else: ret_ += "\n╠══[ OFF ] Auto Add"
                                        if settings["autoJoin"] == True: ret_ += "\n╠══[ ON ] Auto Join"
                                        else: ret_ += "\n╠══[ OFF ] Auto Join"
                                        if settings["autoLeave"] == True: ret_ += "\n╠══[ ON ] Auto Leave Room"
                                        else: ret_ += "\n╠══[ OFF ] Auto Leave Room"
                                        if settings["autoJoinTicket"] == True: ret_ += "\n╠══[ ON ] Auto Join Ticket"
                                        else: ret_ += "\n╠══[ OFF ] Auto Join Ticket"
                                        if settings["autoRead"] == True: ret_ += "\n╠══[ ON ] Auto Read"
                                        else: ret_ += "\n╠══[ OFF ] Auto Read"
                                        if settings["autoRespon"] == True: ret_ += "\n╠══[ ON ] Detect Mention"
                                        else: ret_ += "\n╠══[ OFF ] Detect Mention"
                                        if settings["checkContact"] == True: ret_ += "\n╠══[ ON ] Check Contact"
                                        else: ret_ += "\n╠══[ OFF ] Check Contact"
                                        if settings["checkPost"] == True: ret_ += "\n╠══[ ON ] Check Post"
                                        else: ret_ += "\n╠══[ OFF ] Check Post"
                                        if settings["checkSticker"] == True: ret_ += "\n╠══[ ON ] Check Sticker"
                                        else: ret_ += "\n╠══[ OFF ] Check Sticker"
                                        if settings["setKey"] == True: ret_ += "\n╠══[ ON ] Set Key"
                                        else: ret_ += "\n╠══[ OFF ] Set Key"
                                        if settings["unsendMessage"] == True: ret_ += "\n╠══[ ON ] Unsend Message"
                                        else: ret_ += "\n╠══[ OFF ] Unsend Message"
                                        ret_ += "\n╚══[ Status ]"
                                        client.sendMessage(to, str(ret_))
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crash":
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd.startswith("changename:"):
                               if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                               if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd == "respon":
                                sendMention(to, "@!", [sender])
                                client.sendContact(to, sender)
                            elif cmd == "me":
                            	sendMention(to, "@!", [sender])
                            	client.sendContact(to, sender)
                            	contact = client.getContact(sender)
                            	textx = "[ PROFILE ]\n{}".format(contact.displayName)
                            	client.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~mamanggd','AGENT_ICON': "http://dl.profile.line-cdn.net/" + contact.pictureStatus})
                            elif cmd == "mymid":
                                client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = client.getProfileCoverURL(sender)          
                                path = str(channel)
                                client.sendImageWithURL(to, path)
                            elif cmd == "sider on":
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                                wait["Sider"] = True
                                client.sendMessage(msg.to,"Sider On")

                            elif cmd == "sider off":
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    wait["Sider"] = False
                                    client.sendMessage(msg.to, "Sider Off")
                                else:
                                    client.sendMessage(msg.to, "Set dulu bang")
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == 'groupcreator':
                                group = client.getGroup(to)
                                GS = group.creator.mid
                                client.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔══[ Group Info ]"
                                ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                                ret_ += "\n╠ ID Group : {}".format(group.id)
                                ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n╠ Group Qr : {}".format(gQr)
                                ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupmemberlist':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    client.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif cmd == "changepictureprofile":
                               if msg._from in admin:
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == 'mention':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//100
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*100 : (a+1)*100]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(to, "Total {} Mention".format(str(len(nama))))  
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    client.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    client.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[R E A D E R ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking belum diaktifkan")

# Pembatas Script #   
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "╔══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                    ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠ " + data[1]
                                    ret_ += "\n╠ " + data[2]
                                    ret_ += "\n╠ " + data[3]
                                    ret_ += "\n╠ " + data[4]
                                    ret_ += "\n╠ " + data[5]
                                    ret_ += "\n╚══[ Success ]"
                                    client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔══[ Weather Status ]"
                                        ret_ += "\n╠ Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                        ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n╠ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n╠══[ Time Status ]"
                                        ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += "\n╚══[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔══[ Location Status ]"
                                        ret_ += "\n╠ Location : " + data[0]
                                        ret_ += "\n╠ Google Maps : " + link
                                        ret_ += "\n╚══[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        client.sendImageWithURL(to, str(path))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    client.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    client.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return alin.sendMessage(to, "Language not found")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        client.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══[ Music ]"
                                            ret_ += "\n╠ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠ Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚══[ Finish ]"
                                            client.sendImageWithURL(to, str(data["result"]["img"]))
                                            client.sendMessage(to, str(ret_))
                                            client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Lyric ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        client.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ Youtube Result ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                    ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ Total {} ]".format(len(datas))
                                client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return alin.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                client.sendMessage(to, str(A))
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykey":
                            if msg._from in admin:
                                 client.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "setkey on":
                            if msg._from in admin:
                                settings["setKey"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan setkey")
                        elif text.lower() == "setkey off":
                            if msg._from in admin:
                                settings["setKey"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan setkey")
# Pembatas Script #
                    elif msg.contentType == 1:
                       if msg._from in admin:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendMessage(to, "Berhasil mengubah foto group")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if text in ["Crash","crash"]:
                        dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash","Kamu asungecrash terus!")
                        ket = random.choice(dia)
                        client.sendMessage(to,ket)
                        client.kickoutFromGroup(msg.to,[sender])
                        client.sendMessage(to,"Mampus!")
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, "Oi Asw @!,jangan main tag tag", [sender])
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = client.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "Send Message cancelled."
                                ret_ += "\nSender : @!"
                                ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            client.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
	
              
        if op.type == 55:
            print ("[ 55 ] NOTIFIED CEK SIDER")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
                if op.param1 in cctv['cyduk']:
                    if op.param1 in cctv['point']:
                        Name=client.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n= "+Name
                            if " " in Name:
                                nick = Name.split('')
                                if len(nick)==2:
                                    sendMention(op.param1, "@! kang sider datang",[op.param2])
                                else:
                                    sendMention(op.param1, "@! cie sider moga jadian",[op.param2])
                            else:
                                sendMention(op.param1, "@! telah membaca",[op.param2])
                    else:
                       pass
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
