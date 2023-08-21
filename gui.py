import tkinter as tk
from tkinter import filedialog, messagebox

class GUI:
    def __init__(self, title: str, main):
        self.title = title
        self.main = main
        self.window = tk.Tk()
        self.window.title(self.title)
        self._create_widgets()

    def _create_widgets(self):
        self.upload_button = tk.Button(self.window, text="Upload File", command=self._upload_file)
        self.upload_button.pack()

        self.download_button = tk.Button(self.window, text="Download File", command=self._download_file)
        self.download_button.pack()

    def _upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.main.file_path = file_path
            messagebox.showinfo("File Upload", "File uploaded successfully!")

    def _download_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".apkg")
        if file_path:
            self.main.output_path = file_path
            self.main.run()
            messagebox.showinfo("File Download", "File downloaded successfully!")

    def run(self):
        self.window.mainloop()
