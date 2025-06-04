

## Whisper 🚀

**Whisper** is a lightweight, terminal-based offline secure chat tool designed for PC and mobile (via Termux), enabling private communication over LAN, USB, Bluetooth, or phone hotspots — *no internet needed*. Perfect for security-conscious users who want fast, reliable, and encrypted messaging anywhere, anytime.

---

## Features ✨

* **Offline chat** via LAN (WiFi), USB tethering, Bluetooth, or phone hotspot
* **End-to-end encryption** with a custom substitution cipher (SECRET mode)
* **Emoji support** for expressive conversations
* **Auto-delete messages** after 5 minutes (optional toggle)
* **File transfer** over offline connections
* **Dark/Light UI modes** for comfortable chatting
* **Auto-response bot** (optional)
* **Chat lock** for privacy protection
* **Typing indicator** (optional, coming soon)

---

## How It Works ⚙️

Whisper runs entirely in your terminal on PC or mobile. Connect your devices via a shared LAN, USB, Bluetooth, or hotspot network — no internet required. Run the server script on one device, and the client script on the other. Enjoy secure, encrypted chatting in real-time with zero dependency on online services.

---

## Installation 💻

1. Clone the repository:

   ```bash
   git clone https://github.com/ankan-debug/whisper.git  
   cd whisper  
   ```

2. (Optional) Create a Python virtual environment:

   ```bash
   python -m venv venv  
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`  
   ```

3. Install requirements (if any, add later when you have external libs):

   ```bash
   pip install -r requirements.txt  
   ```

---

## Usage 🚀

* **Start the server:**

  ```bash
  python server.py  
  ```

* **Start the client:**

  ```bash
  python client.py  
  ```

Follow on-screen prompts to connect devices and chat securely offline.

---

## Configuration ⚙️

Toggle features via `config.json`:

* `auto_delete`: Enable/disable auto-delete messages
* `file_transfer`: Enable/disable file transfer
* `dark_mode`: Enable/disable dark mode UI
* `auto_response`: Enable/disable auto chatbot replies
* `secret_mode`: Enable/disable encryption (substitution cipher)

---

## Contributions 🤝

Whisper is an open-source project. Contributions, suggestions, and bug reports are welcome! Feel free to fork, improve, and submit PRs.

---

## License 📄

Distributed under the MIT License. See `LICENSE` for details.

---

## Contact ✉️

Created by Ankan Saha — Cybersecurity Enthusiast & Developer
GitHub: [ankan-debug](https://github.com/ankan-debug)

Email: sahaankan628@gmail.com

---

## ✨ Made with ❤️ by Ankan


