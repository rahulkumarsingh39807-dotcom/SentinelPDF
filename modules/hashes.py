import hashlib

def calculate_hashes(file_path):
    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256()
    }

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            for h in hashes.values():
                h.update(chunk)

    return {
        "md5": hashes["md5"].hexdigest(),
        "sha1": hashes["sha1"].hexdigest(),
        "sha256": hashes["sha256"].hexdigest()
    }