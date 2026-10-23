
def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Invalid record")

    time, level, message = parts

    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Invalid level")

    return {
        "time": time,
        "level": level,
        "message": message
    }


def count_levels(lines) -> dict:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue

        level = event["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] != "ERROR":
            continue

        message = event["message"]
        errors[message] = errors.get(message, 0) + 1

    sorted_errors = sorted(
        errors.items(),
        key=lambda item: (-item[1], item[0])
    )

    return [
        [message, count]
        for message, count in sorted_errors[:n]
    ]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"
