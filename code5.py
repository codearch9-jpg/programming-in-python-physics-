a = [1,2]
sum = 0 
while sum<4000000:
    sum = a[-2]+a[-1]
    a.append(sum)
    total = 0 
    for i in a:
        if i%2 == 0:
            total += i
print("The sum of a1 even numbers in fibonaci series till 4000000 is :", total)
