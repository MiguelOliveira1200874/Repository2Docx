import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import subprocess
import os

# Define the color scheme and fonts
DARK_BG = "#2D2D30"
DARK_FG = "#CCCCCC"
ACCENT_COLOR = "#007ACC"
FONT_NAME = "Segoe UI"
FONT_SIZE = 10

class ModernRepoDocGUI:
    def __init__(self, root):
        self.root = root
        root.title("Repository Documentation Tool")
        root.configure(bg=DARK_BG)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configure style for buttons
        self.style.configure('TButton', foreground=DARK_FG, background=ACCENT_COLOR, font=(FONT_NAME, FONT_SIZE), borderwidth=1)
        self.style.map('TButton', background=[('active', ACCENT_COLOR)], foreground=[('active', DARK_FG)])

        # Configure style for labels
        self.style.configure('TLabel', background=DARK_BG, foreground=DARK_FG, font=(FONT_NAME, FONT_SIZE))

        # Configure style for entry fields
        self.style.configure('TEntry', fieldbackground=DARK_BG, foreground=DARK_FG, bordercolor=DARK_BG, font=(FONT_NAME, FONT_SIZE))

        # Configure style for checkbuttons
        self.style.configure('TCheckbutton', background=DARK_BG, foreground=DARK_FG, font=(FONT_NAME, FONT_SIZE))
        self.style.map('TCheckbutton', background=[('active', DARK_BG), ('selected', ACCENT_COLOR)])

        # Layout
        self.create_widgets()

    def create_widgets(self):
        # Repository Path
        ttk.Label(self.root, text="Repository Path:").grid(row=0, column=0, sticky="w", padx=10, pady=(10,0))
        self.repo_path_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.repo_path_var, width=50).grid(row=0, column=1, pady=(10,0), padx=(0,10))
        ttk.Button(self.root, text="Browse...", command=self.browse_repo_path).grid(row=0, column=2, pady=(10,0))

        # Output File
        ttk.Label(self.root, text="Output File:").grid(row=1, column=0, sticky="w", padx=10)
        self.output_file_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.output_file_var, width=50).grid(row=1, column=1, padx=(0,10))
        ttk.Button(self.root, text="Browse...", command=self.browse_output_file).grid(row=1, column=2)

        # Options
        self.ignore_settings_var = tk.BooleanVar()
        ttk.Checkbutton(self.root, text="Ignore Settings Files", variable=self.ignore_settings_var).grid(row=2, column=1, sticky="w", padx=10)

        # Generate Button
        ttk.Button(self.root, text="Generate Report", command=self.start_generation_thread).grid(row=3, column=1, pady=10)

        # Progress Bar (using default style for simplicity)
        self.progress = ttk.Progressbar(self.root, length=100, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, pady=10, padx=10)

    def browse_repo_path(self):
        directory = filedialog.askdirectory()
        if directory:
            self.repo_path_var.set(directory)

    def browse_output_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".docx")
        if file:
            self.output_file_var.set(file)

    def generate_report(self):
        self.progress.start()
        try:
            repo_path = self.repo_path_var.get()
            output_file = self.output_file_var.get()
            ignore_settings = self.ignore_settings_var.get()

            # Construindo o comando para executar o script repo2txt.py
            script_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'repo2txt.py')
            command = ['python', script_path, '-r', repo_path, '-o', output_file]
            if ignore_settings:
                command.append('--ignore-settings')

            # Execute o script
            result = subprocess.run(command, capture_output=True, text=True)

            # Verifique se houve erros
            if result.returncode == 0:
                messagebox.showinfo("Sucesso", "O relatório foi gerado com sucesso.", parent=self.root)
            else:
                messagebox.showerror("Erro", f"Falha ao gerar relatório:\n{result.stderr}", parent=self.root)
        finally:
            self.progress.stop()

    def start_generation_thread(self):
        threading.Thread(target=self.generate_report, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernRepoDocGUI(root)
    root.geometry("600x200")
    root.mainloop()