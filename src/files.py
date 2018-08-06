from os import path, walk


def find_matches(cwd, vsrc):
    matches = {}
    for root, dirs, files in walk(cwd):
        for file in files:
            if file.endswith(vsrc):
                match = path.join(root, file)
                size = path.getsize(match)
                matches[match] = size
    return matches


def get_status(matches):
    count = 0
    total = 0
    for path, size in matches.items():
        count += 1
        total += size
    return count, total
