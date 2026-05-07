# print all even numbers from 1 to 10
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=" ")

# Q.2 sum of numbers
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(a))
# n=input("Enter your number: ")
# sum=0
# for i in range(1, int(n)+1):
#     sum+=i
# print(sum)


# Q.3 Reverse a string
# str=input("Enter your string: ")
# print(str[::-1])

# Reverse Each Word Separately
# str=input("Enter your string: ")
# words=str.split()
# for word in words:
#     print(word[::-1], end=" ")

# Reverse Word Positions
str=input("Enter your string: ")
words=str.split()

print(words[::-1])

word=" ".join