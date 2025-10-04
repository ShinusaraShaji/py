vow=['a','e','i','o','u','A','E','I','O','U']
s=input("Enter the string:")
count=0
for i in range(len(s)):
    if s[i] in vow:
     count += 1
print("The number of vowels is:",count)
