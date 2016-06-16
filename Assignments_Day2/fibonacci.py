# '''
# '''how to implement Fibonacci gotten from python docs using recursion'''
def fibo(n):
	num_list = []
	a, b = 0, 1
	while b < n:
		num_list.append(b)
		a,b = b, a + b
	return num_list
	

print(fibo(10))