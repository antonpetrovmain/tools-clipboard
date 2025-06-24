import pyperclip
import threading
import time
import colorama
from colorama import Fore, Style

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]

def display_entries(history):
    print("\033[2J\033[H", end='')  # Clear screen and move to top-left
    if not history:
        print("No entries in clipboard history.")
    else:
        for i, entry in enumerate(history):
            reversed_index = len(history) - 1 - i
            color = COLORS[reversed_index % len(COLORS)]
            preview = entry
            line = f"{color}{reversed_index}: {preview}{Style.RESET_ALL}"
            print(line, end='')

def monitor_clipboard(history, redraw_event):
    previous_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            # Remove older entries with the same content before adding the new one
            history[:] = [entry for entry in history if entry != current_clipboard]
            history.append(current_clipboard)
            redraw_event.set()
            previous_clipboard = current_clipboard
        time.sleep(0.2)

def main():
    colorama.init()
    history = []
    redraw_event = threading.Event()

    clipboard_thread = threading.Thread(target=monitor_clipboard, args=(history, redraw_event), daemon=True)
    clipboard_thread.start()

import sys
import select

def main():
    colorama.init()
    history = []
    redraw_event = threading.Event()

    clipboard_thread = threading.Thread(target=monitor_clipboard, args=(history, redraw_event), daemon=True)
    clipboard_thread.start()

    while True:
        # Check for input with timeout (0.1s) to allow frequent redraw checks
        if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
            choice = input().strip()
            if choice.isdigit():
                idx = int(choice)
                if 0 <= idx < len(history):
                    original_index = len(history) - 1 - idx
                    pyperclip.copy(history[original_index])
                    print(f"Entry {idx} copied to clipboard.")
                else:
                    print("Invalid entry number.")
            elif choice == "":
                pass  # Allow execution to continue and redraw the screen
            else:
                print("Invalid input. Please enter a number.")

        # Always check for redraw event
        if redraw_event.is_set():
            display_entries(history)
            redraw_event.clear()

        # Optional: Add a small sleep to reduce CPU usage
        time.sleep(0.1)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
