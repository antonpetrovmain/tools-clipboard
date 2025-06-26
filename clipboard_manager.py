import pyperclip
import threading
import time
import colorama
import sys
import select
from colorama import Fore, Style

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]

def display_entries(history, filter_str=""):
    print('\033[2J\033[H', end='')  # Clear screen and reset cursor
    filtered = []
    for idx, entry in enumerate(history):
        if not filter_str or filter_str.lower() in entry.lower():
            filtered.append((idx, entry))
    for i, (original_idx, entry) in enumerate(filtered):
        color = COLORS[i % len(COLORS)]
        displayed_index = len(history) - 1 - original_idx
        line = f"{color}{displayed_index}: {entry}{Style.RESET_ALL}"
        print(line, end='\n')
    return filtered

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
        time.sleep(0.1)

def main():
    colorama.init()
    history = []
    redraw_event = threading.Event()
    current_filter = ""

    clipboard_thread = threading.Thread(target=monitor_clipboard, args=(history, redraw_event), daemon=True)
    clipboard_thread.start()

    while True:
        if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
            choice = input().strip()
            if not choice:
                current_filter = ""
            elif choice.isdigit():
                idx = int(choice)
                displayed_indexes = []
                for original_idx, entry in enumerate(history):
                    if not current_filter or current_filter.lower() in entry.lower():
                        displayed_index = len(history) - 1 - original_idx
                        displayed_indexes.append(displayed_index)
                if idx in displayed_indexes:
                    original_idx = len(history) - 1 - idx
                    pyperclip.copy(history[original_idx])
                    print(f"Entry {idx} copied to clipboard.")
                else:
                    print("Invalid index.")
                current_filter = ""
                redraw_event.set()
            else:
                current_filter = choice
                redraw_event.set()  # Trigger immediate screen refresh after filter update

        if redraw_event.is_set():
            display_entries(history, current_filter)
            redraw_event.clear()

        time.sleep(0.1)

if __name__ == "__main__":
    main()
