# List of tupled items
from termios import FIOASYNC


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Use a list comprehension to map by prices
prices = [item[1] for item in items]

# Use a list comprehension to filter by prices
filtered = [item for item in items if item[1] >= 10]

print(filtered)
