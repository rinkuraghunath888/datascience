# def find_sum(num):
#     if num==0:
#         return 0
#     elif num==1:


# def sum(n1):
#     if n1<=1:
#         return n1
#     else:
#         return n1 +sum(n1-1)
# print(sum(5))

# def sum(num):
#     if num==0:
#         return 0
#     else:
#         return num + sum(num - 1)

# Python program to display all the prime numbers within an interval

# lower = 1
# upper = 100
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#
# print(prime nmbrs between )

def find_prime(r1,r2):
    primes=[]
    if r1>=r2:
        print("not valid range")
    else:
        for num in range(r1,r2):
            for j in range(2,int(num/2)+1):
                if num%j==0:
                    break
            else:
                primes.append(num)

    return primes

print(find_prime(5,100))