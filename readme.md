# FITS Frame Counter

A user-friendly Python tool for astrophotographers to count light frames by filter and date. Works with any folder structure.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- **Folder picker dialog** — no typing paths
- **Configurable** — works with any folder naming convention
- **Flexible** — supports any FITS filter keyword
- **Summary totals** — see counts per session and overall
- **Ordered output** — filters displayed in logical order (L, R, G, B, H, S, O)

## Scripts

This project includes two versions:

| Script | Description |
|--------|-------------|
| `fits.py` | Simple version with hardcoded settings (looks for "date" folders and "lights" subfolders) |
| `fits_counter_prompts.py` | Configurable version with interactive prompts for custom folder structures |

---

## fits.py — Simple Version

Best for users with a standard folder structure using "date" prefixes and "lights" subfolders.

### Sample Output

```
You selected: astro_data

date_2025-12-20: {'L': 50, 'R': 25, 'G': 25, 'B': 25}
date_2025-12-21: {'L': 40, 'Ha': 30}
date_2025-12-24: {'L': 60, 'R': 20, 'G': 20, 'B': 20, 'Ha': 15}
--------------------------------------------------
TOTAL: {'L': 150, 'R': 45, 'G': 45, 'B': 45, 'Ha': 45}
```

A popup dialog also displays the results:

```
┌─────────────────────────────────────────────────┐
│  FITS Frame Counter - Results                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  date_2025-12-20: {'L': 50, 'R': 25, 'G': 25,   │
│                    'B': 25}                     │
│  date_2025-12-21: {'L': 40, 'Ha': 30}           │
│  date_2025-12-24: {'L': 60, 'R': 20, 'G': 20,   │
│                    'B': 20, 'Ha': 15}           │
│  ----------------------------------------       │
│  TOTAL: {'L': 150, 'R': 45, 'G': 45,            │
│          'B': 45, 'Ha': 45}                     │
│                                                 │
│                    [ OK ]                       │
└─────────────────────────────────────────────────┘
```

### Expected Folder Structure

```
data/
├── date_2025-12-20/
│   └── lights/
│       ├── image_001.fits
│       └── image_002.fits
└── date_2025-12-21/
    └── lights/
        └── image_001.fits
```

---

## fits_counter_prompts.py — Configurable Version

Best for users with custom folder structures or non-standard naming conventions.

### Sample Output

```
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

### Configuration Dialogs

Before selecting a folder, three dialog prompts appear:

```
┌─────────────────────────────────────────────────┐
│  Date Identifier                                │
├─────────────────────────────────────────────────┤
│                                                 │
│  How are your date folders identified?          │
│                                                 │
│  Examples:                                      │
│    • 'date' if folders are like 'date_2025...' │
│    • '2025' if folders are like '2025-12-24'   │
│    • Leave blank to include ALL subfolders     │
│                                                 │
│  [ date_____________________________ ]          │
│                                                 │
│              [ OK ]  [ Cancel ]                 │
└─────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────┐
│  Subfolder Name                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  What is your imaging subfolder called?         │
│                                                 │
│  Examples: lights, light, Light, LIGHT          │
│                                                 │
│  [ lights___________________________ ]          │
│                                                 │
│              [ OK ]  [ Cancel ]                 │
└─────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────┐
│  FITS Keyword                                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  What FITS header keyword contains your         │
│  filter name?                                   │
│                                                 │
│  Common options: FILTER, FILTER1, FILTNAM       │
│                                                 │
│  [ FILTER___________________________ ]          │
│                                                 │
│              [ OK ]  [ Cancel ]                 │
└─────────────────────────────────────────────────┘
```

### Results Dialog

```
┌─────────────────────────────────────────────────┐
│  FITS Frame Counter - Results                   │
├─────────────────────────────────────────────────┤
│                                                 │
│  date_2025-12-20: {'L': 50, 'R': 25, 'G': 25,   │
│                    'B': 25}                     │
│  date_2025-12-21: {'L': 40, 'Ha': 30}           │
│  date_2025-12-24: {'L': 60, 'R': 20, 'G': 20,   │
│                    'B': 20, 'Ha': 15}           │
│  ----------------------------------------       │
│  TOTAL: {'L': 150, 'R': 45, 'G': 45,            │
│          'B': 45, 'Ha': 45}                     │
│                                                 │
│                    [ OK ]                       │
└─────────────────────────────────────────────────┘
```

---

## Installation

### Option 1: Run from source

```bash
# Install dependency
pip install astropy

# Run simple version
python fits.py

# Run configurable version
python fits_counter_prompts.py
```

### Option 2: Create standalone executable

```bash
# Install PyInstaller
pip install pyinstaller

# Create .exe (Windows) or binary (Mac/Linux)
pyinstaller --onefile --windowed fits_counter_prompts.py
```

The executable will be in the `dist` folder. Share this file — no Python installation required!

---

## Supported Folder Structures

The configurable version (`fits_counter_prompts.py`) is flexible. Here are some examples:

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

---

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

---

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

---

## Executable Download

You can find a downloadable exe file in the repo if you want to just download that or make it yourself with the instructions above.

---

## Contributing

Suggestions welcome!

## License

MIT License — free to use, modify, and distribute.

## Support

If this tool helped with your imaging sessions, consider buying me a coffee!

<a href="buymeacoffee.com/dzauski585u">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="200">
</a>

## Acknowledgments

Built with:
- [Astropy](https://www.astropy.org/) — FITS file handling
- Python's tkinter — GUI dialogs
- Claude.ai for readme creation, code commenting, and quick checks of logic/syntax

Clear skies! 🌟
