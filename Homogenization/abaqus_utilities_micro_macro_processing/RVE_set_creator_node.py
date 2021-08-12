#Create sets of RVE's. The result will be homogenized on these sets
# This is a custom code. Need to be edited as per the geometry.


# abaqus command to select nodes and  elements by actual number rather than mask
session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

extreme_nodes =  mdb.models['Model-1'].parts['geometry_creation_test_centered'].nodes.getBoundingBox()
bottom_left = extreme_nodes["low"]
top_right = extreme_nodes["high"]

tol = top_right[0]/10**6
# create set : "boundary_nodes" ; taylor boundary condition is defined on this
nodes_left_bd=mdb.models['Model-1'].parts['geometry_creation_test_centered'].nodes.getByBoundingBox(xMin=bottom_left[0], yMin=bottom_left[1], xMax=bottom_left[0]+tol, yMax=top_right[1])

nodes_right_bd=mdb.models['Model-1'].parts['geometry_creation_test_centered'].nodes.getByBoundingBox(xMin=top_right[0] - tol, yMin=bottom_left[1], xMax=top_right[0], yMax=top_right[1])

nodes_top_bd=mdb.models['Model-1'].parts['geometry_creation_test_centered'].nodes.getByBoundingBox(xMin=bottom_left[0], yMin=top_right[1] - tol, xMax=top_right[0], yMax=top_right[1])

nodes_bottom_bd=mdb.models['Model-1'].parts['geometry_creation_test_centered'].nodes.getByBoundingBox(xMin=bottom_left[0], yMin=bottom_left[1] - tol, xMax=top_right[0]+tol, yMax=bottom_left[1])

mdb.models['Model-1'].parts['geometry_creation_test_centered'].Set(nodes = (
												nodes_left_bd,
												nodes_right_bd,
												nodes_top_bd,
												nodes_bottom_bd),
												 name = "boundary_nodes1") 
