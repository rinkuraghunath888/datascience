def student_details(name,**subjects):
    print(name)
    sum=0
    for i in subjects:
        print(i,"-",subjects.get(i))
        sum=sum+subjects.get(i)
    print("total marks:",sum)

student_details(name="rinku",physics=60,chemistry=50,maths=56,english=89)
# count=0
# def sample():
#     global count
#     count=count+1
#     print(f"this functn is called{count} times")
#
# sample()
# sample()
# sample()
