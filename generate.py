import random


def convert(s):
    ans = 0
    pow = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            ans += pow
        pow *= 2
    return hex(ans)


def generate(num):
    ans = ""
    temp = ""
    for i in range(num + 1):
        if i % 500000 == 0:
            print(float(i) / float(num))
        if i % 4 == 0:
            ans += convert(temp)[2]
            temp = ""
        if random.random() > 0.5:
            temp += "1"
        else:
            temp += "0"
    ans = ans[1:] + "\n"
    return ans


if __name__ == "__main__":
    ans = []
    num = (1 << 23)
    for i in range(10):
        ans.append(generate(num))
        print(i)
    with open("1.txt", "w") as f:
        f.writelines(ans)