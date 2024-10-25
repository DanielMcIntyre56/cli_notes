from hashlib import sha256


def hash_string(string: str) -> str:
    """
    Hashes a string using SHA-256.
    Returns the hash as hexadecimal.
    """
    _hash = sha256(string.encode('utf-8')).hexdigest()
    return _hash
