# # def Factorial(n, m):
# #   fact_n = 1
# #   fact_m = 1
# #   for i in range(1, n+1):
# #     fact_n *= i
# #   for j in range(1, m+1):
# #     fact_m *= j
# #   return fact_n // fact_m

# # n = 5
# # m = 2

# # result = Factorial(n, m)
# # print(result)

# def Factorial(n, m):
#   fact_n = 1
#   fact_m = 1
#   for i in range(1, n+1):
#     fact_n *= i
#   for j in range(1, m+1):
#     fact_m *= j
#   return fact_n // fact_m

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

# result = Factorial(n, m)
# print(result)

def calc(expr):
    result = eval(expr.replace('/', '//')) 
    result = int(result)
    return result

expr = input("Enter the expression: ")
print("Output:", calc(expr))

def custom_input():
    n = int(input())  
    expr = input()  
    result = eval(expr.replace('/', '//'))  
    result = int(result) 
    print("Output:", result)

custom_input()