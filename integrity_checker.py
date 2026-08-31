import hashlib
import json
import os


def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


file = "monitored_file.txt"
hash_file = "hashes.json"


if not os.path.exists(hash_file):

    file_hash = calculate_hash(file)

    data = {
        file: file_hash
    }

    with open(hash_file, "w") as f:
        json.dump(data, f, indent=4)

    print("Baseline hash created.")

else:

    with open(hash_file, "r") as f:
        data = json.load(f)

    original_hash = data[file]
    current_hash = calculate_hash(file)

    print("=" * 50)
    print("       FILE INTEGRITY MONITORING SYSTEM")
    print("=" * 50)

    print("\nFile:", file)
    print("Original Hash:", original_hash)
    print("Current Hash :", current_hash)

    if original_hash == current_hash:
        print("\n[✓] STATUS: FILE INTEGRITY VERIFIED")
        print("[✓] No modification detected.")

    else:
        print("\n[!] SECURITY ALERT")
        print("[!] File modification detected!")
        print("[!] Integrity verification FAILED.")

    print("=" * 50)