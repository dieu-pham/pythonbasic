
# def print_message(message, count):
#     for i in range(1, count + 1):
#         print(message)
#
#
# print_message("Xin chào", 5)
# print_message("Ciao", 3)

# def sum(start, end):
#     total = 0
#     for i in range(1, end + 1):
#         total += i
#     return total # đưa giá trị ra bên ngoài hàm
#
# print("tổng các số từ 1 đến 10: " + str(sum(1, 10)))
# print("tổng các số từ 5 đến 15: " + str(sum(5, 15)))

#1 đầu ra của hàm này là đầu vào của hàm khác
#2 giữ lại type của biến bên trong hàm
#3 tăng khả năng tái sử dụng

def sum(start, end):
    global total
    for i in range(1, end + 1):
        total += i

total = 0
sum(1,10)
print(total)

# Stack Overflow
