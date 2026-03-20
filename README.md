# 🔐 WiFi Password Manager
  
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

A simple **Python CLI tool** to list, show, and save WiFi passwords on your system. Perfect for quick recovery of saved WiFi credentials. 💻✨

---

## 🚀 Features

- List all saved WiFi profiles 📝  
- Show password for a specific WiFi 🔑  
- Fetch all passwords with multi-threading ⚡  
- Save passwords to a text file 📂  
- Thread-safe and error-resistant 🛡️  
- Easy to extend for JSON/CSV export 📊  

---

## 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/Mahdi-Haqiqat/Wifi-Password-Manager.git
cd Wifi-Password-Manager
```

2. Install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

### List all WiFi profiles

```bash
python main.py --list
```

### Show password for a specific WiFi

```bash
python main.py --show "YourWiFiName"
```

### Show all passwords

```bash
python main.py --all
```

### Save passwords to file

```bash
python main.py --all --save
```

> Output file: wifi_passwords.txt 📄

---

## 🔧 Notes

- Works on systems where Python can access saved WiFi credentials.  
- Multi-threaded for faster retrieval.  
- Handles errors gracefully – failed passwords will appear as None.  

---

## ⚠️ Disclaimer

This tool is intended **for educational purposes and personal use only**.  
Do **not use this software to access networks you do not own or have explicit permission to test**.  
The author is **not responsible for any misuse** of this tool.  

Always respect local laws and regulations regarding computer networks and cybersecurity.  
By using this tool, you agree to use it responsibly and legally.  

---

## ❤️ Contributing

Feel free to open issues, submit PRs, or suggest improvements!  
This project is open-source under the MIT License.  

---

## 📝 License

This project is licensed under the [MIT License](https://github.com/Mahdi-Haqiqat/Wifi-Password-Manager/blob/main/LICENSE).

---

Made with ❤️ and Python 🐍
