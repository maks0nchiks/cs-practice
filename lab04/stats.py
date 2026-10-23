def parse_record(line: str) -> dict:
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Invalid record")

    city, temp, date = parts
    city = city.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Empty city or date")

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Invalid temperature")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }