# first n natural number
def sum_of(n):
	sum = 0
	for i in range(1,n+1):
		sum +=i
	return sum
result1 = sum_of(10)
result2 = sum_of(100)
result3 = sum_of(200)
print("Sum of 10 natural numbers is ",result1)
print("Sum of 100 natural numbers is ",result2)
print("Sum of 200 natural numbers is ",result3)
result = result1 + result2 + result3
print("final answer is ",result)