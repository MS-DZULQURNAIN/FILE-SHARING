# File-sharing-Bot

<p align="center">
  <a href="https://youtube.com/@msdzulqurnain5914">
    &nbsp;<img src="https://img.shields.io/badge/MS%20DZULQURNAIN-ff0000?style=flat-square&logo=youtube" width="250" height="40">&nbsp;
  </a><br>
  <a href="https://instagram.com/ms_dzulqurnain09?igshid=YmMyMTA2M2Y=">
    &nbsp;<img src="https://img.shields.io/badge/MS%20DZULQURNAIN-pink?style=flat-square&logo=instagram" width="250" height="40">&nbsp;
  </a><br>
  <a href="https://www.tiktok.com/@ms_dzulqurnain?_r=1&_d=e1ii1ll6jkblmk&language=id&sec_uid=MS4wLjABAAAAvteD7eBGyERB-w3bg4q5Y8fMdJfzrbbo2QpjVtQpDAYqJIxg7y9EKCkNND6N4q9I&share_author_id=6823405357177701378&source=h5_t&u_code=dc881ih0565j7b&timestamp=1673701948&user_id=6823405357177701378&sec_user_id=MS4wLjABAAAAvteD7eBGyERB-w3bg4q5Y8fMdJfzrbbo2QpjVtQpDAYqJIxg7y9EKCkNND6N4q9I&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_iid=7184522025100560134&share_link_id=8c044b07-7b52-476e-bc51-04adacb47e52&share_app_id=1180&ugbiz_name=Account&ug_btm=b8727%2Cb4907">
    &nbsp;<img src="https://img.shields.io/badge/MS%20DZULQURNAIN-black?style=flat-square&logo=tiktok" width="250" height="40">&nbsp;
  </a><br>
  <a href="https://t.me/ms_dzulqurnain">
    &nbsp;<img src="https://img.shields.io/badge/MS%20DZULQURNAIN-blue?style=flat-square&logo=telegram" width="250" height="40">&nbsp;
  </a><br>
 - MY TELEGRAM GROUP -
  <a href="https://t.me/MS_DZULQURNAIN_NET">
    &nbsp;<img src="https://img.shields.io/badge/MS DZULQURNAIN NET-blue?logo=telegram" width="200" height="35">&nbsp;
  </a><br>
  <a href="https://t.me/ZULLL_CHIP">
    &nbsp;<img src="https://img.shields.io/badge/ZULLL CHIP-blue?logo=telegram" width="200" height="35">&nbsp;
  </a><br>
</p>


### FITUR"
- DAPAT DI SESUAIKAN SEPENUHNYA.
- BISA EDIT PESAN SELAMAT DATANG & PESAN FORCE SUB.
- DAPAT MEMPOSTING BEBERAPA FILE DI DALAM 1 LINK. 
- DAPAT DIGUNAKAN DI HEROKU SECARA LANGSUNG. 

### PENGATURAN AGAR BOT HIDUP
- TAMBAHKAN BOT KE CHANNEL DATABASE & JADIKAN ADMIN
- TAMBAHKAN BOT KE CH/GC FORCE SUB & JADIKAN ADMIN (JIKA MEMAKAI FORCE SUB) 
##
### Installation
#### DEPLOY DI HEROKU
**SEBELUM DEPLOY DI HEROKU, ANDA HARUS "FORK" REPO INI DAN MENGUBAH NAMANYA MENJADI APA SAJA**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>

#### DEPLOY DI RAILWAY
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

#### DEPLOY DI KOYEB

Cara tercepat untuk deploy aplikasi adalah dengan mengklik **Deploy to Koyeb** tombol dibawah.


[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/MS-DZULQURNAIN/FILE-SHARING&branch=koyeb&name=filesharingbot)


#### Deploy di VPS
````bash
git clone https://github.com/MS-DZULQURNAIN/FILE-SHARING
cd FILE-SHARING
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### PERINTAH ADMIN 

```
/start - start bot

/batch - buat link lebih dari 1 file

/genlink - buat link untuk 1 postingan

/users - cek jumlah pengguna

/broadcast - pesan broadcast untuk semua pengguna bot

/stats - checking your bot uptime

/uptime - cek uptime bot
```

### VARIABEL

* `API_HASH` API HASH dari [my.telegram.org](my.telegram.org) 
* `APP_ID` APP ID dari [my.telegram.org](my.telegram.org) 
* `TG_BOT_TOKEN` TOKEN bot Anda dari [@BotFather](https://t.me/BotFather) 
* `OWNER_ID` Harus memasukkan Id Telegram Anda
* `CHANNEL_ID` Channel ID Anda contoh:- -100xxxxxxxx
* `DATABASE_URL` URL MONGO DB Anda
* `DATABASE_NAME` Nama session MONGO DB Anda
* `ADMINS` Optional: Daftar username dari admins, hanya mereka yg dapat membuat link
* `START_MESSAGE` Optional: Pesan start dari bot, gunakan HTML and <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional: Pesan Force sub dari bot, gunakan HTML & <a href='https://github.com/MS-DZULQURNAIN/FILE-SHARING/blob/main/README.md#fillings'>fillings</a>
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, tinggalkan 0 jika Anda ingin menonaktifkan force sub
* `PROTECT_CONTENT` Optional: "True" jika Anda perlu mencegah penerusan file

### VARIABEL TAMBAHAN "OPSIONAL"

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
- dan join [Channel](https://t.me/MS_DZULQURNAIN_NET) untuk info selanjutnya

### Credits
- [GITHUB](https://github.com) 
- Terima kasih kehebatannya [Libary](https://github.com/pyrogram/pyrogram)
- [CodeXBotz](https://github.com/CodeXBotz) 
- Seluruh support member grup

### FILE SHARING BOT TELEGRAM
Reedit by [MS-DZULQURNAIN](https://github.com/MS-DZULQURNAIN)
