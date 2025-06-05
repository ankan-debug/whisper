# 🔒 WHISPER: Offline Secure Chat App

WHISPER is a minimalist Python-based offline chat tool that works across PC and mobile using Termux. You can chat securely using LAN, Wi-Fi hotspot, Bluetooth, or USB — even without internet!


### 💡 Features

- 🗨️ Real-time chat between devices
- 🛡️ Optional cipher-based secret mode (substitution cipher)
- ⏲️ Auto-delete messages after 5 mins (toggleable)
- 🌒 Light/Dark terminal mode
- 📁 File transfer support (toggleable)
- 🤖 Auto response (toggleable)
- 🔐 Chat lock with PIN
- 🖼️ Emoji support
- 📱 Works on Termux and PC

### 🧑‍💻 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/ankan-debug/whisper
cd whisper
````

### 2. Run Server on Receiver Device

```bash
python server.py
```

### 3. Run Client on Sender Device

```bash
python client.py
```

### 4. Optional: Toggle Config

Edit `config.json` to enable/disable features.

---

## 📦 Requirements

* Python 3.8+
* Works on Windows/Linux/Mac
* Termux for Android support

---

## 🔐 Secret Mode

WHISPER uses a basic custom substitution cipher.
To enable it:

```json
"secret_mode": true
```

---

## 📂 File Structure

```
whisper/
├── client.py
├── server.py
├── cipher.py
├── utils.py
├── config.json
└── README.md
```

---

## 🧪 Future Add-ons

* GUI for toggles (Tkinter or CLI-based switch)
* QR-based peer connection
* Custom emoji packs
* Bluetooth/USB mode setup scripts

---

## ✨ Made with ❤️ by Ankan

```
📧 sahaankan628@gmail.com

