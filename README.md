### _Ambient Desktop Widget for Focus & Flow_

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/API-ZenQuotes-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

<p align="center">
  A minimal, always-on desktop widget that delivers real-time quotes —  
  designed to <b>blend into your workflow</b>, not interrupt it.
</p>

---

## ⚡ What is this?

**Live Quotes** is a lightweight desktop widget that sits quietly in the corner of your screen and refreshes quotes every few seconds.

No popups.  
No distractions.  
Just clean, ambient motivation while you work.

---

## 🎯 Why it stands out

Most apps compete for attention.

This one **stays out of your way**.

- No UI clutter  
- No notifications  
- No interaction needed  

It simply exists — like background music, but for your mind.

---

## ✨ Features

✔ **Live Quote Streaming**  
Fetches fresh quotes from ZenQuotes API  

✔ **Offline Fallback System**  
Works even without internet  

✔ **Always-on Ambient Mode**  
Visible but never intrusive  

✔ **Ultra Lightweight**  
Runs silently with minimal resources  

✔ **Stealth Mode**  
No taskbar presence, no distractions  

✔ **Auto Refresh Engine**  
New quote every 10–15 seconds  

✔ **Minimal Aesthetic UI**  
Clean black + subtle typography  

✔ **Instant Exit**  
Press `ESC` anytime  

---

## 📸 Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/0e1eab27-c616-4052-a255-83c66ab1667c" width="45%">
  <img src="https://github.com/user-attachments/assets/746dea60-d566-4869-8e36-0fb21a1efbf2" width="45%">
</p>

📍 Bottom-right corner  
👁 Always visible  
🧘 Never distracting 

---

## 🚀 Installation

### 1. Clone the repo
```bash
git clone https://github.com/laxdip/live-quotes.git
cd live-quotes
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the widget
```bash
python app.py
```

---

## ⚡ Quick Launch Options

### Option 1 — Manual (Python)

```bash
python app.py
```

---

### Option 2 — One-Click Launch (.bat file)

Simply double-click:

```
start_quotes.bat
```

This will automatically launch the widget.

---

## 📄 What does the `.bat` file do?

The `start_quotes.bat` file is a simple Windows script that runs your app.

### Example:

```bat
@echo off
cd /d %~dp0
python app.py
pause
```

### Explanation:

- `@echo off` → hides command output noise  
- `cd /d %~dp0` → navigates to project folder automatically  
- `python app.py` → runs the application  
- `pause` → keeps window open (useful for debugging)

---

## 💡 Why use the .bat file?

- One-click launch  
- No need to open terminal  
- Beginner-friendly  
- Can be added to startup for auto-run  

---

## ⚙️ Run on Startup (Windows)

1. Press `Win + R`  
2. Type:
   ```
   shell:startup
   ```
3. Paste `start_quotes.bat` inside  

Now the widget starts automatically on boot 🚀

---

## 🧠 Tech Stack

- **Python** — Core logic  
- **Tkinter** — GUI  
- **ZenQuotes API** — Quote source  

---

## 🧪 How it works

1. Fetches quote from API  
2. Displays it in floating window  
3. Falls back to local quotes if offline  
4. Refreshes automatically  

Runs continuously in the background.

---

## 🔮 Future Enhancements

- 🎛 Custom themes (dark / glass / neon)
- 📍 Draggable widget position
- 🧠 Smart quote categories (dev / mindset / humor)
- 💾 Local quote database expansion
- ⌨️ Custom hotkeys
- 🌈 Smooth animations & transitions

---

## 🧑‍💻 Philosophy

> _Build tools that don’t demand attention —  
but improve focus silently._

---

## 🤝 Contributing

Pull requests are welcome.

If you have ideas to improve UI, performance, or features — feel free to contribute.

---

## ⭐ Support

If you like this project:

- ⭐ Star the repo  
- 🔁 Share it  
- 🛠 Build something on top of it  

---

## ⚡ Final Note

This is not just a widget.

It’s a **tiny system running beside your work —  
keeping your mind slightly sharper, every few seconds.**
