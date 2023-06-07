a=int(input("Enter the number of rows :"))
for i in range(a):
  print(" "*(a-i),end="")
  print(" ".join(map(str,str(11**i))))
