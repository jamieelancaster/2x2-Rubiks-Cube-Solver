def read_db(filename):
    results = []

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(25)
            if not chunk:
                break

            state = chunk[:24]      # bytes object
            depth = chunk[24]       # int (0–255)

            results.append((state, depth))

    return results

REVERSE_COLOR_MAP = {
    0: "Y",
    1: "W",
    2: "R",
    3: "O",
    4: "G",
    5: "B"
}

def decode_state(state_bytes):
    return [REVERSE_COLOR_MAP[b] for b in state_bytes]

print(decode_state(read_db("cube_db.bin")))