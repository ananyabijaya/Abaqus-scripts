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
# file = path+'//F_M_and_E_gl_List.npz'
# F_M_List = np.load(file)["F_M_List"]


# small_strain = np.array([
# 	[],
# 	[],
# 	])
# load11 = small_strain[0,0]
# load12 = small_strain[0,1] 
# load21 = small_strain[1,0]
# load22 = small_strain[1,1]
# itr_expression = str(load11)+"*X + ("+str(load12)+")*Y"
# mdb.models['Model-1'].analyticalFields['Disp_X'].setValues(
# 	expression=itr_expression)
# itr_expression = str(load21)+"*X + ("+str(load22)+")*Y"
# mdb.models['Model-1'].analyticalFields['Disp_Y'].setValues(
# 	expression=itr_expression)



# Create fields:
mdb.models['Model-1'].analyticalFields['Disp_X-Col-1'].setValues(expression=    '1*X + 0 *Y')
mdb.models['Model-1'].analyticalFields['Disp_Y-Col-1'].setValues(expression=    '0*X + 1*Y')
......................................???????? (add code)



mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-1', previous=  'Step-1')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-2', previous=    'Step-Col-1')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-3', previous=   'Step-Col-2')



mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-1_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-1_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c2_top_left_col-1_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-1_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-1_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c2_top_left_col-1_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)



mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-2_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-2_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c2_top_left_col-2_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-2_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-2_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c2_top_left_col-2_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)




mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-3_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-3_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c2_top_left_col-3_X', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-3_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-3_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c2_top_left_col-3_Y', region=
    mdb.models['Model-1'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)



job_name = str(i)
# job_name = job_name.replace(".","__")
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
multiprocessingMode=DEFAULT, name=job_name, nodalOutputPrecision=SINGLE, 
numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='',type= ANALYSIS, waitHours=0, 
waitMinutes=0)
mdb.jobs[job_name].writeInput()
mdb.jobs[job_name].submit(consistencyChecking=OFF)

# del mdb.jobs[job_name]

# mdb.JobFromInputFile(activateLoadBalancing=False, atTime=None, 
# explicitPrecision=SINGLE, getMemoryFromAnalysis=True, inputFileName=
# job_name+".inp", memory=90, memoryUnits=PERCENTAGE, multiprocessingMode=DEFAULT, name=
# job_name, nodalOutputPrecision=SINGLE, numCpus=2, 
# numDomains=2, parallelizationMethodExplicit=DOMAIN, queue=None, 
# resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine=
# 'E:\\NN_Research\\UMAT_St_Venant.for', waitHours=0, 
# waitMinutes=0)
# mdb.jobs[job_name].submit(consistencyChecking=OFF)

