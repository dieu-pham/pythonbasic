
n = int(input("nhập số nguyên n: "))
i = n//4096
if(n % 4096 == 0):
    print("dung lượng của file là: ", i*4, "Kb")
else:
    print("dung lượng của file là:", (i+1)*4, "Kb" )