# -------------------------------------------------------------------------------------------------

def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    # Using the boolean to be used as 1 or 0 when multiplying
    return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"

# -------------------------------------------------------------------------------------------------

def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    # Don't get eaten!
    
    # No time to run, shark appeared in front of you
    if sharkDistance == 0: return "Shark Bait!"
    
    if dolphin:
        sharkSpeed /= 2
    
    ## Let's calculate how long we take to reach the pontoon and see if we can get it before the shark
    deltaYou = pontoonDistance / youSpeed
    deltaShark = (pontoonDistance + sharkDistance) / sharkSpeed
    
    if deltaYou < deltaShark:
        return "Alive!"
    return "Shark Bait!"

# -------------------------------------------------------------------------------------------------

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
        
    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed
    
    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"

# -------------------------------------------------------------------------------------------------

def shark(d1, d2, v1, v2, x):
    return "Alive!" if d1 / v1 < d2 / v2 * (x + 1) else "Shark Bait!"

# -------------------------------------------------------------------------------------------------

def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    if dolphin:
        sharkSpeed /= 2
    return "Alive!" if pontoonDistance / youSpeed <= sharkDistance / sharkSpeed else "Shark Bait!"

# -------------------------------------------------------------------------------------------------
