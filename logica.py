def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
        
    return total
     
positive_sum(arr=[11 , -4, 7, 12])

r = positive_sum(arr=[11 , -4, 7, 12])
print(r)

