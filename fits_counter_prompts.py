from pathlib import Path
from astropy.io import fits
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

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
        
def get_user_settings():
    """Prompt user for their folder structure settings."""
    root = tk.Tk()
    root.withdraw()
    
    # Ask for date identifier
    date_keyword = simpledialog.askstring(
        "Date Identifier",
        "How are your date folders identified?\n\n"
        "Examples:\n"
        "  • 'date' if folders are like 'date_2025-12-24'\n"
        "  • '2025' if folders are like '2025-12-24'\n"
        "  • Leave blank to include ALL subfolders",
        parent=root
    )
    
    # Ask for subfolder name
    subfolder_name = simpledialog.askstring(
        "Subfolder Name",
        "What is your imaging subfolder called?\n\n"
        "Examples: lights, light, Light, LIGHT",
        initialvalue="lights",
        parent=root
    )
    
    # Ask for filter keyword
    filter_keyword = simpledialog.askstring(
        "FITS Keyword",
        "What FITS header keyword contains your filter name?\n\n"
        "Common options: FILTER, FILTER1, FILTNAM",
        initialvalue="FILTER",
        parent=root
    )
    
    root.destroy()
    
    return {
        'date_keyword': date_keyword.lower() if date_keyword else None,
        'subfolder_name': subfolder_name.lower() if subfolder_name else 'lights',
        'filter_keyword': filter_keyword.upper() if filter_keyword else 'FILTER'
    }
    
def contains_date(folder_name, date_keyword):
    """Check if folder matches date criteria."""
    if date_keyword is None:
        return True  # Include all folders
    return date_keyword in folder_name.lower()
    

def get_subfolder(folder, subfolder_name): #goes inside folders with dates and checks if those sub files are folders and if so checks if their name is light or lights and then returns the path
    """Find specified subfolder."""
    for item in folder.iterdir():
        if item.is_dir() and item.name.lower() == subfolder_name:
            return item
    return None

"""Count FITS files by filter in the given folder."""        
def fits_counter(folder, filter_keyword):
    counts = defaultdict(int) #missing key counts start at 0
    
    for fits_file in folder.glob('*.fits'): #finds files in the lights folder that are .fits
        try:
            header = fits.getheader(fits_file) #gets the fits heade
            filter_name = header.get(filter_keyword, 'UNKNOWN')
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
    results =[]
    
    settings = get_user_settings()
    folder = folder_selection()
    
    print(f"\nSettings:")
    print(f"  Date keyword: {settings['date_keyword'] or '(all folders)'}")
    print(f"  Subfolder: {settings['subfolder_name']}")
    print(f"  Filter keyword: {settings['filter_keyword']}")
    print(f"\nAnalyzing: {folder}\n")
    print("-" * 50)
    
    for subfolder in sorted(folder.iterdir()):
        if not subfolder.is_dir():
            continue
        if not contains_date(subfolder.name, settings['date_keyword']):
            continue
        
        target_folder = get_subfolder(subfolder, settings['subfolder_name'])
        if not target_folder:
            continue
        
        found_any = True
        counts = fits_counter(target_folder, settings['filter_keyword'])
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