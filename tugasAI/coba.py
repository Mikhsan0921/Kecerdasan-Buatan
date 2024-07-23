# Membership functions
def cold_water(x):
    if x <= 20:
        return 1
    elif x > 20 and x <= 30:
        return (30 - x) / 10
    else:
        return 0

def moderate_water(x):
    if x <= 20:
        return 0
    elif x > 20 and x <= 40:
        return (x - 20) / 20
    elif x > 40 and x <= 60:
        return (60 - x) / 20
    else:
        return 0

def hot_water(x):
    if x <= 40:
        return 0
    elif x > 40 and x <= 60:
        return (x - 40) / 20
    else:
        return 1

def low_thirst(x):
    if x <= 30:
        return 1
    elif x > 30 and x <= 50:
        return (50 - x) / 20
    else:
        return 0

def moderate_thirst(x):
    if x <= 30:
        return 0
    elif x > 30 and x <= 50:
        return (x - 30) / 20
    elif x > 50 and x <= 70:
        return (70 - x) / 20
    else:
        return 0

def high_thirst(x):
    if x <= 50:
        return 0
    elif x > 50 and x <= 70:
        return (x - 50) / 20
    else:
        return 1

# Fuzzy inference rules
def infer_rules(temperature, thirst):
    rules = [
        # Cold water
        (cold_water, low_thirst, 1),
        (cold_water, moderate_thirst, 0.5),
        (cold_water, high_thirst, 0.1),

        # Moderate temperature water
        (moderate_water, low_thirst, 0.1),
        (moderate_water, moderate_thirst, 1),
        (moderate_water, high_thirst, 0.5),

        # Hot water
        (hot_water, low_thirst, 0.1),
        (hot_water, moderate_thirst, 0.5),
        (hot_water, high_thirst, 1),
    ]

    output = 0
    for rule in rules:
        membership = min(rule[0](temperature), rule[1](thirst))
        output = max(output, membership * rule[2])

    return output

def dispense_water(temperature, thirst):
    water_level = infer_rules(temperature, thirst)
    return water_level

if __name__ == "__main__":
    temperature = float(input("Masukkan suhu air (0-100): "))
    thirst_level = float(input("Masukkan tingkat kehausan (0-100): "))

    water_level = dispense_water(temperature, thirst_level)
    print("Level air yang didispense:", water_level)
