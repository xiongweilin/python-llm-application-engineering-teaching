try:
    raise ValueError("invalid value")
except ValueError:
    print("caught")

print("continued")