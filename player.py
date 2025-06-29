from stat_feedback import increase_stat_feedback, decrease_stat_feedback

player = {
    "name": "",
    "stats": {
        "identity_stability":2,
        "insight":0,
        "willpower":0,
        "empathy":0,
        "curiosity":0,
        "corruption":0    
    },
    "flags": {
        "discarded_ticket": False,
    },
}

def update_stat(player, stat_name, amount):
    stats = player['stats']

    if stat_name in stats:
        stats[stat_name] += amount
        if stats[stat_name] < 0:
            stats[stat_name] = 0
        
        if amount > 0:
            message = increase_stat_feedback.get(stat_name)
        elif amount < 0:
            message = decrease_stat_feedback.get(stat_name)
             
    return message
