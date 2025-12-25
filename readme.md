# FITS Frame Counter

A user-friendly Python tool for astrophotographers to count light frames by filter and date. Works with any folder structure through interactive prompts.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- **Folder picker dialog** — no typing paths
- **Configurable** — works with any folder naming convention
- **Flexible** — supports any FITS filter keyword
- **Summary totals** — see counts per session and overall
- **Ordered output** — filters displayed in logical order (L, R, G, B, H, S, O)

## Sample Output

```
FITS Frame Counter
==================================================

Settings:
  Date keyword: date
  Subfolder: lights
  Filter keyword: FILTER

Analyzing: /home/user/astro_data

--------------------------------------------------
date_2025-12-20: {'L': 50, 'R': 25, 'G': 25, 'B': 25}
date_2025-12-21: {'L': 40, 'Ha': 30}
date_2025-12-24: {'L': 60, 'R': 20, 'G': 20, 'B': 20, 'Ha': 15}
--------------------------------------------------
TOTAL: {'L': 150, 'R': 45, 'G': 45, 'B': 45, 'Ha': 45}
```

## Installation

### Option 1: Run from source

```bash
# Install dependency
pip install astropy

# Run
python fits_counter.py
```

### Option 2: Create standalone executable

```bash
# Install PyInstaller
pip install pyinstaller

# Create .exe (Windows) or binary (Mac/Linux)
pyinstaller --onefile --windowed fits_counter.py
```

The executable will be in the `dist` folder. Share this file — no Python installation required!

## Usage

1. **Run the program**
2. **Configure your settings** (three dialog boxes):
   - **Date identifier**: What text identifies your date folders? (e.g., "date", "2025", or blank for all folders)
   - **Subfolder name**: What's your lights folder called? (e.g., "lights", "Light", "LIGHT")
   - **FITS keyword**: What header keyword contains filter info? (e.g., "FILTER", "FILTER1", "FILTNAM")
3. **Select your data folder**
4. **View results**

## Supported Folder Structures

The program is flexible. Here are some examples that all work:

**Structure A: date prefix**
```
data/
├── date_2025-12-20/
│   └── lights/
└── date_2025-12-21/
    └── lights/
```
Settings: Date keyword = `date`, Subfolder = `lights`

**Structure B: date only**
```
data/
├── 2025-12-20/
│   └── Light/
└── 2025-12-21/
    └── Light/
```
Settings: Date keyword = `2025`, Subfolder = `light`

**Structure C: target names with dates**
```
data/
├── M31_2025-12-20/
│   └── LIGHTS/
└── M42_2025-12-21/
    └── LIGHTS/
```
Settings: Date keyword = `2025`, Subfolder = `lights`

**Structure D: all folders (no date filtering)**
```
data/
├── session1/
│   └── lights/
└── session2/
    └── lights/
```
Settings: Date keyword = (leave blank), Subfolder = `lights`

## Common FITS Filter Keywords

| Camera/Software | Keyword |
|-----------------|---------|
| ZWO ASI | FILTER |
| QHY | FILTER |
| NINA | FILTER |
| SGP | FILTER |
| MaxIm DL | FILTER |
| Some filter wheels | FILTER1 |
| Older software | FILTNAM |

Not sure? Run this on one of your FITS files to see all keywords:

```python
from astropy.io import fits
header = fits.getheader('your_image.fits')
for key in header:
    print(f"{key}: {header[key]}")
```

## Troubleshooting

**"No matching folders found"**
- Check your date keyword matches your folder names
- Verify the subfolder name is correct (case-insensitive)
- Make sure folders contain .fits files

**"UNKNOWN" filter showing**
- Your FITS files use a different keyword
- Run the keyword check above to find the correct one

**Dialog boxes not appearing**
- On Linux, you may need: `sudo apt install python3-tk`
- On Mac, tkinter should be included with Python

## Creating an Executable

To share with others who don't have Python:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed fits_counter.py
```

Find the executable in the `dist/` folder.

**Note for Mac users:** You may need to right-click and select "Open" the first time due to Gatekeeper.

## Executable Download

You can find a downloadable exe file in the repo if you want to just download that or make it yourself with the instructions above. 

## Contributing

Suggestions welcome!

## License

MIT License — free to use, modify, and distribute.

## Acknowledgments

Built with:
- [Astropy](https://www.astropy.org/) — FITS file handling
- Python's tkinter — GUI dialogs
- Claude.ai for readme creation, code commenting, and quick checks of logic/syntax

Clear skies! 🌟