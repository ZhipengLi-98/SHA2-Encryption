import SHA256
import SHA512

if __name__ == "__main__":
    cryptor = SHA512.SHA512()
    print(cryptor.encrypt(("").encode("utf-8")))