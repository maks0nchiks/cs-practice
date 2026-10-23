import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

nonempty_lines = [line for line in lines if line.strip()]
skipped = len(nonempty_lines) - len(records)

averages = average_by_city(records)
city = warmest_city(records)

print(len(records))
print(skipped)
print(f"{averages.get(city, 0.0):.1f}")