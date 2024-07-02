# PYnative29@#8496




# t="PYnative29@#8496"
# sum=0
# count=0
# for char in t:
#     if char.isdigit():
#         count+=1
#         s=int(char)
#         sum+=s
# print(sum,sum/count)
# change code

t=input()
total=0
count=0
for char in t:
    if char.isdigit():
        count+=1
        s=int(char)
        total+=s
average=total/count
print("Sum is: {} Average is {}".format(total, average))