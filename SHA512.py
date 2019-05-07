from utils512 import *

class SHA512:
    def rotate_right(self, num, n):
        return (num >> n) | (num << 64 - n)

    def big_sigma0(self, num):
        return self.rotate_right(num, 28) ^ self.rotate_right(num, 34) ^ self.rotate_right(num, 39)

    def big_sigma1(self, num):
        return self.rotate_right(num, 14) ^ self.rotate_right(num, 18) ^ self.rotate_right(num, 41)

    def small_sigma0(self, num):
        return self.rotate_right(num, 1) ^ self.rotate_right(num, 8) ^ (num >> 7)

    def small_sigma1(self, num):
        return self.rotate_right(num, 19) ^ self.rotate_right(num, 61) ^ (num >> 6)

    def ch(self, x, y, z):
        return (x & y) ^ (~x & z)

    def ma(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def preprocess(self, msg):
        length = len(msg)
        msg += b'\x80'
        msg += b'\x00' * ((111 - length) % 128)
        msg += (length * 8).to_bytes(16, byteorder="big")
        ans = []
        for i in range(len(msg) // 128):
            ans.append([])
            for j in range(16):
                temp = i * 128 + j * 8
                ans[i].append(int.from_bytes(msg[temp: temp + 8], "big"))
        return ans

    def encrypt(self, msg):
        H = IV.copy()
        con = 1 << 64
        for w in self.preprocess(msg):
            a, b, c, d, e, f, g, h = H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]
            for i in range(80):
                if i > 15:
                    w.append((self.small_sigma1(w[i - 2]) +
                              w[i - 7] +
                              self.small_sigma0(w[i - 15]) +
                              w[i - 16]) % con)
                t1 = (h + self.big_sigma1(e) + self.ch(e, f, g) + K[i] + w[i]) % con
                t2 = (self.big_sigma0(a) + self.ma(a, b, c)) % con
                h = g
                g = f
                f = e
                e = (d + t1) % con
                d = c
                c = b
                b = a
                a = (t1 + t2) % con
            temp = zip([a, b, c, d, e, f, g, h], H)
            H = [(i[0] + i[1]) % con for i in temp]
        ans = ""
        for i in H:
            ans += str(hex(i))[2:]
        return ans