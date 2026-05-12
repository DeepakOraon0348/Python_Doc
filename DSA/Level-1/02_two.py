# Q.4: Count Vowels====================
# def count_vowels(str):
#     count=0
#     for i in str:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count;

# str="programming"
# print(count_vowels(str))

def check_odd(a):
    if a%2==0:
        print(f"{a} is even.")
    else:
        print(f"{a} is odd.")

check_odd(2)
check_odd(3)