# File-sharing-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://t.me/CodeXBotz">
    <img src="https://github.com/CodeXBotz/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://t.me/CodeXBotz">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://t.me/codexbotzsupport">
    &nbsp;<img src="https://img.shields.io/badge/Code%20%F0%9D%95%8F%20Botz-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/CodeXBotz/File-Sharing-Bot?style=social">
  </a>
  <a href="https://github.com/CodeXBotz/File-Sharing-Bot/fork">
    <img src="https://img.shields.io/github/forks/CodeXBotz/File-Sharing-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot to store Posts and Documents and it can Access by Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

##

**If you need any more modes in repo or If you find out any bugs, mention in [@codexbotzsupport ](https://www.telegram.dog/codexbotzsupport)**

**Make sure to see [contributing.md](https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/CONTRIBUTING.md) for instructions on contributing to the project!**



### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
**BEFORE YOU DEPLOY ON HEROKU, YOU SHOULD FORK THE REPO AND CHANGE ITS NAME TO ANYTHING ELSE**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>
<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>
**Check This Tutorial Video on YouTube for any Help**<br>
**Thanks to [Erich](https://t.me/ErichDaniken) and his [InFoTel](https://t.me/InFoTel_Group) for this Video**

#### Deploy on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

#### Deploy on Koyeb

The fastest way to deploy the application is to click the **Deploy to Koyeb** button below.


[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/CodeXBotz/File-Sharing-Bot&branch=koyeb&name=filesharingbot)


#### Deploy di VPS
````bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users

/stats - checking your bot uptime

/uptime - cek uptime bot
```

### Variabel

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DATABASE_URL` Your mongo db url
* `DATABASE_NAME` Your mongo db session name
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional: Pesan Force sub dari bot, gunakan HTML & <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a>
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, tinggalkan 0 jika Anda ingin menonaktifkan force sub
* `PROTECT_CONTENT` Optional: "True" jika Anda perlu mencegah penerusan file

### Variabel Tambahan

* `CUSTOM_CAPTION` letakkan teks Teks khusus Anda jika Anda ingin Pengaturan Teks Khusus, Anda dapat menggunakan HTML dan <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Letakkan "True" untuk Nonaktifkan Tombol Berbagi Saluran, Default "False'
* `BOT_STATS_TEXT` letakkan teks khusus Anda untuk perintah statistik, gunakan HTML dan <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a>
* `USER_REPLY_TEXT` letakkan teks Anda untuk ditampilkan saat pengguna mengirim pesan apa pun, gunakan HTML


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - Nama awal pengguna
* `{last}` - Nama akhir pengguna
* `{id}` - ID pengguna
* `{mention}` - tag pengguna
* `{username}` - Username

#### EDIT_JUDUL

* `{filename}` - Nama dari dokumen
* `{previouscaption}` - Original Caption

#### EDIT_STATISTIK

* `{uptime}` - Cek Bot Uptime


### Support   
- DONASI UNTUK ADMIN [SAWERIA](https://saweria.co/msdzulqurnain) 😉
- Join [Telegram Group](https://t.me/MS_DZULQURNAIN_NET) Untuk support 
- dan join [Channel](https://t.me/sukamamamuuuu) Asupan 18+ 

### Credits
- [GITHUB](https://github.com) 
- Terima kasih kehebatannya [Libary](https://github.com/pyrogram/pyrogram)
- [CodeXBotz](https://github.com/CodeXBotz) 
- Seluruh support member grup

### FILE SHARING BOT TELEGRAM
Reedit by [MS-DZULQURNAIN](https://github.com/MS-DZULQURNAIN)
