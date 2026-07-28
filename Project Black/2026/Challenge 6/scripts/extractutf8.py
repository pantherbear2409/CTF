def file_to_binary(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    row1 = []
    for char in text:
        if char.isupper():
            row1.append("1")
        elif char.islower():
            row1.append("0")
    return "".join(row1)

def bits_to_bytes(bitstring):
    bitstring = bitstring[:len(bitstring) - (len(bitstring) % 8)]

    return bytes(
        int(bitstring[i:i+8], 2)
        for i in range(0, len(bitstring), 8)
    )

if __name__ == "__main__":
    input_file = "challenge6.txt"

    r1 = file_to_binary(input_file)

    b1 = bits_to_bytes(r1)

    print("\n[ROW 1 RAW BYTES]\n", b1[:100])

    try:
        print("\nROW 1 UTF-8:\n", b1.decode())
    except:
        print("\nROW 1 is NOT UTF-8 text")

    with open("row1.bin", "wb") as f:
        f.write(b1)
