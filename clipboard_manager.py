import pyperclip
import threading
import time

def monitor_clipboard(history):
    previous_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != previous_clipboard:
            history.append(current_clipboard)
            print("Clipboard added to history.")
            previous_clipboard = current_clipboard
        time.sleep(1)

def main():
    history = []

    clipboard_thread = threading.Thread(target=monitor_clipboard, args=(history,), daemon=True)
    clipboard_thread.start()

    while True:
        print("\nClipboard Manager")
        print("2. View all entries")
        print("3. Select entry by number")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "2":
            if not history:
                print("No entries in history.")
            else:
                for i, entry in enumerate(history):
                    preview = (entry[:20] + "...") if len(entry) > 20 else entry
                    print(f"{i+1}: {preview}")

        elif choice == "3":
            if not history:
                print("No entries to select.")
                continue
            try:
                idx = int(input(f"Enter entry number (1-{len(history)}): ")) - 1
                if 0 <= idx < len(history):
                    pyperclip.copy(history[idx])
                    print(f"Entry {idx+1} copied to clipboard.")
                else:
                    print("Invalid entry number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
