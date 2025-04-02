import random
import tkinter as tk
from tkinter import messagebox

# Expanded word lists for more uniqueness
adjectives = [
    "Stealthy", "Electric", "Majestic", "Vicious", "Clever", "Rogue", "Shadowy", "Infernal", "Mythic", "Quantum", 
    "Xeno", "Nebula", "Cyber", "Eternal", "Dark", "Phantom", "Arcane", "Venomous", "Stormborn", "Titanic", 
    "Radiant", "Nocturnal", "Glacial", "Celestial", "Crimson", "Blazing", "Spectral", "Void", "Lunar", "Solar", 
    "Warped", "Ancient", "Neon", "Vortex", "Silent", "Grim", "Obsidian", "Ember", "Wicked", "Draconic", "Abyssal",
    "Relentless", "Savage", "Tempest", "Frozen", "Spirited", "Vigilant", "Untamed", "Thunderous", "Unyielding", 
    "Radiant", "Invisible", "Frostbite", "Apocalyptic", "Luminous", "Sinister", "Vast", "Phantom", "Unstoppable", 
    "Wicked", "Invincible", "Nocturnal", "Primal", "Titanic"
]

nouns = [
    "Storm", "Titan", "Ghost", "Hawk", "Wolf", "Knight", "Sphinx", "Specter", "Reaper", "Cipher", "Drake", 
    "Phantom", "Rogue", "Sentinel", "Viper", "Striker", "Banshee", "Warden", "Falcon", "Ronin", "Dragon", "Shade", 
    "Enigma", "Raptor", "Blade", "Wraith", "Hunter", "Shogun", "Crusader", "Dagger", "Juggernaut", "Onyx", "Fox", 
    "Warlock", "Samurai", "Golem", "Omen", "Raven", "Demon", "Aether", "Lancer", "Cyborg", "Dragonfly", "Lancer", 
    "Juggernaut", "Spectre", "Viper", "Colossus", "Revenant", "Phoenix", "Shaman", "Oracle", "Exile", "Warlord", 
    "Champion", "Sovereign", "Golem", "Behemoth", "Monarch", "Specter", "Ghoul", "Valkyrie", "Fury", "Ravenous", "Crusader"
]

symbols = ["_", "-", ".", "x", "~", "*"]
leetspeak_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "$", "t": "7"}

# Function to apply leetspeak
def apply_leetspeak(text):
    return ''.join(leetspeak_map.get(char, char) for char in text)

# Function to generate a stylish nickname from a base name
def generate_nickname(base):
    if len(base) > 3:
        transformations = [
            base[::-1],  # Reverse the name
            base[:3] + random.choice("xyz"),  # Truncate and add flair
            base[0].upper() + base[1:].lower() + random.choice("ionx"),  # Capitalization & suffix
            base.replace("a", "@").replace("o", "0"),  # Symbol replacement
            base[:2] + base[-2:],  # Blend front & back
            base.capitalize() + random.choice(["X", "Z", "on", "ius", "yx", "ar"]),  # Append suffix
        ]
        return random.choice(transformations)
    return base.capitalize()

# Function to generate usernames
def generate_usernames():
    name_input = name_entry.get().strip()
    interest_input = interest_entry.get().strip()
    style = style_var.get()
    add_number = num_var.get()
    add_symbol = symbol_var.get()
    use_leetspeak = leet_var.get()
    
    if not name_input:
        messagebox.showerror("Input Error", "Please enter your initials or name.")
        return
    
    usernames = []
    for _ in range(5):  # Generate 5 usernames
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        symbol = random.choice(symbols) if add_symbol else ""
        number = str(random.randint(10, 99)) if add_number else ""
        
        base_name = generate_nickname(name_input)
        interest_fragment = interest_input[:4].capitalize() if interest_input else ""
        
        if style == "Cool":
            username = f"{adj}{noun}"
        elif style == "Funny":
            username = f"{random.choice(['Bouncy', 'Goofy', 'Wacky', 'Zany', 'Jumpy', 'Silly', 'Crazy', 'Bizarre', 'Quirky', 'Loco', 'Mondo', 'Sponge', 'Jolly', 'Loony', 'Clumsy', 'Odd', 'Snappy', 'Bubbly', 'Hapless', 'Mischief', 'Comical', 'Ticklish', 'Cheeky', 'Jester', 'Nutty'])}{noun}"
        elif style == "Mysterious":
            username = f"{random.choice(['Void', 'Dark', 'Shadow'])}{symbol}{noun}"
        elif style == "Professional":
            username = f"{base_name}{symbol}{adj}"
        else:
            username = f"{adj}{interest_fragment}{symbol}{noun}"
        
        if use_leetspeak:
            username = apply_leetspeak(username)
        
        usernames.append(username + number)
    
    result_var.set("\n".join(usernames))

def copy_to_clipboard():
    generated_usernames = result_var.get()
    if generated_usernames:
        root.clipboard_clear()
        root.clipboard_append(generated_usernames)
        root.update()
        messagebox.showinfo("Copied!", "Usernames copied to clipboard.")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Username Generator")
root.geometry("400x450")

# Labels and Input Fields
tk.Label(root, text="Enter initials or name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter interests (optional):").pack()
interest_entry = tk.Entry(root)
interest_entry.pack()

# Style Selection
style_var = tk.StringVar(value="Cool")
tk.Label(root, text="Select style:").pack()
tk.Radiobutton(root, text="Cool", variable=style_var, value="Cool").pack()
tk.Radiobutton(root, text="Funny", variable=style_var, value="Funny").pack()
tk.Radiobutton(root, text="Mysterious", variable=style_var, value="Mysterious").pack()
tk.Radiobutton(root, text="Professional", variable=style_var, value="Professional").pack()

# Customization Options
num_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()
leet_var = tk.BooleanVar()
tk.Checkbutton(root, text="Add Numbers", variable=num_var).pack()
tk.Checkbutton(root, text="Add Symbols", variable=symbol_var).pack()
tk.Checkbutton(root, text="Use Leetspeak", variable=leet_var).pack()

# Generate Button
tk.Button(root, text="Generate Usernames", command=generate_usernames).pack()

# Display Results
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify="left")
result_label.pack()

# Copy to Clipboard Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
