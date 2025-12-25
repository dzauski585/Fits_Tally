from pathlib import Path
from astropy.io import fits
from datetime import datetime
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog


def folder_selection():
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open the folder picker
    folder_string = filedialog.askdirectory(title='Select your data folder') #filediaglog returns path as a string but wrapped in path it is a file path allowing for iteration through the subfolders. 
   
    if folder_string:  # User selected something
        folder = Path(folder_string)
        print(f'You selected: {folder}')
        root.destroy()
        return folder
    else:
        print("No folder selected")
        exit()

def item_validate(folder):
    if folder.is_dir():
        return True
    else: 
        return False

def contains_date(folder_name):
    # Try every position in the string
    if 'date' in folder_name:
            return True
    else:
        return False

def get_lights(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name.lower() == 'light' or item.name.lower() == 'lights':
                return item
    return None
        
def fits_counter(lights_folder):
    counts = defaultdict(int) #missing key counts start at 0
    for fits_file in lights_folder.glob('*.fits'):
        header = fits.getheader(fits_file)
        if 'FILTER' in header: 
           counts[header['FILTER']] += 1
        else:
           print("No filter found")    
    return counts


def main():
    folder = folder_selection()
    for subfolder in folder.iterdir():
        if item_validate(subfolder) and contains_date(subfolder.name):
            lights_folder = get_lights(subfolder)
            counts = fits_counter(lights_folder)
            print(f"{subfolder}: {dict(counts)}") #converts to regular dict
        else:
            print(f"No date folders found in {subfolder}")
            
if __name__ == "__main__":
    main()