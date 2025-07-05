import os
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

# Folder to save images
SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)


hunter_journal_kills = {
    "Crawlid": [0, 1, "Forgotten Crossroads"],
    "Vengefly": [0, 45, "Forgotten Crossroads"],
    "Vengefly King": [0, 2, "Forgotten Crossroads"],
    "Gruzzer": [0, 25, "Forgotten Crossroads"],
    "Gruz Mother": [0, 3, "Forgotten Crossroads"],
    "Tiktik": [0, 30, "Forgotten Crossroads"],
    "Aspid Hunter": [0, 20, "Forgotten Crossroads"],
    "Aspid Mother": [0, 15, "Forgotten Crossroads"],
    "Aspid Hatchling": [0, 30, "Forgotten Crossroads"],
    "Goam": [0, 1, "Forgotten Crossroads"],
    "Wandering Husk": [0, 35, "City of Tears"],
    "Husk Hornhead": [0, 35, "City of Tears"],
    "Leaping Husk": [0, 35, "City of Tears"],
    "Husk Bully": [0, 35, "City of Tears"],
    "Husk Warrior": [0, 10, "City of Tears"],
    "Husk Guard": [0, 6, "Forgotten Crossroads"],
    "Entombed Husk": [0, 10, "City of Tears"],
    "False Knight": [0, 1, "Forgotten Crossroads"],
    "Maggot": [0, 2, "Forgotten Crossroads"],
    "Lifeseed": [0, 10, "Greenpath"],
    "Baldur": [0, 20, "Forgotten Crossroads"],
    "Elder Baldur": [0, 1, "Forgotten Crossroads"],
    "Mosscreep": [0, 30, "Greenpath"],
    "Mossfly": [0, 25, "Greenpath"],
    "Mosskin": [0, 25, "Greenpath"],
    "Volatile Mosskin": [0, 25, "Greenpath"],
    "Fool Eater": [0, 15, "Greenpath"],
    "Squit": [0, 25, "Greenpath"],
    "Obble": [0, 20, "Greenpath"],
    "Gulka": [0, 15, "Greenpath"],
    "Maskfly": [0, 15, "Greenpath"],
    "Moss Charger": [0, 15, "Greenpath"],
    "Massive Moss Charger": [0, 1, "Greenpath"],
    "Moss Knight": [0, 8, "Greenpath"],
    "Mossy Vagabond": [0, 10, "Greenpath"],
    "Durandoo": [0, 8, "Greenpath"],
    "Duranda": [0, 8, "Greenpath"],
    "Aluba": [0, 1, "Queen's Garden"],
    "Charged Lumafly": [0, 1, "Fog Canyon"],
    "Uoma": [0, 20, "Fog Canyon"],
    "Ooma": [0, 12, "Fog Canyon"],
    "Uumuu": [0, 1, "Fog Canyon"],
    "Ambloom": [0, 15, "Fungal Wastes"],
    "Fungling": [0, 30, "Fungal Wastes"],
    "Fungoon": [0, 20, "Fungal Wastes"],
    "Sporg": [0, 20, "Fungal Wastes"],
    "Void Tendrils": [0, 1, "Ancient Basin"],
    "Shade": [0, 1, "The Birthplace"],
    "Hunter's Mark": [0, 1, "Hunter's Journal"],
    "Belfly": [0, 15, "Forgotten Crossroads"],
    "Bluggsac": [0, 1, "Multiple Locations"],
    "Boofly": [0, 20, "Kingdom's Edge"],
    "Brooding Mawlek": [0, 1, "Forgotten Crossroads"],
    "Carver Hatcher": [0, 15, "Deepnest"],
    "Corpse Creeper": [0, 15, "Deepnest"],
    "Husk Miner": [0, 20, "Crystal Peak"],
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
    "Husk Sentry": [0, 25, "City of Tears"],
    "Heavy Fool": [0, 20, "Colosseum of Fools"],
    "Heavy Sentry": [0, 20, "City of Tears"],
    "Hive Guardian": [0, 12, "The Hive"],
    "Hornet": [0, 2, "Greenpath"],
    "Oblobble": [0, 3, "Colosseum of Fools"],
    "Grey Prince Zote": [0, 1, "Dirtmouth (Dream)"],
    "Zote": [0, 1, "Colosseum of Fools"],
    "White Defender": [0, 1, "Royal Waterways"],
    "Hive Knight": [0, 1, "The Hive"],
    "Hive Soldier": [0, 15, "The Hive"],
    "Hopper": [0, 25, "Forgotten Crossroads"],
    "Husk Dandy": [0, 25, "City of Tears"],
    "Husk Hive": [0, 10, "The Hive"],
    "Shielded Fool": [0, 25, "Colosseum of Fools"],
    "Crystallised Husk": [0, 15, "Crystal Peak"],
    "Hwurmp": [0, 20, "Deepnest"],
    "Infected Balloon": [0, 10, "Forgotten Crossroads"],
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
    "Pilflip": [0, 20, "Royal Waterways"],
    "Primal Aspid": [0, 25, "Kingdom's Edge"],
    "Royal Retainer": [0, 1, "White Palace"],
    "Shadow Creeper": [0, 20, "Ancient Basin"],
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
    "The Collector": [0, 1, "Tower of Love"],
    "Traitor Lord": [0, 1, "Queen's Garden"],
    "Volt Twister": [0, 6, "Soul Sanctum"],
    "Watcher Knight": [0, 1, "City of Tears"],
    "Winged Fool": [0, 25, "Colosseum of Fools"],
    "Winged Sentry": [0, 30, "City of Tears"],
    "Wingmould": [0, 1, "White Palace"],
    "Hollow Knight": [0, 1, "Forgotten Crossroads"],
    "Menderbug": [0, 0, "Forgotten Crossroads"],
    "Fungified Husk": [0, 10, " Fungal Wastes"],
    "Lost Kin": [0, 1, "Ancient Basin"],
    "Cowardly Husk": [0, 25, "City of Tears"],
    "Gluttonous Husk": [0, 25, "City of Tears"],
    "Collector": [0, 1, "City of Tears"],
    "Furious Vengefly": [0, 15, "Forgotten Crossroads"],
    "Volatile Gruzzer": [0, 25, "Greenpath"],
    "Violent Husk": [0, 15, "Forgotten Crossroads"],
    "Slobbering Husk": [0, 15, "Forgotten Crossroads"],
    "Lesser Mawlek": [0, 10, "Ancient Basin & C.O.F"],
    "Stalking Devout": [0, 15, "Deepnest"],
    "Carver Hatcher": [0, 15, "Deepnest"],
    "Hiveling": [0, 30, "The Hive"],
    "Grub Mimic": [0, 5, "Multiple Locations"],
    "Mawlurk": [0, 10, "Ancient Basin"],
    "Lightseed": [0, 20, "Forgotten Crossroads"],
    "Sibling": [0, 25, "The Birthplace"],
    "Armoured Squit": [0, 15, "Colosseum of Fools"],
    "God Tamer": [0, 1, "Colosseum of Fools"],
    "Elder Hu": [0, 1, "Fungal Wastes"],
    "Xero": [0, 1, "Resting Grounds"],
    "Gorb": [0, 1, "Howling Cliffs"],
    "Marmu": [0, 1, "Queen's Garden"],
    "No Eyes": [0, 1, "Greenpath"],
    "Markoth": [0, 1, "Kingdom's Edge"],
    "Galien": [0, 1, "Deepnest"],
    "Volatile Zoteling": [0, 1, "Dirtmouth (Dream)"],
    "Hopping Zoteling": [0, 1, "Dirtmouth (Dream)"],
    "The Hunter": [0, 1, "Greenpath"],
}

enemies = [
    {"code_name": "killedCrawler", "game_name": "Crawlid"},
    {"code_name": "killedBuzzer", "game_name": "Vengefly"},
    {"code_name": "killedBouncer", "game_name": "Baldur"},
    {"code_name": "killedBouncer", "game_name": "Gruzzer"},
    {"code_name": "killedClimber", "game_name": "Tiktik"},
    {"code_name": "killedWorm", "game_name": "Goam"},
    {"code_name": "killedSpitter", "game_name": "Aspid Hunter"},
    {"code_name": "killedHatcher", "game_name": "Carver Hatcher"},
    {"code_name": "killedHatchling", "game_name": "Aspid Hatchling"},
    {"code_name": "killedZombieRunner", "game_name": "Wandering Husk"},
    {"code_name": "killedZombieHornhead", "game_name": "Husk Hornhead"},
    {"code_name": "killedZombieLeaper", "game_name": "Leaping Husk"},
    {"code_name": "killedZombieBarger", "game_name": "Husk Bully"},
    {"code_name": "killedZombieShield", "game_name": "Husk Warrior"},
    {"code_name": "killedZombieGuard", "game_name": "Husk Guard"},
    {"code_name": "killedBigBuzzer", "game_name": "Vengefly King"},
    {"code_name": "killedBigFly", "game_name": "Gruz Mother"},
    {"code_name": "killedMawlek", "game_name": "Brooding Mawlek"},
    {"code_name": "killedFalseKnight", "game_name": "False Knight"},
    {"code_name": "killedRoller", "game_name": "Baldur"},
    {"code_name": "killedBlocker", "game_name": "Elder Baldur"},
    {"code_name": "killedPrayerSlug", "game_name": "Maggot"},
    {"code_name": "killedMenderBug", "game_name": "Menderbug"},
    {"code_name": "killedMossmanRunner", "game_name": "Mosscreep"},
    {"code_name": "killedMossmanShaker", "game_name": "Mosskin"},
    {"code_name": "killedMosquito", "game_name": "Squit"},
    {"code_name": "killedBlobFlyer", "game_name": "Boofly"},
    {"code_name": "killedFungifiedZombie", "game_name": "Fungified Husk"},
    {"code_name": "killedPlantShooter", "game_name": "Gulka"},
    {"code_name": "killedMossCharger", "game_name": "Moss Charger"},
    {"code_name": "killedMegaMossCharger", "game_name": "Massive Moss Charger"},
    {"code_name": "killedSnapperTrap", "game_name": "Fool Eater"},
    {"code_name": "killedMossKnight", "game_name": "Moss Knight"},
    {"code_name": "killedGrassHopper", "game_name": "Shrumal Warrior"},
    {"code_name": "killedAcidWalker", "game_name": "Durandoo"},
    {"code_name": "killedMossFlyer", "game_name": "Mossfly"},
    {"code_name": "killedMossKnightFat", "game_name": "Heavy Sentry"},
    {"code_name": "killedMossWalker", "game_name": "Mossy Vagabond"},
    {"code_name": "killedInfectedKnight", "game_name": "Lost Kin"},
    {"code_name": "killedLazyFlyer", "game_name": "Maskfly"},
    {"code_name": "killedZapBug", "game_name": "Charged Lumafly"},
    {"code_name": "killedJellyfish", "game_name": "Uoma"},
    {"code_name": "killedJellyCrawler", "game_name": "Ambloom"},
    {"code_name": "killedMegaJellyfish", "game_name": "Uumuu"},
    {"code_name": "killedFungoonBaby", "game_name": "Fungling"},
    {"code_name": "killedMushroomTurret", "game_name": "Sporg"},
    {"code_name": "killedMantis", "game_name": "Mantis Warrior"},
    {"code_name": "killedMushroomRoller", "game_name": "Shrumal Warrior"},
    {"code_name": "killedMushroomBrawler", "game_name": "Shrumal Ogre"},
    {"code_name": "killedMushroomBaby", "game_name": "Shrumeling"},
    {"code_name": "killedMantisFlyerChild", "game_name": "Mantis Petra"},
    {"code_name": "killedFungusFlyer", "game_name": "Fungling"},
    {"code_name": "killedFungCrawler", "game_name": "Shrumeling"},
    {"code_name": "killedMantisLord", "game_name": "Mantis Lords"},
    {"code_name": "killedBlackKnight", "game_name": "Watcher Knight"},
    {"code_name": "killedElectricMage", "game_name": "Soul Warrior"},
    {"code_name": "killedMage", "game_name": "Mistake"},
    {"code_name": "killedMageKnight", "game_name": "Soul Warrior"},
    {"code_name": "killedRoyalDandy", "game_name": "Husk Dandy"},
    {"code_name": "killedRoyalCoward", "game_name": "Cowardly Husk"},
    {"code_name": "killedRoyalPlumper", "game_name": "Gluttonous Husk"},
    {"code_name": "killedFlyingSentrySword", "game_name": "Winged Sentry"},
    {"code_name": "killedFlyingSentryJavelin", "game_name": "Lance Sentry"},
    {"code_name": "killedSentry", "game_name": "Husk Sentry"},
    {"code_name": "killedSentryFat", "game_name": "Heavy Sentry"},
    {"code_name": "killedMageBlob", "game_name": "Folly"},
    {"code_name": "killedGreatShieldZombie", "game_name": "Great Husk Sentry"},
    {"code_name": "killedJarCollector", "game_name": "Collector"},
    {"code_name": "killedMageBalloon", "game_name": "Infected Balloon"},
    {"code_name": "killedMageLord", "game_name": "Soul Master"},
    {"code_name": "killedGorgeousHusk", "game_name": "Gorgeous Husk"},
    {"code_name": "killedFlipHopper", "game_name": "Pilflip"},
    {"code_name": "killedFlukeman", "game_name": "Flukemon"},
    {"code_name": "killedFlukeMother", "game_name": "Flukemarm"},
    {"code_name": "killedDungDefender", "game_name": "Dung Defender"},
    {"code_name": "killedCrystalCrawler", "game_name": "Crystal Crawler"},
    {"code_name": "killedCrystalFlyer", "game_name": "Crystal Hunter"},
    {"code_name": "killedLaserBug", "game_name": "Shardmite"},
    {"code_name": "killedBeamMiner", "game_name": "Husk Miner"},
    {"code_name": "killedZombieMiner", "game_name": "Crystallised Husk"},
    {"code_name": "killedMegaBeamMiner", "game_name": "Crystal Guardian"},
    {"code_name": "killedMinesCrawler", "game_name": "Glimback"},
    {"code_name": "killedAngryBuzzer", "game_name": "Furious Vengefly"},
    {"code_name": "killedBurstingBouncer", "game_name": "Volatile Gruzzer"},
    {"code_name": "killedBurstingZombie", "game_name": "Violent Husk"},
    {"code_name": "killedSpittingZombie", "game_name": "Slobbering Husk"},
    {"code_name": "killedBabyCentipede", "game_name": "Deepling"},
    {"code_name": "killedBigCentipede", "game_name": "Deephunter"},
    {"code_name": "killedCentipedeHatcher", "game_name": "Dirtcarver"},
    {"code_name": "killedLesserMawlek", "game_name": "Lesser Mawlek"},
    {"code_name": "killedSlashSpider", "game_name": "Stalking Devout"},
    {"code_name": "killedSpiderCorpse", "game_name": "Corpse Creeper"},
    {"code_name": "killedShootSpider", "game_name": "Lesser Mawlek"},
    {"code_name": "killedMiniSpider", "game_name": "Little Weaver"},
    {"code_name": "killedSpiderFlyer", "game_name": "Carver Hatcher"},
    {"code_name": "killedMimicSpider", "game_name": "Nosk"},
    {"code_name": "killedBeeHatchling", "game_name": "Hiveling"},
    {"code_name": "killedBeeStinger", "game_name": "Hive Soldier"},
    {"code_name": "killedBigBee", "game_name": "Hive Guardian"},
    {"code_name": "killedHiveKnight", "game_name": "Hive Knight"},
    {"code_name": "killedBlowFly", "game_name": "Hwurmp"},
    {"code_name": "killedCeilingDropper", "game_name": "Spiny Husk"},
    {"code_name": "killedGiantHopper", "game_name": "Great Hopper"},
    {"code_name": "killedGrubMimic", "game_name": "Grub Mimic"},
    {"code_name": "killedMawlekTurret", "game_name": "Mawlurk"},
    {"code_name": "killedOrangeScuttler", "game_name": "Lightseed"},
    {"code_name": "killedHealthScuttler", "game_name": "Lifeseed"},
    {"code_name": "killedPigeon", "game_name": "Loodle"},
    {"code_name": "killedZombieHive", "game_name": "Husk Hive"},
    {"code_name": "killedDreamGuard", "game_name": "Kingsmould"},
    {"code_name": "killedHornet", "game_name": "Hornet"},
    {"code_name": "killedAbyssCrawler", "game_name": "Shadow Creeper"},
    {"code_name": "killedSuperSpitter", "game_name": "Primal Aspid"},
    {"code_name": "killedSibling", "game_name": "Sibling"},
    {"code_name": "killedPalaceFly", "game_name": "Wingmould"},
    {"code_name": "killedEggSac", "game_name": "Bluggsac"},
    {"code_name": "killedMummy", "game_name": "Entombed Husk"},
    {"code_name": "killedOrangeBalloon", "game_name": "Infected Balloon"},
    {"code_name": "killedAbyssTendril", "game_name": "Void Tendrils"},
    {"code_name": "killedHeavyMantis", "game_name": "Mantis Traitor"},
    {"code_name": "killedTraitorLord", "game_name": "Traitor Lord"},
    {"code_name": "killedMantisHeavyFlyer", "game_name": "Mantis Petra"},
    {"code_name": "killedGardenZombie", "game_name": "Royal Retainer"},
    {"code_name": "killedRoyalGuard", "game_name": "Kingsmould"},
    {"code_name": "killedWhiteRoyal", "game_name": "White Defender"},
    {"code_name": "killedOblobble", "game_name": "Oblobble"},
    {"code_name": "killedZote", "game_name": "Zote"},
    {"code_name": "killedBlobble", "game_name": "Obble"},
    {"code_name": "killedColMosquito", "game_name": "Armoured Squit"},
    {"code_name": "killedColRoller", "game_name": "Sharp Baldur"},
    {"code_name": "killedColFlyingSentry", "game_name": "Winged Fool"},
    {"code_name": "killedColMiner", "game_name": "Sturdy Fool"},
    {"code_name": "killedColShield", "game_name": "Shielded Fool"},
    {"code_name": "killedColWorm", "game_name": "Garpede"},
    {"code_name": "killedColHopper", "game_name": "Death Loodle"},
    {"code_name": "killedLobsterLancer", "game_name": "God Tamer"},
    {"code_name": "killedGhostAladar", "game_name": "Elder Hu"},
    {"code_name": "killedGhostXero", "game_name": "Xero"},
    {"code_name": "killedGhostHu", "game_name": "Gorb"},
    {"code_name": "killedGhostMarmu", "game_name": "Marmu"},
    {"code_name": "killedGhostNoEyes", "game_name": "No Eyes"},
    {"code_name": "killedGhostMarkoth", "game_name": "Markoth"},
    {"code_name": "killedGhostGalien", "game_name": "Galien"},
    {"code_name": "killedWhiteDefender", "game_name": "White Defender"},
    {"code_name": "killedGreyPrince", "game_name": "Grey Prince Zote"},
    {"code_name": "killedZotelingBalloon", "game_name": "Volatile Zoteling"},
    {"code_name": "killedZotelingHopper", "game_name": "Hopping Zoteling"},
    {"code_name": "killedHopper", "game_name": "Hopper"},
    {"code_name": "killedHollowKnight", "game_name": "Hollow Knight"},
    {"code_name": "killedAcidFlyer", "game_name": "Duranda"},
    {"code_name": "killedHunterMark", "game_name": "The Hunter"},
    {"code_name": "killedFatFluke", "game_name": "Flukemunga"},
    {"code_name": "killedPaleLurker", "game_name": "Pale Lurker"},
]


def normalize_name(name):
    return name.lower().replace(" ", "_").replace("'", "").replace("-", "_")


def download_enemy_image(name):
    encoded_name = urllib.parse.quote(name.replace(" ", "_"))
    url = (
        f"https://hollowknight.fandom.com/wiki/{encoded_name}?file=B_{encoded_name}.png"
    )

    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to access page for {name}: {e}")
        return

    soup = BeautifulSoup(resp.text, "html.parser")

    # Look for the image link in the file section
    image_tag = soup.select_one("a.image img")
    if not image_tag:
        print(f"No image found for {name}")
        return

    img_url = image_tag.get("src")
    if not img_url:
        print(f"No src found for {name}")
        return

    if img_url.startswith("//"):
        img_url = "https:" + img_url

    ext = os.path.splitext(img_url)[1].split("?")[0]
    if ext.lower() not in [".png", ".jpg", ".jpeg", ".gif", ".webp"]:
        ext = ".png"

    filename = normalize_name(name) + ext
    filepath = os.path.join(SAVE_DIR, filename)

    try:
        img_data = requests.get(img_url).content
        with open(filepath, "wb") as f:
            f.write(img_data)
        # print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download image for {name}: {e}")


folder_path = "images"
os.makedirs(folder_path, exist_ok=True)

expected_files = [normalize_name(name) for name in hunter_journal_kills.keys()]

# Get actual files in the folder (without extension)
actual_files = [
    os.path.splitext(f)[0]
    for f in os.listdir(SAVE_DIR)
    if os.path.isfile(os.path.join(SAVE_DIR, f))
]

# Find missing ones
missing = [name for name in expected_files if name not in actual_files]

print(f"Total enemies: {len(expected_files)}")
print(f"Images found: {len(actual_files)}")
print(f"Missing images: {len(missing)}")
print("\nEnemies without images:")
for m in missing:
    print(m)

l = [
    "Husk Sentry",
    "Zote",
    "Grey Prince Zote",
    "Oblobble",
    "White Defender",
    "Shielded Fool",
]
for i in l:
    download_enemy_image(i)
