# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import numpy as np
import os

from math import cos, sin, radians, atan, pi

session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

# K1_amp = 1e7
crack_width = 3e-3
TOL = 1e-6
TOL_y = 3e-3
Lx = 0.3
Ly = 0.3
rho_bar = 0.1
lattice_type = "triangle"
name_tag = "_"+str(rho_bar)[2:]
job_name_gen = "triangle_"
job_name = job_name_gen + name_tag
##############################################################################
mdb.models['Model-1'].materials['silicon_carbide'].elastic.setValues(
    dependencies=1, table=((418000000000.0, 0.16, 0.0), (418000000000.0, 0.16, 
    0.9), (418000000.0, 0.16, 0.91), (418000000.0, 0.16, 1.0)))
mdb.models['Model-1'].materials['silicon_carbide'].UserDefinedField()
mdb.models['Model-1'].materials['silicon_carbide'].Depvar(n=1)
mdb.models['Model-1'].steps['Step-1'].setValues(initialInc=0.001, maxInc=0.001,
    maxNumInc=1000, minInc=0.001)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'E', 'U', 'RF', 'RM', 'CF', 'SDV', 'FV', 'STATUS'))
###############################################################################
part_name = "triangular_lattice_15_deg"
extreme_nodes = (
	mdb.models["Model-1"]
	.parts[part_name]
	.nodes.getBoundingBox()
)
bottom_left = extreme_nodes["low"]
top_right = extreme_nodes["high"]

xMin = bottom_left[0]
yMin = bottom_left[1]
xMax = top_right[0]
yMax = top_right[1]

###############################################################################
coords = [
	[-Lx / 2, Ly / 2],
	[Lx / 2, Ly / 2],
	[-Lx / 2, -Ly / 2],
	[Lx / 2, -Ly / 2],
]

bd_box_upper = {
	"xMin_1": coords[0][0],
	"xMax_1": coords[1][0],
	"yMin_1": coords[0][1],
	"yMax_1": coords[1][1],
}
bd_box_lower = {
	"xMin_1": coords[2][0],
	"xMax_1": coords[3][0],
	"yMin_1": coords[2][1],
	"yMax_1": coords[3][1],
}

bd_boxes = [bd_box_upper, bd_box_lower]
set_name = ["top_face", "bottom_face"]

mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (1.0, 5e-4)), name=
    'Inc_disp', smooth=SOLVER_DEFAULT, timeSpan=STEP)

# Ux_BC = ['']
Uy_BC = [1, 0]
for idx, bd_box in enumerate(bd_boxes):
	X1, Y1 = bd_box["xMin_1"], bd_box["yMin_1"]
	X2, Y2 = bd_box["xMax_1"], bd_box["yMax_1"]
	# create set : "boundary_nodes" ; taylor boundary condition is defined on this
	node_list_1 = (
		mdb.models["Model-1"]
		.parts[part_name]
		.nodes.getByBoundingBox(
			xMin=X1 - TOL, yMin=Y1 - TOL_y, xMax=X2 + TOL, yMax=Y2 + TOL_y)
	)
	mdb.models["Model-1"].parts[part_name].Set(
		nodes=(node_list_1,), name=set_name[idx]
	)
	mdb.models['Model-1'].rootAssembly.regenerate()
	# part_name+"-1."+
	mdb.models["Model-1"].DisplacementBC(
		amplitude="Inc_disp",
		createStepName="Step-1",
		distributionType=UNIFORM,
		fieldName= '',
		fixed=OFF,
		localCsys=None,
		name="BC_" + set_name[idx],
		region=mdb.models["Model-1"]
		.rootAssembly.instances[part_name+"-1"]
		.sets[set_name[idx]],
		u1=UNSET,
		u2=Uy_BC[idx],
		ur3=UNSET,
	)
	# mdb.models["Model-1"].DisplacementBC(
	# 	amplitude="Inc_disp",
	# 	createStepName="Step-1",
	# 	distributionType=FIELD,
	# 	fieldName="omega_K1_" + set_name[idx],
	# 	fixed=OFF,
	# 	localCsys=None,
	# 	name="BC_omega_" + set_name[idx],
	# 	region=mdb.models["Model-1"]
	# 	.rootAssembly.instances[part_name+"-1"]
	# 	.sets[set_name[idx]],
	# 	u1=UNSET,
	# 	u2=UNSET,
	# 	ur3=1,
	# )

mdb.models['Model-1'].rootAssembly.regenerate()

mdb.Job(name=job_name, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine=r"E:\Anisotropic_Fracture_Behaviour_of_Lattices\G_1C_Calculation\Triangular_lattice_Gc_det_Dif_Orientations\Crack_propagation_and_Gc_calc\damage_usdfld_MOD.for", 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
# mdb.jobs[job_name].writeInput(consistencyChecking=OFF)
mdb.jobs[job_name].submit(consistencyChecking=OFF)
