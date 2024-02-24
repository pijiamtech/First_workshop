def f(x):
    return x**2-4

def df(x):
    return 2*x

# def display(x):
#     print(f'f({x}) = {f_x}')
#     print(f'df({x}) = {df_x}')


# x=10
# f_x = f(x)
# df_x = df(x)
# 
# for i in range(20):
#     if df(x) == 0:
#         print('df(x) is zero')
#         break
#     x = x - f(x)/df(x)
#     print(f'at i = {i} x = {x} f(x) = {f(x)}')

# display(x)


from newton import Newton
    
x=10
f_x = f(x)
df_x = df(x)

obj = Newton(f, df)
obj.solve(x, 1e-10, 100)