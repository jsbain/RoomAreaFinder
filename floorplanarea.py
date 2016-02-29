# coding: utf-8
def polygonArea(X, Y):
	area = 0
	j = len(X) - 1
	for i in range(len(X)):
		area = area + (X[j] + X[i]) * (Y[j] - Y[i])
		j = i
	return abs(area/2)
	
	
def getLineLength(A, B):
	getEndPoints()
	length = ((A[1]-A[0])**2 + (B[1]-B[0])**2)**.5
	return length
	
	
def getPolygonVertices():
# Touch successive vertices, draw lines connecting points, recognize when polygon is closed (or close), return coordinates of vertices
	X = (0, 3, 0)
	Y = (0, 0, 4)
	return X, Y
	
	
def getEndPoints():
# Touch 2 points on image, draw line to confirm, return coordinates
	A = (0, 0)
	B = (0, 4)
	return A, B
	
	
def getscale():
	print "Touch 2 points along a known length"
	A, B = getEndPoints()
	LineLength = getLineLength(A, B)
	scale = input('Enter known length: ')
	return scale/LineLength

a = getscale()
X, Y = getPolygonVertices()
print a * polygonArea(X, Y)

	

