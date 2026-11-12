import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.splitlines()

    if not lines:
        return []

    headers = lines[0].split(',')
    values = lines[1:]

    result = []

    for value in values:
        if not value:
            continue

        index_city = value.split(',')
        record = dict(zip(headers, index_city))
        result.append(record)

    return result


def convert(value: str):
    value = value.strip()

    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None

    for line in lines:
        line = line.split('#')[0].strip()

        if not line:
            continue

        if line.startswith('- '):
            current_list.append(line[2:])

        elif line.endswith(':'):
            key = line[:-1].strip()
            result[key] = []
            current_list = result[key]

        else:
            current_list = None
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            result[key] = convert(value)

    return result