import tkinter as tk


class Dashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Automation Suite")

        self.root.geometry("400x300")

        title = tk.Label(self.root, text="Automation Suite Dashboard", font=("Arial", 16))
        title.pack(pady=20)

        btn1 = tk.Button(self.root, text="Run File Organizer")
        btn1.pack(pady=10)

        btn2 = tk.Button(self.root, text="Run Web Scraper")
        btn2.pack(pady=10)

        btn3 = tk.Button(self.root, text="Check System")
        btn3.pack(pady=10)

        self.root.mainloop()