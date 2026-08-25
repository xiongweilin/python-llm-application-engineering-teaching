temperature = 18
target_temperature = 20

def needs_heating(current_temperature, target):
    if current_temperature < target:
        return True

    return False

heating_needed = needs_heating(temperature, target_temperature)

print(heating_needed)