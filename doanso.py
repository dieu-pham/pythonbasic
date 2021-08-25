import random
c = 0
n = random.randint(1, 10) # chon so ngay nhien tu 1 den 10
while True:
    if c==3:
        print("Bạn đã thua cuộc, số đúng là: ", n)
        break
    a = int(input("Nhập số: "))
    if  a==n:
        print("Chúc mừng bạn đã chiến thắng")
        break
    else:
        c = c+1
        if a>n:
            print("Bạn đã đoán sai, hãy đoán số nhỏ hơn")
        else:
            print("Bạn đã đoán sai, hãy đoán số lớn hơn")
