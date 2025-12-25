from pathlib import Path
from astropy.io import fits
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox

"""Open folder picker dialog and return selected path."""
def folder_selection():
    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open the folder picker
    folder_string = filedialog.askdirectory(title='Select your data folder') #filediaglog returns path as a string but wrapped in path it is a file path allowing for iteration through the subfolders. 
   
    if folder_string:  # User selected something
        folder = Path(folder_string)
        print(f'You selected: {folder.name}')
        root.destroy()
        return folder
    else:
        print("No folder selected")
        exit()
    
"""Check if folder name contains 'date' keyword."""
def contains_date(folder_name):
    #looking for the date keyword in the folder name
    if 'date' in folder_name:
            return True
    else:
        return False

"""Find and return the lights subfolder, or None if not found."""
def get_lights(folder): #goes inside folders with dates and checks if those sub files are folders and if so checks if their name is light or lights and then returns the path
    for item in folder.iterdir():
        if item.is_dir():
            if item.name.lower() in ('light', 'lights'):
                return item
    return None

"""Count FITS files by filter in the given folder."""        
def fits_counter(lights_folder):
    counts = defaultdict(int) #missing key counts start at 0
    
    for fits_file in lights_folder.glob('*.fits'): #finds files in the lights folder that are .fits
        try:
            header = fits.getheader(fits_file) #gets the fits heade
            filter_name = header.get('FILTER', 'UNKNOWN')
            counts[filter_name] += 1
        except Exception as e:
            print(f"Error reading {fits_file.name}: {e}")   
    return counts

def order_filters(counts):
    preferred_order = ['L', 'R', 'G', 'B', 'H', 'S', 'O']
    ordered = {}
    
    # Add filters in preferred order first
    for key in preferred_order:
        if key in counts:
            ordered[key] = counts[key]
    
    # Add any remaining filters not in the list
    for key in counts:
        if key not in ordered:
            ordered[key] = counts[key]
    
    return ordered

def main():
    global_counts = defaultdict(int)
    found_any = False
    results = []
    
    folder = folder_selection()
    
    for subfolder in sorted(folder.iterdir()):
        if not subfolder.is_dir() or not contains_date(subfolder.name):
            continue
        
        lights_folder = get_lights(subfolder)
        if not lights_folder:
            continue
        
        found_any = True
        counts = fits_counter(lights_folder)
        ordered = order_filters(counts)
        print(f"{subfolder.name}: {dict(ordered)}") #converts to regular dict
        results.append(f"{subfolder.name}: {dict(ordered)}")    
        
        for filter_name, count in counts.items():
            global_counts[filter_name] += count
            
    if found_any:
        print("-" * 50)
        print(f"TOTAL: {order_filters(dict(global_counts))}")
        results.append('-' * 40)
        results.append(f"TOTAL: {order_filters(dict(global_counts))}")
        message = "\n".join(results)
    else:
        print("No date folders with lights found.")        
        message = "No matching folders found."
        
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("FITS Frame Counter - Results", message)
    root.destroy()           
        
if __name__ == "__main__":
    main()