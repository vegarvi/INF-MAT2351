from numpy import sum,matrix,linalg

def quadLSQ(t,y):
	n = len(t)


	A = matrix([[n, sum(t)],[sum(t), sum(t*t)]])

	b = matrix([[sum(y)],[sum(t*y)]])

	alpha,beta = linalg.solve(A,b)

	return float(alpha),float(beta)

