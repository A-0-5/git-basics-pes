languages = {
    "C++": {
        "philosophy": "Trust the programmer.",
        "vibe": "Manual transmission sports car.",
        "secret_power": "Deterministic memory management via RAII.",
        "catchphrase": "With great power comes great responsibility (and segmentation faults)."
    },
    "Python": {
        "philosophy": "Beautiful is better than ugly.",
        "vibe": "Self-driving luxury electric car.",
        "secret_power": "List comprehensions and 'batteries included' library.",
        "catchphrase": "Life is short, you need Python."
    }
}

for lang, traits in languages.items():
    print(f"--- {lang} ---")
    for key, value in traits.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()