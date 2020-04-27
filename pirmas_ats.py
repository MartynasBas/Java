import numpy as np
from sympy import *

def function1():
	print(np.linspace(-1.3, 2.5, 64))

def function2(n):
	a = [1, 2, 3]
	for i in range(n-1):
		a = np.append(a, [1, 2, 3])
	print(a)
	#print(type(a))
	#for i in range(n):
		#a = np.append(a, [1, 2, 3])
	#print(list(map(int, a.tolist())))
	#a = []
	#np.full(n, [1, 2, 3], dtype = np.int)
	#print(a)

def function3():
	print(np.arange(1,20,2))

def function4():
	a = np.ones((10,10))
	a[1:-1, 1:-1] = 0
	print(a)

def function5():
	a = np.zeros((10, 10))
	a[::2, 1::2] = 1
	a[1::2, ::2] = 1
	print(a)

def function6(n):
	array = np.array(range(0,n*n))
	for x in array:
		array[x]=(x%n)+(x/n)
	print(array.reshape((n,n)))


def function7():
	a = np.random.rand(3,5)
	print(np.sum(a))
	print(np.sum(a,0))
	print(np.sum(a,1))

def function8():
	a = np.random.rand(5,5)
	print(a)
	print(a[a[:,1].argsort()])

def function9(n, x):
	a = np.random.rand(n,n)
	print(a)
	a[::-1, ::-1] = a[::1, ::1]
	print(a)
	x = np.matrix(x)
	#inverseMatrix = matrix.I
	print(x)
	print(x.getI())

def function10():
	w, v = np.linalg.eig(np.array([[2, 1], [3, 1]]))
	print("Values\n", w,"\nVectors\n", v)

def function11():
	x = Symbol('x')
	f = 2*x**2+3
	#print(type(f))
	f_prime = f.diff(x)
	print(f_prime)

def function12(a, b):
	x = Symbol('x')
	f = 2*x**2+3
	integrate(f, x)
	integrate(f, (x, a, b))
	print("Indefinite: ", integrate(f, x))
	print("Definite: ", integrate(f, (x, a, b)))


#function1()
#function2(3)
#function3()
#function4()
#function5()
#function6(5)
#function7()
#function8()
#function9(5, [[1,2],[3,4]])
#function10()
#function11()
#function12(0, 1)

