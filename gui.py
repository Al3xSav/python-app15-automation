import tkinter as tk
from tkinter import messagebox

from main import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        # ✅ Make sure to initialize web_automation
        self.web_automation = WebAutomation()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        # Login Frame
        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name:").grid(row=0, column=0, sticky="w")
        self.fullname_entry = tk.Entry(self.form_frame)
        self.fullname_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email:").grid(row=1, column=0, sticky="w")
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address:").grid(row=2, column=0, sticky="w")
        self.current_address_entry = tk.Entry(self.form_frame)
        self.current_address_entry.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address:").grid(row=3, column=0, sticky="w")
        self.permanent_address_entry = tk.Entry(self.form_frame)
        self.permanent_address_entry.grid(row=3, column=1, sticky="ew")

        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10, padx=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)


    def submit_data(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        fullname = self.fullname_entry.get()
        email = self.email_entry.get()
        current_address = self.current_address_entry.get()
        permanent_address = self.permanent_address_entry.get()

        # Perform actions with the submitted data
        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(fullname, email, current_address, permanent_address)
        self.web_automation.download()
    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Browser Closed", "Submitted Successfully")

root = tk.Tk()
app = App(root)
root.mainloop()