import tkinter as tk
from tkinter import messagebox
import time
import threading

class AlarmeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarme")
        self.root.geometry("300x200")  # Define o tamanho da janela

        self.intervalo_label = tk.Label(root, text="Intervalo (segundos):")
        self.intervalo_label.pack()

        self.intervalo_entry = tk.Entry(root)
        self.intervalo_entry.pack()

        self.repeticoes_label = tk.Label(root, text="Repetições:")
        self.repeticoes_label.pack()

        self.repeticoes_entry = tk.Entry(root)
        self.repeticoes_entry.pack()

        self.iniciar_button = tk.Button(root, text="Iniciar Alarme", command=self.iniciar_alarme)
        self.iniciar_button.pack()

        self.parar_button = tk.Button(root, text="Parar Alarme", command=self.parar_alarme, state=tk.DISABLED)
        self.parar_button.pack()

        self.status_label = tk.Label(root, text="Repetições restantes: N/A")
        self.status_label.pack()

        self.alarme_ativo = False
        self.thread = None

    def iniciar_alarme(self):
        try:
            intervalo = int(self.intervalo_entry.get())
            repeticoes = int(self.repeticoes_entry.get())
            self.alarme_ativo = True
            self.parar_button.config(state=tk.NORMAL)
            self.thread = threading.Thread(target=self.alarme, args=(intervalo, repeticoes))
            self.thread.start()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos")

    def parar_alarme(self):
        self.alarme_ativo = False
        if self.thread is not None:
            self.thread.join()
        self.parar_button.config(state=tk.DISABLED)
        self.status_label.config(text="Repetições restantes: N/A")
        messagebox.showinfo("Alarme", "Alarme parado")

    def alarme(self, intervalo, repeticoes):
        for i in range(repeticoes):
            if not self.alarme_ativo:
                break
            self.status_label.config(text=f"Repetições restantes: {repeticoes - i}")
            time.sleep(intervalo)
            if self.alarme_ativo:
                messagebox.showinfo("Alarme", f"Alarme {i+1}!")
        self.parar_button.config(state=tk.DISABLED)
        self.status_label.config(text="Repetições restantes: N/A")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmeApp(root)
    root.mainloop()
