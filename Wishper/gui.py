import tkinter as tk
import json

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def toggle_option(option, button, config):
    config[option] = not config[option]
    button.config(bg="green" if config[option] else "red")
    save_config(config)

def build_gui():
    config = load_config()
    root = tk.Tk()
    root.title("WHISPER Feature Control")
    root.geometry("350x300")
    root.config(bg="#222222")

    options = {
        "auto_delete": "Auto Delete after 5min",
        "file_transfer": "File Transfer",
        "dark_mode": "Dark Mode",
        "auto_response": "Auto Response",
        "secret_mode": "SECRET Mode"
    }

    for i, (key, label) in enumerate(options.items()):
        btn = tk.Button(root,
                        text=label,
                        width=25,
                        bg="green" if config[key] else "red",
                        fg="white",
                        font=("Arial", 10, "bold"),
                        command=lambda k=key, b=None: toggle_option(k, b, config))
        btn.grid(row=i, column=0, padx=20, pady=8)
        # Fix button reference
        btn.config(command=lambda k=key, b=btn: toggle_option(k, b, config))

    root.mainloop()

if __name__ == "__main__":
    build_gui()