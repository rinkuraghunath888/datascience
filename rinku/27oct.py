# n1=[10,20,30,4,2,7,8]
# for i in n1:
#     new=[]
#     result=((i*i)+100)/3
#     new.append(result)
# print(new)

# n1=[10,20,30,4,2,7,8]
#
# def calc(num):
#     val=((num*num)+100)/3
#     return val
#
# res_list=[]
# for i in n1:
#     val=calc(i)
#     res_list.append(val)
# print(res_list)

# n1=[10,20,30,4,2,7,8]
#
# def calc(num):
#     val=((num*num)+100)/3
#     return val
#
# res=tuple(map(calc,n1))
# print(res)
#
# list=['rinku','rahul','reena','raghu']
# def calc(name):
#     return len(name)
# res=tuple(map(calc))

def find_fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*find_fact(num-1)

print(find_fact(3))
    