Create abaqus model:

1. Model the lattice/composite 
2. Mesh boundaries in a periodic manner. This will take some trial and error (can't always use structured mesh)
3. Run EasyPBC to create node sets. It uses the node number as the node set name.
4. Run "periodic_node_pair_list.py" this create "node_coord.csv" and write the boundary nodes.
5. Copy the node list from csv to "Create_PBC_equations.py" and run it abaqus to generate constraint equations. Verify the corner node description, 'c2, c5, c6' are created by easyPBC. However, in lattice RVE with no corner nodes we need to define p1, p2, p3, p4.
		c2   (Abaqus Node): Top-left node
		c5   (Abaqus Node): Bottom-Right node
		c6   (Abaqus Node): Bottom-Left node

		p1   (Abaqus Node):  Bottom most node on the back (left) boundary
		p2   (Abaqus Node):  Bottom most node on the front (right) boundary
		p3   (Abaqus Node):  Left most node on the bottom boundary	
		p4   (Abaqus Node):  Left most node on the top boundary 

6. Define displacement field 
	Disp_x = F11 * X + F12 * Y
	Disp_y = F21 * X + F22 * Y
7. Define prescribed boundary using the defined displacement field, for the corner nodes in abaqus.
8. The RVE can be analyzed now.

For getting Material tangent matrix:
1. Use "add_perturb_step_to_cae.py" file to generate linear analysis steps and the related fields and boundary conditions

field_val = [
['Disp_X-Col-1', '1*X + 0*Y'],
['Disp_Y-Col-1', '0*X + 0*Y'],
['Disp_X-Col-2', '0*X + 0*Y'],
['Disp_Y-Col-2', '0*X + 1*Y'],
['Disp_X-Col-3', '0*X + 0.5*Y'],
['Disp_Y-Col-3', '0.5*X + 0*Y'],
]
Note that the third column for the CMAT is defined 2*epsilon12 or 
gamma12 = epsilon12 + epsilon21 (see barbero)
In DNN to get the derivative with respect to epsilon12 we need to multiply 2 to the third column of obtained CMAT. (See Research Notebook 11)
