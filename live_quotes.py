import tkinter as tk
import random
import requests
import threading
import ctypes  # ← NEW

# ========== WORKING APIS ==========
# ========== NEW CLEAN API ==========
def get_quote_from_zenquotes():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()[0]
            text = data["q"]
            author = data["a"]

            # Filter unwanted words (extra safety)
            banned_words = ["porn", "shit", "fuck", "suicide"]
            if any(word in text.lower() for word in banned_words):
                return None

            return {
                "text": text,
                "author": author,
                "online": True
            }
    except:
        pass
    return None

# ========== SETTINGS ==========
WIDTH = 400
HEIGHT = 110
OFFSET_RIGHT = 7
OFFSET_BOTTOM = 30
TRANSPARENCY = 0.92
QUOTE_SIZE = 13
AUTHOR_SIZE = 10

# ========== CREATE WINDOW ==========
root = tk.Tk()
root.title("")
root.attributes('-alpha', TRANSPARENCY)
root.attributes('-topmost', False)
root.overrideredirect(True)
root.configure(bg='black')
root.wm_attributes('-transparentcolor', 'black')

# Position
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - WIDTH - OFFSET_RIGHT
y = screen_height - HEIGHT - OFFSET_BOTTOM
root.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

# ========== HIDE FROM TASKBAR (NEW) ==========
def hide_from_taskbar():
    try:
        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        # WS_EX_TOOLWINDOW = 0x00000080
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, 
            ctypes.windll.user32.GetWindowLongW(hwnd, -20) | 0x00000080)
    except:
        pass

root.after(100, hide_from_taskbar)  # Hide after window is created

# ========== UI ==========
main = tk.Frame(root, bg='black')
main.pack(fill='both', expand=True)

quote_label = tk.Label(
    main,
    text="Loading...",
    font=("Caveat", 18),
    fg="white",
    bg='black',
    wraplength=WIDTH - 20,
    justify='right',
    anchor='e'
)
quote_label.pack(expand=True, pady=(8, 0))

author_label = tk.Label(
    main,
    text="",
    font=("Caveat", 13, "italic"),
    fg="#CCCCCC",
    bg='black',
    justify='right',
    anchor='e'
)
author_label.pack(pady=(0, 8))

# Status
status_label = tk.Label(
    main,
    text="🟢 LIVE",
    font=("Segoe UI", 7),
    fg="#00FF00",
    bg='black'
)
status_label.place(relx=1.0, rely=1.0, x=-5, y=-5)

# ========== FETCH QUOTE FUNCTION ==========
def fetch_new_quote():
    quote = get_quote_from_zenquotes()
    if quote:
        return quote

    # Clean motivational + funny fallback quotes
    fallbacks = [
        {"text": "Do something today that your future self will thank you for.", "author": "Unknown"},
        {"text": "Dream big. Start small. Act now.", "author": "Robin Sharma"},
        {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
        {"text": "I’m not lazy, I’m on energy-saving mode.", "author": "Unknown"},
        {"text": "Why fall in love when you can fall asleep?", "author": "Unknown"},
        {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
        {"text": "If at first you don’t succeed, then skydiving definitely isn’t for you.", "author": "Steven Wright"},
        {"text": "Stay hungry. Stay foolish.", "author": "Steve Jobs"},
        {"text": "Work hard in silence, let success make the noise.", "author": "Unknown"},
    ]

    fallback = random.choice(fallbacks)
    fallback["online"] = False
    return fallback

# ========== UPDATE DISPLAY ==========
def update_quote():
    """Background thread to fetch and update"""
    
    def fetch_and_update():
        quote = fetch_new_quote()
        
        # Update UI in main thread
        root.after(0, lambda: display_quote(quote))
    
    # Run fetch in background
    thread = threading.Thread(target=fetch_and_update)
    thread.daemon = True
    thread.start()

def display_quote(quote):
    """Update the labels with new quote"""
    quote_label.config(text=f'"{quote["text"]}"')
    author_label.config(text=f"— {quote['author']}")
    
    # Update status
    if quote.get("online", True):
        status_label.config(text="🟢 LIVE", fg="#00FF00")
    else:
        status_label.config(text="🔴 OFFLINE", fg="#FF0000")
    
    # Schedule next update (10-15 seconds)
    next_update = random.randint(30000, 35000)
    root.after(next_update, update_quote)

def keep_behind():
    root.lower()
    root.after(2000, keep_behind)

def exit_app(event):
    root.quit()

# ========== START ==========
root.bind('<Escape>', exit_app)

print("✨ LIVE QUOTES RUNNING")
print("📍 Bottom Right (Hidden from taskbar)")
print("🌐 Getting fresh quotes every 10-15 seconds")
print("🖱️  Press ESC to exit")

# Start
update_quote()
root.after(2000, keep_behind)

root.mainloop()