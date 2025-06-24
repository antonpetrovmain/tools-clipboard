# Clipboard Manager

A terminal-based clipboard history manager that tracks clipboard entries in real-time, removes duplicates (keeping only the newest), and allows interactive selection of past entries.

## 🧠 Features

- ✅ **Real-time clipboard monitoring**
  Detects and stores new clipboard content every 0.2 seconds.

- 🚫 **Duplicate removal**
  Automatically removes older entries with the same content as newer ones.

- 🖱️ **Interactive selection interface**
  View and select clipboard history entries directly in the terminal.

- 🔄 **Auto-refresh display**
  Screen updates automatically when new entries appear or after user actions.

## 📦 Installation

1. Ensure Python 3 is installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

1. Run the program:

```bash
python clipboard_manager.py
```

2. **Interact with the interface:**
   - A list of clipboard entries appears in reverse chronological order (newest at the bottom).
   - Each entry is color-coded for easy identification.
   - Enter a number to copy an entry back to your clipboard.
   - Press **Enter** to refresh the display without copying anything.

3. Exit by pressing `Ctrl+C`.

## 📝 Notes

- The clipboard history is stored in memory only. Restarting the program will clear it.
- Requires `pyperclip` for clipboard access and `colorama` for terminal colors.
- On Linux, the test script (`test.sh`) uses `xsel`. Install it with:
  ```bash
  sudo apt install xsel
  ```
- Tested on Linux/macOS. On Windows, ensure Python has clipboard access.

## 🧩 Dependencies

```txt
colorama==0.4.6
pyperclip==1.8.2
```

(Defined in `requirements.txt`.)

## 🧪 Testing

Run the test script to simulate clipboard changes:

```bash
./test.sh
```

This will add "foo", "bar", and "zab" to the clipboard history for testing.

## 📁 File Structure

```
.
├── clipboard_manager.py      # Main program
├── requirements.txt          # Python dependencies
├── test.sh                   # Test script (uses xsel)
├── .gitignore                # Git ignore rules
└── README.md                 # This file (you're here!)
```
