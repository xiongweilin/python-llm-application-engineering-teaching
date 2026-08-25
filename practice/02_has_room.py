attempt = 5
max_attempts = 5

def has_room(current_attempt, limit):
    if current_attempt < limit:
        return True

    return False

available = has_room(attempt, max_attempts)

print(available)