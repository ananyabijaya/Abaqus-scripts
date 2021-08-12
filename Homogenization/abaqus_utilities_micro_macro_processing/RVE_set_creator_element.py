#Create sets of RVE's. The result will be homogenized on these sets
# This is a custom code. Need to be edited as per the geometry.

w_rve = 0.001 # mm
h_rve = 0.001 # mm
tol = w_rve/10000
l = 1
for i in range(20):
	for j in range(10):
		x_min_bbox = i* .001 - tol
		y_min_bbox = j * .001 - tol
		x_max_bbox = (i+1)* 0.001 + tol
		y_max_bbox = (j+1)* 0.001 + tol
		set_elements=mdb.models['Model-1'].parts['Part-1'].elements.getByBoundingBox(xMin=x_min_bbox, yMin=y_min_bbox, xMax=x_max_bbox, yMax=y_max_bbox)
		mdb.models['Model-1'].parts['Part-1'].Set(elements=set_elements, name = "RVE"+str(l) ) 
		l = l+1