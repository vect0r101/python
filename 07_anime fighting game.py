import random

print("""
Choose your fighting style:

1. Bankai
   - Ultimate release of a Soul Reaper's Zanpakuto.

2. Domain Expansion
   - Creates a powerful domain that overwhelms enemies.

3. Wand + Grimoire Magic
   - Cast powerful magical spells.

""")


choice = int(input("Enter your skill: "))
if choice > 3 or choice < 1:
    print("Invalid choice.")


if choice == 1:
    print("You have chosen Bankai!")
    a = print("Your character is: ", random.choice(skills["1"]["characters"]))
if a >98 :
    print("You Won!")

elif choice == 2:
    print("You have chosen Domain Expansion!")

elif choice == 3:
    print("You have chosen Wand + Grimoire Magic!")






skills = {
    "1": {
        "name": "Bankai",
        "characters": [
            ("Renji Abarai", 60),
            ("Ikkaku Madarame", 62),
            ("Rukia Kuchiki", 65),
            ("Kensei Muguruma", 68),
            ("Rose Otoribashi", 70),
            ("Love Aikawa", 72),
            ("Shinji Hirako", 74),
            ("Soi Fon", 76),
            ("Sajin Komamura", 78),
            ("Mayuri Kurotsuchi", 80),
            ("Kaname Tosen", 82),
            ("Toshiro Hitsugaya", 84),
            ("Byakuya Kuchiki", 88),
            ("Gin Ichimaru", 89),
            ("Yoruichi Shihoin", 90),
            ("Kenpachi Zaraki", 95),
            ("Retsu Unohana", 98),
            ("Ichigo Kurosaki", 102),
            ("Shunsui Kyoraku", 105),
            ("Kisuke Urahara", 108),
            ("Sosuke Aizen", 115),
            ("Genryusai Yamamoto", 120),
            ("Ichibe Hyosube", 125),
            ("Yhwach", 130)
        ]
    },

    "2": {
        "name": "Domain Expansion",
        "characters": [
            ("Megumi Fushiguro", 65),
            ("Dagon", 68),
            ("Hanami", 70),
            ("Jogo", 73),
            ("Mahito", 76),
            ("Hiromi Higuruma", 80),
            ("Kinji Hakari", 82),
            ("Naoya Zenin", 84),
            ("Yorozu", 86),
            ("Ryu Ishigori", 87),
            ("Takako Uro", 88),
            ("Yuji Itadori", 89),
            ("Yuki Tsukumo", 92),
            ("Yuta Okkotsu", 96),
            ("Toji Fushiguro", 98),
            ("Suguru Geto", 100),
            ("Kenjaku", 105),
            ("Satoru Gojo", 120),
            ("Ryomen Sukuna", 130),
            ("Hajime Kashimo", 94),
            ("Maki Zenin", 91),
            ("Uraume", 93)
        ]
    },

    "3": {
        "name": "Magic (Wand + Grimoire)",
        "characters": [
            ("Sekke Bronzazza", 40),
            ("Magna Swing", 55),
            ("Luck Voltia", 70),
            ("Gauche Adlai", 72),
            ("Grey", 65),
            ("Charmy Pappitson", 74),
            ("Vanessa Enoteca", 76),
            ("Finral Roulacase", 68),
            ("Gordon Agrippa", 69),
            ("Zora Ideale", 75),
            ("Noelle Silva", 84),
            ("Yuno", 95),
            ("Asta", 92),
            ("Fuegoleon Vermillion", 96),
            ("Mereoleona Vermillion", 104),
            ("William Vangeance", 98),
            ("Yami Sukehiro", 102),
            ("Julius Novachrono", 110),
            ("Lucius Zogratis", 125),
            ("Zenon Zogratis", 103),
            ("Dante Zogratis", 101),
            ("Vanica Zogratis", 100),
            ("Licht", 108),
            ("Patry", 97)
        ]
    }
}


