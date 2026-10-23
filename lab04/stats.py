
def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Invalid record")

    city, temp, date = parts
    city = city.strip()
    temp = temp.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Empty city or date")

    try:
        temp = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError("Invalid temperature")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    return {
        city: round(total[city] / count[city], 1)
        for city in total
    }


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    return min(
        averages,
        key=lambda city: (-averages[city], city)
    )
