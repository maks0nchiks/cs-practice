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