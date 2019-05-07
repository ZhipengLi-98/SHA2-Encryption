import example

if __name__ == "__main__":
    print(example.sha512('a'.encode('utf-8')).hex())
    for i in example.K[64]:
        print(hex(i) + ",")

