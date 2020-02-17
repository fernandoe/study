# Current Points: 88 -> 126

def likes(names):
    total = len(names)
    if total == 0:
        return "no one likes this"
    elif total == 1:
        return f"{names[0]} likes this"
    elif total == 2:
        return f"{' and '.join(names)} like this"
    elif total == 3:
        return f"{', '.join(names[0:2])} and {names[2]} like this"
    else:
        return f"{', '.join(names[0:2])} and {total-2} others like this"
