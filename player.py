player = {
    "name": "",
    "stats": {
        "identity_stability":0,
        "insight":0,
        "willpower":0,
        "empathy":0,
        "curiosity":0,
        "corruption":0    
    },
    "flags": {
        # Placeholder for adding flags later
        # e.g. "refused_name_entry": False
    },
}

def update_stat(player, stat_name, amount):
    stats = player['stats']

    if stat_name in stats:
        stats[stat_name] += amount
    
    if stats[stat_name] < 0:
        stats[stat_name] = 0
