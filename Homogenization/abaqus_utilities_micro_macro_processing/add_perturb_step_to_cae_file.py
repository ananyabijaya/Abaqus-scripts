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
# itr_expression = str(load11)+"*X + ("+str(load12)+")*Y"
# mdb.models['Model-1_pos_neg'].analyticalFields['Disp_X'].setValues(
# 	expression=itr_expression)
# itr_expression = str(load21)+"*X + ("+str(load22)+")*Y"
# mdb.models['Model-1_pos_neg'].analyticalFields['Disp_Y'].setValues(
# 	expression=itr_expression)
# boundary condition is already created.
#
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-1', previous=  'Step-1')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-2', previous=    'Step-Col-1')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='Step-Col-3', previous=   'Step-Col-2')
field_val = [
['Disp_X-Col-1', '1*X + 0*Y'],
['Disp_Y-Col-1', '0*X + 0*Y'],
['Disp_X-Col-2', '0*X + 0*Y'],
['Disp_Y-Col-2', '0*X + 1*Y'],
['Disp_X-Col-3', '0*X + 0.5*Y'],
['Disp_Y-Col-3', '0.5*X + 0*Y'],
]
for name, val in field_val:
    mdb.models['Model-1_pos'].ExpressionField(description='', expression=val, localCsys=None, name=name)

mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-1_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-1_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_X-Col-1', fixed=OFF,
    localCsys=None, name='c2_top_left_col-1_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-1_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-1_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-1', distributionType=FIELD, fieldName='Disp_Y-Col-1', fixed=OFF,
    localCsys=None, name='c2_top_left_col-1_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)



mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-2_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-2_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_X-Col-2', fixed=OFF,
    localCsys=None, name='c2_top_left_col-2_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-2_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-2_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-2', distributionType=FIELD, fieldName='Disp_Y-Col-2', fixed=OFF,
    localCsys=None, name='c2_top_left_col-2_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)




mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-3_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-3_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_X-Col-3', fixed=OFF,
    localCsys=None, name='c2_top_left_col-3_X', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=1.0, u2=UNSET, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c5_bottom_right_col-3_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c5'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c6_bottom_left_col-3_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c6'], u1=UNSET, u2=1, ur3=UNSET)
mdb.models['Model-1_pos'].DisplacementBC(amplitude=UNSET, createStepName=
    'Step-Col-3', distributionType=FIELD, fieldName='Disp_Y-Col-3', fixed=OFF,
    localCsys=None, name='c2_top_left_col-3_Y', region=
    mdb.models['Model-1_pos'].rootAssembly.sets['c2'], u1=UNSET, u2=1, ur3=UNSET)







