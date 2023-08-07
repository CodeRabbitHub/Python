import os
import platform
import tkinter as tk
from tkinter import filedialog, scrolledtext

selected_drive = ""
previous_selections = []


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_label.config(text=f"Selected Folder: {folder_path}")
        output_text.insert(tk.END, f"Selected Folder: {folder_path}\n")
        previous_selections.append(f"Selected Folder: {folder_path}")
    else:
        selected_label.config(text="")
        output_text.insert(tk.END, "Folder selection canceled.\n")
        previous_selections.append("Folder selection canceled.")


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_label.config(text=f"Selected File: {file_path}")
        output_text.insert(tk.END, f"Selected File: {file_path}\n")
        previous_selections.append(f"Selected File: {file_path}")
    else:
        selected_label.config(text="")
        output_text.insert(tk.END, "File selection canceled.\n")
        previous_selections.append("File selection canceled.")


def select_drive(*args):
    global selected_drive
    selected_drive = option_var.get()
    if selected_drive:
        selected_label.config(text=f"Selected Drive: {selected_drive}")
        output_text.insert(tk.END, f"Selected Drive: {selected_drive}\n")
        previous_selections.append(f"Selected Drive: {selected_drive}")


def undo_selection():
    global previous_selections
    if previous_selections:
        previous_selections.pop()
        output_text.delete("1.0", tk.END)
        for selection in previous_selections:
            output_text.insert(tk.END, selection + "\n")


def clear_output():
    global previous_selections
    output_text.delete("1.0", tk.END)
    previous_selections = []


def go_back():
    global previous_selections
    selected_label.config(text="")
    option_var.set(options[0])
    output_text.delete("1.0", tk.END)
    previous_selections = []


def get_available_drives():
    if platform.system() == "Windows":
        return [d for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
    else:
        return []


root = tk.Tk()
root.title("Path Selector")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

drive_label = tk.Label(frame, text="Select Drive:")
drive_label.pack()

drives = get_available_drives()
options = drives if drives else ["No drives detected"]

option_var = tk.StringVar()
option_var.set(options[0])  # Set default option
option_var.trace("w", select_drive)  # Call select_drive when the option is changed

drive_menu = tk.OptionMenu(frame, option_var, *options)
drive_menu.pack()

folder_button = tk.Button(frame, text="Select Folder", command=select_folder)
folder_button.pack(pady=10)

file_button = tk.Button(frame, text="Select File", command=select_file)
file_button.pack()

undo_button = tk.Button(frame, text="Undo", command=undo_selection)
undo_button.pack()

next_button = tk.Button(frame, text="Next", command=clear_output)
next_button.pack()

selected_label = tk.Label(root, text="")
selected_label.pack(padx=20, pady=10)

# Text widget for terminal-like output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
output_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Go Back button
go_back_button = tk.Button(root, text="Go Back", command=go_back)
go_back_button.pack(pady=10)

root.mainloop()
