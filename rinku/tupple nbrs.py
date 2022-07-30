cE=0
cO=0
num=(1,2,3,4,5,6,7,8,9,10,11)
for i in num:
    if i%2==0:
        cE=cE+1
    else:
        cO=cO+1
print(f"count of even numbr is {cE}")
print(f"count of odd numbers is {cO}")
