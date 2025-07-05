#!/usr/bin/env python3
"""
Script to compare enemies.json code names with decrypted.json kill data
and find any missing entries.
"""

import json
import os


def load_json_file(filename):
    """Load and parse a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: {filename} not found!")
        return None
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {filename}: {e}")
        return None


def extract_kill_keys_from_decrypted(decrypted_data):
    """Extract all 'killed' keys from decrypted.json (not 'kills' keys)."""
    kill_keys = set()

    if "playerData" in decrypted_data:
        player_data = decrypted_data["playerData"]

        # Look for keys that start with 'killed' (not 'kills')
        for key in player_data.keys():
            if key.startswith("killed"):
                kill_keys.add(key)

    return kill_keys


def extract_code_names_from_enemies(enemies_data):
    """Extract all code_name values from enemies.json."""
    code_names = set()

    if isinstance(enemies_data, list):
        for enemy in enemies_data:
            if isinstance(enemy, dict) and "code_name" in enemy:
                code_names.add(enemy["code_name"])

    return code_names


def compare_enemies():
    """Main comparison function."""
    print("=" * 60)
    print("  Hollow Knight Enemy Comparison Tool")
    print("=" * 60)
    print()

    # Load files
    print("Loading files...")
    enemies_data = load_json_file("enemies.json")
    decrypted_data = load_json_file("decrypted.json")

    if enemies_data is None or decrypted_data is None:
        return

    # Extract data
    print("Extracting data...")
    enemies_code_names = extract_code_names_from_enemies(enemies_data)
    decrypted_kill_keys = extract_kill_keys_from_decrypted(decrypted_data)

    print(f"Found {len(enemies_code_names)} code names in enemies.json")
    print(f"Found {len(decrypted_kill_keys)} 'killed' keys in decrypted.json")
    print()

    # Find missing entries
    print("=" * 60)
    print("  ANALYSIS RESULTS")
    print("=" * 60)
    print()

    # Find code names in enemies.json that don't have corresponding kill data
    missing_kill_data = []
    for code_name in enemies_code_names:
        if code_name not in decrypted_kill_keys:
            missing_kill_data.append(code_name)

    # Find kill data in decrypted.json that don't have corresponding code names
    missing_code_names = []
    for kill_key in decrypted_kill_keys:
        if kill_key not in enemies_code_names:
            missing_code_names.append(kill_key)

    # Report results
    print(
        f"Code names in enemies.json missing from decrypted.json: {len(missing_kill_data)}"
    )
    if missing_kill_data:
        print("Missing kill data for:")
        for code_name in sorted(missing_kill_data):
            print(f"  - {code_name}")
    else:
        print("  ✓ All code names have corresponding kill data!")

    print()

    print(
        f"'killed' keys in decrypted.json missing from enemies.json: {len(missing_code_names)}"
    )
    if missing_code_names:
        print("Missing code names for:")
        for kill_key in sorted(missing_code_names):
            print(f"  - {kill_key}")
    else:
        print("  ✓ All 'killed' keys have corresponding code names!")

    print()

    # Summary
    print("=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(f"Total code names in enemies.json: {len(enemies_code_names)}")
    print(f"Total 'killed' keys in decrypted.json: {len(decrypted_kill_keys)}")
    print(f"Missing kill data: {len(missing_kill_data)}")
    print(f"Missing code names: {len(missing_code_names)}")

    if len(missing_kill_data) == 0 and len(missing_code_names) == 0:
        print("\n🎉 PERFECT MATCH! All entries are synchronized.")
    else:
        print(
            f"\n⚠️  {len(missing_kill_data) + len(missing_code_names)} discrepancies found."
        )

    print()


if __name__ == "__main__":
    compare_enemies()
