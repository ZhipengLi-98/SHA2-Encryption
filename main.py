import SHA256

if __name__ == "__main__":
    cryptor = SHA256.SHA256()
    print(cryptor.encrypt("a".encode("utf-8")))