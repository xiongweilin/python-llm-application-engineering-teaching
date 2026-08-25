attempt = 2
max_attempts = 4

def can_retry(current_attempt, limit):
    if current_attempt < limit:
        return True

    return False

allowed = can_retry(attempt, max_attempts)

print(allowed)