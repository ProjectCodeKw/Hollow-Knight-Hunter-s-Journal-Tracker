# Hollow Knight Hunter Journal GUI

I was going INSANE wanted that COMPLETE hunter achievement but there was no way for me to keep track of how many kills i need for each enemy and how many i have left ;(
Thats why i used a little bit of that Pyyyy magic and now i have an external friendly mod that keeps track of my deadly habbits (killing bugs)...

Ok now some technical details 🐧

## Features

- **Interactive GUI**: Built with Tkinter for easy navigation and filtering
- **Enemy Tracking**: Tracks all 156+ enemies from the Hunter Journal
- **Location Filtering**: Filter enemies by region/location
- **Search Functionality**: Search enemies by name
- **Sort Options**: Sort by completion status (most/least completed)
- **Visual Indicators**: Shows enemy images and completion status
- **Auto-refresh**: Update kill counts from current save file

## Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python GUI.py
   ```
ORRRR run the .exe/.bat file... more on it below

## Requirements

- Python 3.7+
- Tkinter (usually included with Python)
- requests
- Pillow

## Usage

### START.exe or START.bat

- If you dont have Python installed run this as a normal program :D
- Before you start the program insert your savefile path into the text file named: HK_savefilepath.txt without any spacing or extra characters or quotation
- If you wanna use another save file change the value within that textfile
- If an error occurs try running it with administration access because it needs to read your current savefile

### START.py

- Run this script to start the GUI overlay
- Before running it change the input_file variable to your actual savefile path
- To find your save file [Click Here](https://example.com)

### Enemy Data
This was the hardest part since the enemy names are different in the savefile from their actual names. Literally spent HOURS guessing, AI-ing and questoning WHAT THE HELL IS kellingPrayerSlug turns out its the two maggots... apperantly they prey to you before you kill them lol. Also AI SUCKS Gemini, DeepAI and ChatGPT were useless when mapping, ceativity is human's only superpower afterall.

P.S. thats why if there is a miss naming please tell me ;)

- Edit `enemies.json` to modify enemy names, locations, or required kill counts
- Each enemy entry contains: `code_name`, `game_name`, and `kill_count`

## Troubleshooting

### Common Issues

1. **"Save file not found"**

   - Ensure Hollow Knight is installed and you have save files
   - Check the save file path in `decrypt.py`

2. **"Images not loading"**

   - Verify the `images/` directory exists with enemy images
   - Check that image filenames match enemy names

3. **"GUI not starting"**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

### Missing Images

If enemy images are missing, you can:

- Add images to the `images/` directory
- Use the naming format: `enemy_name.png` (lowercase, underscores)
- Images should be 64x64 pixels or smaller for best display

## Contributing

Feel free to contribute improvements:

- Bug fixes
- New features
- UI enhancements
- Additional enemy data

## License

This project is for educational and personal use. Hollow Knight is a trademark of Team Cherry.

## Credits
- **Github Repos** that helped me decrypt the savefile:
  
   -- https://github.com/ReznoRMichael/hollow-knight-completion-check
   -- https://github.com/bloodorca/hollow
  
- **Hollow Knight**: Developed by Team Cherry
- **Enemy Data**: Based on official Hunter Journal Wiki
- **Images**: From Hollow Knight Wiki (Fandom)
