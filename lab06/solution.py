
def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    return min(paths, key=lambda p: (-p.count("/"), p)) if paths else ""
