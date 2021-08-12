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

path = os.getcwd()
# path = r"E:\NN_Research\Prob_YvonnetPlwholeRVE\TestData"
file = path+'//F_M_and_E_gl_List.npz'
F_M_List = np.load(file)["F_M_List"]

i = 0
for F_M in F_M_List:
	F_M_11, F_M_12, F_M_21, F_M_22 = F_M
	load11 = F_M_11 -1
	load12 = F_M_12
	load21 = F_M_21
	load22 = F_M_22 -1
	itr_expression = str(load11)+"*X + ("+str(load12)+")*Y"
	mdb.models['Model-1'].analyticalFields['Disp_X'].setValues(
		expression=itr_expression)
	itr_expression = str(load21)+"*X + ("+str(load22)+")*Y"
	mdb.models['Model-1'].analyticalFields['Disp_Y'].setValues(
		expression=itr_expression)
	# job_name = "Ex1"+"_"+str(load11)[0:6]+"_"+str(load12)[0:6]+"_"+str(load21)[0:6]+"_"+str(load22)[0:6]
	job_name = str(i)
	# job_name = job_name.replace(".","__")
	mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
	explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
	memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
	multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
	numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='',type= ANALYSIS, userSubroutine=
	'E:\\NN_Research\\UMAT_St_Venant.for', waitHours=0, 
	waitMinutes=0)
	mdb.jobs[job_name].writeInput()
	del mdb.jobs[job_name]
	i = i + 1
	# else:
	# 	pass
	
# mdb.saveAs(
#     pathName='E:/NN_Research/Example1_Hyperelasticity/AbaqusModel/All_Jobs')

i = 0
job_name_wfc = []
for i in range(F_M_List.shape[0]):
	print("File No.:", i)
	# load11, load12, load21, load22 = load
	job_name = str(i)
	print(job_name)
	job_name_wfc.append(job_name)
	mdb.JobFromInputFile(activateLoadBalancing=False, atTime=None, 
	explicitPrecision=SINGLE, getMemoryFromAnalysis=True, inputFileName=
	job_name+".inp", memory=90, memoryUnits=PERCENTAGE, multiprocessingMode=DEFAULT, name=
	job_name, nodalOutputPrecision=SINGLE, numCpus=1, 
	numDomains=8, parallelizationMethodExplicit=DOMAIN, queue=None, 
	resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine=
	'E:\\NN_Research\\UMAT_St_Venant.for', waitHours=0, 
	waitMinutes=0)
	mdb.jobs[job_name].submit(consistencyChecking=OFF)
	i = i + 1		
	if i%6 == 0:
		 mdb.jobs[job_name_wfc[0]].waitForCompletion(600)
		 mdb.jobs[job_name_wfc[1]].waitForCompletion()
		 mdb.jobs[job_name_wfc[2]].waitForCompletion()
		 mdb.jobs[job_name_wfc[3]].waitForCompletion()
		 mdb.jobs[job_name_wfc[4]].waitForCompletion()
		 mdb.jobs[job_name_wfc[5]].waitForCompletion()
		 # mdb.jobs[job_name_wfc[6]].waitForCompletion()
		 # mdb.jobs[job_name_wfc[7]].waitForCompletion()
		 job_name_wfc = []
		 print("one cycle done")
	# else:
	# 	pass
