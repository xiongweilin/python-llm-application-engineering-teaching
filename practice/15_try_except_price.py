try:
    raise ValueError("invalid price")
except ValueError:
    print("price handled")

print("finished")