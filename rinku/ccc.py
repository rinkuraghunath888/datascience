w=[2, 3.0,4.3,"hello world", 5, 4.3]
x=[]
y=[]
z=[]

for i in w:
    if type(i)==int:
        x.append(i)
    elif type(i)==float:
        y.append(i)
    elif type(i)==str:
        z.append(i)
print(x)
print(y)
print(z)

# mul_12=[]
# for i in range(1,121):
#     if i % 12==0:
#         mul_12.append(i)
# print(mul_12)
#
# mul_14=[]
# for i in mul_12:
#     i=i+2
#     mul_14.append(i)
#
# print(mul_14)