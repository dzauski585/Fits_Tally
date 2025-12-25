import tkinter as tk
from tkinter import filedialog

# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Open the folder picker
folder = filedialog.askdirectory(title='Select your data folder')

print(f'You selected: {folder}')
root.destroy()
