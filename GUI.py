import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk, ImageDraw
from io import BytesIO
import threading
import os
from decrypt import decrypt_savefile
from read_savefile import current_savefile
import json

# Hunter Journal data
hunter_journal_kills = {
    "Crawlid": [0, 0, "Forgotten Crossroads"],
    "Vengefly": [0, 45, "Forgotten Crossroads"],
    "Vengefly King": [0, 2, "Forgotten Crossroads"],
    "Gruzzer": [0, 25, "Forgotten Crossroads"],
    "Gruz Mother": [0, 3, "Forgotten Crossroads"],
    "Tiktik": [0, 30, "Forgotten Crossroads"],
    "Aspid Hunter": [0, 20, "Greenpath"],
    "Aspid Mother": [0, 15, "Greenpath"],
    "Aspid Hatchling": [0, 30, "Greenpath"],
    "Goam": [0, 1, "Forgotten Crossroads"],
    "Wandering Husk": [0, 35, "City of Tears"],
    "Husk Hornhead": [0, 35, "City of Tears"],
    "Leaping Husk": [0, 35, "City of Tears"],
    "Husk Bully": [0, 35, "City of Tears"],
    "Husk Warrior": [0, 10, "City of Tears"],
    "Husk Guard": [0, 6, "City of Tears"],
    "Entombed Husk": [0, 10, "City of Tears"],
    "False Knight": [0, 1, "Forgotten Crossroads"],
    "Maggot": [0, 2, "Forgotten Crossroads"],
    "Lifeseed": [0, 10, "Greenpath"],
    "Baldur": [0, 20, "Greenpath"],
    "Elder Baldur": [0, 1, "Greenpath"],
    "Mosscreep": [0, 30, "Greenpath"],
    "Mossfly": [0, 25, "Greenpath"],
    "Mosskin": [0, 25, "Greenpath"],
    "Volatile Mosskin": [0, 25, "Greenpath"],
    "Fool Eater": [0, 15, "Fog Canyon"],
    "Squit": [0, 25, "Fog Canyon"],
    "Obble": [0, 20, "Fog Canyon"],
    "Gulka": [0, 15, "Fog Canyon"],
    "Maskfly": [0, 15, "Fog Canyon"],
    "Moss Charger": [0, 15, "Greenpath"],
    "Massive Moss Charger": [0, 1, "Greenpath"],
    "Moss Knight": [0, 8, "Greenpath"],
    "Mossy Vagabond": [0, 10, "Greenpath"],
    "Durandoo": [0, 8, "Fog Canyon"],
    "Duranda": [0, 8, "Fog Canyon"],
    "Aluba": [0, 1, "Queen's Garden"],
    "Charged Lumafly": [0, 1, "Fog Canyon"],
    "Uoma": [0, 20, "Fog Canyon"],
    "Ooma": [0, 12, "Fog Canyon"],
    "Uumuu": [0, 1, "Fog Canyon"],
    "Ambloom": [0, 15, "Fog Canyon"],
    "Fungling": [0, 30, "Fungal Wastes"],
    "Fungoon": [0, 20, "Fungal Wastes"],
    "Sporg": [0, 20, "Fungal Wastes"],
    "Void Tendrils": [0, 1, "Ancient Basin"],
    "Shade": [0, 1, "Various"],
    "Hunter's Mark": [0, 1, "Hunter's Journal"],
    "Belfly": [0, 1, "Forgotten Crossroads"],
    "Bluggsac": [0, 1, "Fog Canyon"],
    "Boofly": [0, 20, "Kingdom's Edge"],
    "Brooding Mawlek": [0, 1, "Forgotten Crossroads"],
    "Carver Hatcher": [0, 15, "Deepnest"],
    "Corpse Creeper": [0, 15, "Deepnest"],
    "Crystallised Husk": [0, 15, "Crystal Peak"],
    "Crystal Crawler": [0, 15, "Crystal Peak"],
    "Crystal Guardian": [0, 2, "Crystal Peak"],
    "Crystal Hunter": [0, 20, "Crystal Peak"],
    "Death Loodle": [0, 15, "Deepnest"],
    "Deephunter": [0, 20, "Deepnest"],
    "Deepling": [0, 25, "Deepnest"],
    "Dirtcarver": [0, 35, "Deepnest"],
    "Dung Defender": [0, 1, "Royal Waterways"],
    "Flukefey": [0, 15, "Royal Waterways"],
    "Flukemarm": [0, 1, "Royal Waterways"],
    "Flukemon": [0, 20, "Royal Waterways"],
    "Flukemunga": [0, 8, "Royal Waterways"],
    "Garpede": [0, 1, "Deepnest"],
    "Glimback": [0, 15, "Crystal Peak"],
    "Gorgeous Husk": [0, 1, "City of Tears"],
    "Great Hopper": [0, 10, "Forgotten Crossroads"],
    "Great Husk Sentry": [0, 10, "City of Tears"],
    "Heavy Fool": [0, 20, "Colosseum of Fools"],
    "Heavy Sentry": [0, 20, "City of Tears"],
    "Hive Guardian": [0, 12, "The Hive"],
    "Hive Knight": [0, 1, "The Hive"],
    "Hive Soldier": [0, 15, "The Hive"],
    "Hopper": [0, 25, "Forgotten Crossroads"],
    "Husk Dandy": [0, 25, "City of Tears"],
    "Husk Hive": [0, 10, "City of Tears"],
    "Husk Miner": [0, 20, "Crystal Peak"],
    "Hwurmp": [0, 20, "Deepnest"],
    "Infected Balloon": [0, 10, "Infected Crossroads"],
    "Kingsmould": [0, 2, "White Palace"],
    "Lance Sentry": [0, 25, "City of Tears"],
    "Little Weaver": [0, 20, "Deepnest"],
    "Loodle": [0, 15, "Deepnest"],
    "Mantis Lords": [0, 1, "Mantis Village"],
    "Mantis Petra": [0, 16, "Mantis Village"],
    "Mantis Traitor": [0, 15, "Mantis Village"],
    "Mantis Warrior": [0, 25, "Mantis Village"],
    "Mantis Youth": [0, 25, "Mantis Village"],
    "Mistake": [0, 25, "Soul Sanctum"],
    "Folly": [0, 15, "Soul Sanctum"],
    "Nosk": [0, 1, "Deepnest"],
    "Oblobbles": [0, 3, "Colosseum of Fools"],
    "Pale Lurker": [0, 1, "Colosseum of Fools"],
    "Pilflip": [0, 20, "Fog Canyon"],
    "Primal Aspid": [0, 25, "Kingdom's Edge"],
    "Royal Retainer": [0, 10, "White Palace"],
    "Shadow Creeper": [0, 20, "Deepnest"],
    "Sharp Baldur": [0, 20, "Greenpath"],
    "Shardmite": [0, 15, "Crystal Peak"],
    "Shrumal Ogre": [0, 8, "Fungal Wastes"],
    "Shrumal Warrior": [0, 20, "Fungal Wastes"],
    "Shrumeling": [0, 20, "Fungal Wastes"],
    "Soul Master": [0, 1, "Soul Sanctum"],
    "Soul Twister": [0, 20, "Soul Sanctum"],
    "Soul Warrior": [0, 2, "Soul Sanctum"],
    "Spiny Husk": [0, 20, "City of Tears"],
    "Stalking Devout": [0, 15, "Deepnest"],
    "Sturdy Fool": [0, 25, "Colosseum of Fools"],
    "Traitor Lord": [0, 1, "Queen's Gardens"],
    "Volt Twister": [0, 6, "Soul Sanctum"],
    "Watcher Knight": [0, 1, "Watcher's Spire"],
    "Winged Fool": [0, 25, "Colosseum of Fools"],
    "Winged Sentry": [0, 30, "City of Tears"],
    "Wingmould": [0, 10, "White Palace"],
    "Hollow Knight": [0, 1, "Forgotten Crossroads"],
    "Menderbug": [0, 1, "Forgotten Crossroads"],
    "Fungified Husk": [0, 10, "Fungal Wastes"],
    "Lost Kin": [0, 0, "Ancient Basin"],
    "Cowardly Husk": [0, 25, "City of Tears"],
    "Gluttonous Husk": [0, 25, "City of Tears"],
    "Collector": [0, 1, "City of Tears"],
    "Furious Vengefly": [0, 15, "Infected Crossroads"],
    "Volatile Gruzzer": [0, 25, "Greenpath"],
    "Violent Husk": [0, 15, "Infected Crossroads"],
    "Slobbering Husk": [0, 15, "Infected Crossroads"],
    "Lesser Mawlek": [0, 10, "Ancient Basin"],
    "Stalking Devout": [0, 15, "Deepnest"],
    "Carver Hatcher": [0, 15, "Deepnest"],
    "Hiveling": [0, 30, "Kingdom's Edge,"],
    "Grub Mimic": [0, 5, "Multiple Locations"],
    "Mawlurk": [0, 10, "Ancient Basin"],
    "Lightseed": [0, 20, "Infected Crossroads"],
    "Sibling": [0, 25, "The Birthplace"],
    "Armoured Squit": [0, 15, "Colosseum of Fools"],
    "God Tamer": [0, 1, "Colosseum of Fools"],
    "Elder Hu": [0, 1, "Fungal Wastes"],
    "Xero": [0, 1, "Resting Grounds"],
    "Gorb": [0, 1, "Howling Cliffs"],
    "Marmu": [0, 1, "Queen's Gardens"],
    "No Eyes": [0, 1, "Greenpath"],
    "Markoth": [0, 1, "Kingdom's Edge"],
    "Galien": [0, 1, "Deepnest"],
    "Volatile Zoteling": [0, 1, "Dirtmouth (Dream)"],
    "Hopping Zoteling": [0, 1, "Dirtmouth (Dream)"],
    "Zote": [0, 1, "Deepnest"],
    "The Hunter": [0, 1, "Greenpath"],
}

first_startup = False


def update_kill_count():
    try:
        # read the current save file
        current_savefile()
        # Load current_save.json
        save_path = os.path.join(os.path.dirname(__file__), "current_save.json")
        if not os.path.exists(save_path):
            raise FileNotFoundError("current_save.json not found!")
        with open(save_path, "r", encoding="utf-8") as f:
            save_data = json.load(f)
        # Build a lookup for game_name -> kill_count
        kill_lookup = {entry["game_name"]: entry["kill_count"] for entry in save_data}

        # Update hunter_journal_kills
        global hunter_journal_kills
        for enemy, values in hunter_journal_kills.items():
            required_kills = values[1]
            kill_count = kill_lookup.get(enemy, 0)
            values[0] = abs(kill_count - required_kills)
        return True
    except Exception as e:
        print(f"Error updating kill count: {e}")
        return False


def normalize_name(name):
    return name.lower().replace(" ", "_").replace("'", "").replace("-", "_")


def show_save_file_error(root):
    """Display error message when save file cannot be found"""
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Create error message frame
    error_frame = tk.Frame(root, bg="#d6d6d6")
    error_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Error title
    error_title = tk.Label(
        error_frame,
        text="Save File Not Found",
        font=("Calibri", 16, "bold"),
        fg="#1f2027",
        bg="#d6d6d6",
    )
    error_title.pack(pady=(0, 20))

    # Error message
    error_msg = tk.Label(
        error_frame,
        text="The Hollow Knight save file could not be found.\n\nThis usually means:\n• Hollow Knight is not installed\n• You haven't created a save file yet\n• The save file is in a different location\n\nClick the button below to watch a tutorial on how to find your save file.",
        font=("Calibri", 11),
        fg="#0e3768",
        bg="#d6d6d6",
        justify="left",
        wraplength=400,
    )
    error_msg.pack(pady=(0, 20))

    # Video link button
    def open_video_tutorial():
        import webbrowser

        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with actual tutorial video
        webbrowser.open(video_url)

    video_button = tk.Button(
        error_frame,
        text="📹 Watch Tutorial Video",
        font=("Calibri", 12, "bold"),
        bg="#1f2027",
        fg="#ffffff",
        relief="raised",
        bd=2,
        padx=20,
        pady=10,
        command=open_video_tutorial,
    )
    video_button.pack(pady=(0, 20))

    # Retry button
    def retry_load():
        if update_kill_count():
            # Success - recreate the main GUI
            create_main_gui(root)
        else:
            # Still failed - show error again
            show_save_file_error(root)

    retry_button = tk.Button(
        error_frame,
        text="🔄 Retry",
        font=("Calibri", 11),
        bg="#555555",
        fg="#ffffff",
        relief="raised",
        bd=1,
        padx=15,
        pady=8,
        command=retry_load,
    )
    retry_button.pack()


def create_main_gui(root):
    """Create the main GUI interface"""
    global first_startup

    # Clear any existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Set up the main window
    root.title("Hunter Journal Guide")
    root.geometry("250x500")
    root.resizable(False, True)
    bg = "#d6d6d6"
    # Configure dark green background with light green border
    root.configure(bg="#1a4d1a")

    # Create main frame with light green border
    main_frame = tk.Frame(root, bg=bg)
    main_frame.pack(fill="both", expand=True, padx=2, pady=2)

    # Title label - smaller and fixed at top
    title_label = tk.Label(
        main_frame,
        text="Hunter Journal Guide",
        font=("Calibri", 12, "bold"),
        fg="#555555",
        bg=bg,
    )
    title_label.pack(anchor="n", pady=10)

    # Create canvas for scrolling
    canvas = tk.Canvas(main_frame, bg=bg, highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg=bg)

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # update the kill count after reading the current save file
    if not first_startup:
        update_kill_count()
        first_startup = True

    # Store all monster data for filtering
    all_monsters = []
    for monster, kills in hunter_journal_kills.items():
        image_path = os.path.join("images", f"{normalize_name(monster)}.png")
        if not os.path.exists(image_path):
            continue
        all_monsters.append((monster, kills, image_path))

    # By default, sort all_monsters by location
    all_monsters.sort(key=lambda m: m[1][2])

    # Add sort button above the search bar
    sort_descending = [False]  # Default: less defeated to most

    def sort_and_update():
        sort_descending[0] = not sort_descending[0]
        if sort_descending[0]:
            sort_button.config(text="less completed")
        else:
            sort_button.config(text="most completed")
        update_monster_list()

    # Get all unique locations for filtering
    unique_locations = sorted(
        set(
            k[2].strip()
            for _, k in hunter_journal_kills.items()
            if len(k) > 2 and k[2].strip()
        )
    )
    unique_locations = ["All"] + unique_locations
    selected_location = ["All"]  # Mutable for closure

    # Add a frame to hold the sort, options, and refresh buttons side by side
    button_frame = tk.Frame(main_frame, bg=bg)
    button_frame.pack(anchor="n", fill="x", padx=20, pady=(0, 5))

    sort_button = tk.Button(
        button_frame,
        text="most completed",
        command=sort_and_update,
        font=("Calibri", 10),  # Smaller font
        bg="#1f2027",
        fg="#ffffff",
        relief="raised",
        bd=0,
        width=14,
        height=1,
        padx=2,
        pady=1,
    )
    sort_button.pack(side="left", padx=(0, 4))

    # Create the menu for location filtering
    options_menu = tk.Menu(root, tearoff=0)

    def set_location_filter(loc):
        selected_location[0] = loc
        update_monster_list()

    for loc in unique_locations:
        options_menu.add_command(
            label=loc, command=lambda l=loc: set_location_filter(l)
        )

    def show_options_menu(event=None):
        x = options_button.winfo_rootx()
        y = options_button.winfo_rooty() + options_button.winfo_height()
        options_menu.tk_popup(x, y)

    options_button = tk.Button(
        button_frame,
        text="Location",
        font=("Calibri", 9),
        bg="#1f2027",
        fg="#ffffff",
        relief="raised",
        bd=0,
        width=8,
        height=1,
        padx=2,
        pady=1,
    )
    options_button.pack(side="left")
    options_button.bind("<Button-1>", show_options_menu)

    # Add refresh button (top right)
    def refresh_kills():
        if update_kill_count():
            update_monster_list()
        else:
            # Show error message if refresh fails
            show_save_file_error(root)

    refresh_button = tk.Button(
        button_frame,
        text="\u21bb",  # Unicode clockwise open circle arrow
        font=("Calibri", 12),
        bg="#d6d6d6",
        fg="#1f2027",
        relief="raised",
        bd=0,
        width=2,  # Increased width
        height=1,
        padx=2,
        pady=0,
        command=refresh_kills,
    )
    refresh_button.pack(side="right")

    # Add upward arrow button to the right of the refresh button
    def scroll_to_top():
        canvas.yview_moveto(0)

    up_button = tk.Button(
        button_frame,
        text="\u2191",  # Unicode upward arrow
        font=("Calibri", 12),
        bg="#d6d6d6",
        fg="#1f2027",
        relief="raised",
        bd=0,
        width=2,
        height=1,
        padx=2,
        pady=0,
        command=scroll_to_top,
    )
    up_button.pack(side="left", padx=(2, 2))  # Add space between up and Location button
    refresh_button.pack(
        side="left", padx=(2, 2)
    )  # Add space between up and Location button

    options_button.pack(side="left", padx=(2, 2))

    # Function to update the displayed monsters based on search and location filter
    def update_monster_list(*args):
        # Clear current widgets
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        search_text = search_var.get().lower()
        if search_text == "search...":
            search_text = ""
        filtered = [m for m in all_monsters if search_text in m[0].lower()]
        # Apply location filter
        if selected_location[0] != "All":
            filtered = [m for m in filtered if m[1][2].strip() == selected_location[0]]
        # Sort by (Defeated - Required kills) difference
        if sort_descending[0]:
            # most defeated: lowest difference to highest
            filtered.sort(key=lambda m: m[1][0] - m[1][1])
        else:
            # less defeated: highest difference to lowest
            filtered.sort(key=lambda m: m[1][0] - m[1][1], reverse=True)
        for monster, kills, image_path in filtered:
            monster_frame = tk.Frame(scrollable_frame, bg=bg)
            monster_frame.pack(fill="x", padx=5, pady=2)
            info_frame = tk.Frame(monster_frame, bg=bg)
            info_frame.pack(side="left", fill="y", padx=(0, 10))
            name_label = tk.Label(
                info_frame,
                text=monster,
                font=("Calibri", 10, "bold"),
                fg="#1f2027",
                bg=bg,
                anchor="w",
            )
            name_label.pack(anchor="w")
            kills_label = tk.Label(
                info_frame,
                text=f"Defeated: {kills[0]} | Required Kills: {kills[1]}",
                font=("Calibri", 8),
                fg="#0e3768",
                bg=bg,
                anchor="w",
            )
            kills_label.pack(anchor="w")
            location = kills[2] if len(kills) > 2 else "Unknown"
            location_label = tk.Label(
                info_frame,
                text=f"{location}",
                font=("Calibri", 8),
                fg="#0e3768",
                bg=bg,
                anchor="w",
            )
            location_label.pack(anchor="w")
            try:
                img = Image.open(image_path)
                max_size = (64, 64)
                if img.width > 64 or img.height > 64:
                    img.thumbnail(max_size, Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                image_label = tk.Label(
                    monster_frame,
                    image=photo,
                    bg=bg,
                    width=64,
                    height=64,
                    relief="flat",
                    bd=0,
                )
                image_label.image = photo
                image_label.pack(side="left", padx=(0, 0))
            except Exception as e:
                print(f"Failed to load image for {monster}: {e}")
                continue
            separator = tk.Frame(scrollable_frame, height=1, bg="white")
            separator.pack(fill="x", padx=5, pady=1)

    # Add search bar below the sort button
    search_var = tk.StringVar()

    search_var.trace_add("write", update_monster_list)
    search_entry = tk.Entry(
        main_frame, textvariable=search_var, font=("Calibri", 10), fg="black"
    )
    search_entry.pack(anchor="n", fill="x", padx=20, pady=(0, 10))
    search_entry.insert(0, "Search...")

    def clear_search_placeholder(event):
        if search_entry.get() == "Search...":
            search_entry.delete(0, tk.END)

    search_entry.bind("<FocusIn>", clear_search_placeholder)

    # Initial population
    update_monster_list()

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind mouse wheel to canvas
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    root.attributes("-topmost", True)

    root.mainloop()

input_file = r'' #save file path

def main():
    """Main function that handles initial setup and error checking"""
    root = tk.Tk()


    # Try to load save file on startup
    if not first_startup:
        if update_kill_count():
            # Success - create main GUI
            create_main_gui(root)
        else:
            # Failed - show error message
            show_save_file_error(root)
    else:
        # First startup - create main GUI without loading save file
        create_main_gui(root)

    root.mainloop()


