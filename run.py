import SHA256
import SHA512
import time

if __name__ == "__main__":
    cryptor = SHA256.SHA256()
    # cryptor = SHA512.SHA512()
    ans = []
    with open("1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\n")[0]
            start = time.time()
            cryptor.encrypt(line.encode("utf-8"))
            end = time.time()
            print(end - start)
            ans.append(str(end - start) + "\n")
    with open("1_256.txt", "w") as f:
        f.writelines(ans)