def recfact(n):
    if n==1:return 1
    else:return(n*recfact(n-1))
num=int(input("Enter a number"))
if num>=1:
 print("factorial of a number",recfact(num))
