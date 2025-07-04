# Hollow Knight Hunter Journal GUI

A Python-based GUI application for tracking enemy kills and completion progress in Hollow Knight. This tool helps players monitor their Hunter Journal progress by reading save files and displaying kill counts in a user-friendly interface.

## Features

- **Real-time Save File Reading**: Automatically reads and decrypts Hollow Knight save files
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

## Requirements

- Python 3.7+
- Tkinter (usually included with Python)
- requests
- Pillow

## File Structure

```
HollowKnight/
├── GUI.py                 # Main GUI application
├── read_savefile.py       # Save file reader and processor
├── decrypt.py            # Save file decryption utility
├── enemies.json          # Enemy database with kill requirements
├── current_save.json     # Current save file data (generated)
├── decrypted.json        # Decrypted save file (generated)
├── images/               # Enemy images directory
├── maps/                 # Enemy map images directory
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Usage

### Main GUI (GUI.py)

- **Launch**: Run `python GUI.py`
- **Refresh**: Click the refresh button (↻) to update kill counts
- **Search**: Use the search bar to find specific enemies
- **Filter**: Use the "Location" button to filter by region
- **Sort**: Toggle between "most completed" and "least completed"
- **Scroll**: Use the scroll bar or up arrow (↑) to navigate

### Save File Reading (read_savefile.py)

- **Purpose**: Reads and processes Hollow Knight save files
- **Output**: Generates `current_save.json` with current kill counts
- **Usage**: Run `python read_savefile.py` to update save data

## Configuration

### Enemy Data

- Edit `enemies.json` to modify enemy names, locations, or required kill counts
- Each enemy entry contains: `code_name`, `game_name`, and `kill_count`

### Save File Path

- Update the save file path in `decrypt.py` if your Hollow Knight save is in a different location
- Default location: Steam userdata directory

## Features in Detail

### Hunter Journal Integration

- Tracks all enemies from the official Hunter Journal
- Shows required kills vs. actual kills
- Displays completion percentage

### Visual Interface

- Clean, modern design with Calibri font
- Color-coded completion status
- Enemy images with proper scaling
- Responsive layout

### Data Management

- Automatic save file decryption
- Real-time kill count updates
- Persistent data storage
- Error handling for missing files

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
