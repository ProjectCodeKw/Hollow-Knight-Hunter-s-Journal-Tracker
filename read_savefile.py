import json
from decrypt import decrypt_savefile
import os


def current_savefile(input_file):
    # Step 1: Decrypt the save file (produces decrypted.json)
    decrypt_savefile(input_file)

    # Step 2: Load enemies.json
    with open(
        os.path.join(os.path.dirname(__file__), "enemies.json"), "r", encoding="utf-8"
    ) as f:
        enemies = json.load(f)

    # Step 3: Load decrypted.json
    with open(
        os.path.join(os.path.dirname(__file__), "decrypted.json"), "r", encoding="utf-8"
    ) as f:
        save_data = json.load(f)

    player_data = save_data.get("playerData", {})

    # Step 4: Build the new list with updated kill counts
    updated_enemies = []
    for enemy in enemies:
        code_name = enemy["code_name"]
        # The kill count is stored as 'kills' + code_name[6:]
        # e.g., code_name 'killedCrawler' -> 'killsCrawler'
        kill_key = "kills" + code_name[6:]
        kill_count = player_data.get(kill_key, 0)
        updated_enemy = dict(enemy)
        updated_enemy["kill_count"] = kill_count
        updated_enemies.append(updated_enemy)

    # Step 5: Write to current_save.json
    with open(
        os.path.join(os.path.dirname(__file__), "current_save.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(updated_enemies, f, indent=4)

    print("current_save.json created with updated kill counts.")
