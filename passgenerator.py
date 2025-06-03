from tkinter import *
from tkinter import messagebox
import string
import random

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f8ff")


        title_lbl = Label(self.root, text=" Password Generator", font=("Helvetica", 20, "bold"), fg="#333", bg="#f0f8ff")
        title_lbl.pack(pady=20)


        length_lbl = Label(self.root, text="Enter Password Length:", font=("Arial", 12), bg="#f0f8ff")
        length_lbl.pack(pady=5)

        self.length_entry = Entry(self.root, font=("Arial", 12), justify=CENTER)
        self.length_entry.pack(pady=5)


        generate_btn = Button(self.root, text="Generate Password", font=("Arial", 12, "bold"),
                              bg="#4CAF50", fg="white", width=25, command=self.generate_password)
        generate_btn.pack(pady=15)


        self.output_label = Label(self.root, text="", font=("Arial", 13), fg="green", bg="#f0f8ff")
        self.output_label.pack(pady=10)


        copy_btn = Button(self.root, text="Copy to Clipboard", font=("Arial", 12, "bold"),
                          bg="#FF5722", fg="white", width=25, command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)

    def generate_password(self):
        length_str = self.length_entry.get()

        if not length_str.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        length = int(length_str)
        if length < 4:
            messagebox.showwarning("Too Short", "Password length should be at least 4 characters.")
            return


        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(chars, k=length))

        self.output_label.config(text=f"{password}")

    def copy_to_clipboard(self):
        password = self.output_label.cget("text")
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("No Password", "Please generate a password first.")


if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
