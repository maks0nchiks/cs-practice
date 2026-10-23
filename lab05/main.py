
from pathlib import Path
from logstats import count_levels, top_errors, format_report

base_dir = Path(__file__).resolve().parent

filename = input().strip()
log_path = base_dir / filename
report_path = base_dir / "report.txt"

with open(log_path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(log_path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

total = sum(counts.values())
error_count = counts.get("ERROR", 0)
broken = counts.get("BROKEN", 0)

print(total)
print(error_count)
print(broken)

report = format_report(counts, errors)

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report)
