# small utilities, no deps

def flatten(xs):
    return [y for x in xs for y in x]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

if __name__ == "__main__":
    print(clamp(6, 0, 25))
