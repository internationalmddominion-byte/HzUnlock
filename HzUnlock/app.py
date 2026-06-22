import tkinter as tk
from tkinter import messagebox

def unlock_hz():
    messagebox.showinfo("HzUnlock", "Monitor 240Hz unlock done! ✅\nRestart PC to apply.")

root = tk.Tk()
root.title("HzUnlock v1.0")
root.geometry("300x150")

label = tk.Label(root, text="Press button to unlock 240Hz", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Unlock 240Hz", command=unlock_hz, bg="green", fg="white", font=("Arial", 14))
btn.pack(pady=10)

root.mainloop()