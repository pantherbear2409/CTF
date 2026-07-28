#!/usr/bin/env python3
import base64
import re

with open('challenge5.txt', 'rb') as f:
    raw_data = f.read()

# Convert tabs/spaces to binary (tab=1, space=0)
binary = ''.join('1' if b == 0x09 else '0' for b in raw_data)

# Convert to bytes
bytes_data = bytes(int(binary[i:i + 8], 2) for i in range(0, len(binary) - 7, 8))

# Try to decode as base64
try:
    # The bytes look like base64 already
    b64_string = bytes_data.decode('ascii')

    # Remove any non-base64 characters
    b64_clean = re.sub(r'[^A-Za-z0-9+/=]', '', b64_string)

    print(f"Base64 length: {len(b64_clean)}")
    print(f"First 100 chars: {b64_clean[:100]}")

    # Decode base64
    decoded = base64.b64decode(b64_clean)

    print(f"\nDecoded size: {len(decoded)} bytes")

    # Check if it's an image
    if decoded[:4] == b'\x89PNG':
        print("It's a PNG image!")
        with open('flag.png', 'wb') as f:
            f.write(decoded)
        print("Saved as flag.png")
    elif decoded[:3] == b'\xff\xd8\xff':
        print("It's a JPEG image!")
        with open('flag.jpg', 'wb') as f:
            f.write(decoded)
        print("Saved as flag.jpg")
    elif decoded[:4] == b'GIF8':
        print("It's a GIF image!")
        with open('flag.gif', 'wb') as f:
            f.write(decoded)
        print("Saved as flag.gif")
    else:
        # Try to open as text
        try:
            text = decoded.decode('utf-8')
            print(f"Decoded text:\n{text[:500]}")
        except:
            print(f"First 100 bytes: {decoded[:100].hex()}")

except Exception as e:
    print(f"Error: {e}")
