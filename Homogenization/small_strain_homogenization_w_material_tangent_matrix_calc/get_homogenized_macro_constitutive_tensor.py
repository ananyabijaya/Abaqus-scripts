 # Begin Post Processing
# Open the Output Data Base for the current Job
import numpy as np
from abaqus import *
from abaqusConstants import *
from odbAccess import *
from visualization import *
import os

#############################################################
# UPDATE Tot_Vol?
#############################################################


path = os.getcwd()
# file = path + "\\F_M_and_E_gl_List_pos.npz"
# saving_dir = "E_gl_M_and_PK2_M_data"


# try:
#     os.mkdir(saving_dir)
# except OSError as error:
#     print(error)



job_name = "Job-1"
Tot_Vol = 6E-3 * 6.06E-3
try:
    odb = openOdb(path=job_name + ".odb")
except:
    print("odb doesn't exists")

myAssembly = odb.rootAssembly
I = np.diag([1, 1, 1])


frameRepository = odb.steps["Step-Col-1"].frames
frameS = []
frameIVOL = []
# for frame in frameRepository:
frame = frameRepository[0]
elms_Vol = frame.fieldOutputs["IVOL"].getSubset(position=INTEGRATION_POINT)
Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
frame = frameRepository[-1]
sigma = frame.fieldOutputs["S"].getSubset(position=INTEGRATION_POINT)
sigma = np.copy(sigma.bulkDataBlocks[0].data)
sigma_11_m, sigma_22_m, sigma_33_m, sigma_12_m = (
    sigma[:, 0],
    sigma[:, 1],
    sigma[:, 2],
    sigma[:, 3],
)


sigma_11_M = (sigma_11_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_12_M = (sigma_12_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
# sigma_21_M = (sigma_21_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_22_M = (sigma_22_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_33_M = (sigma_33_m[:, None] * Volumes).sum(axis=0) / Tot_Vol

C11 = sigma_11_M
C21 = sigma_22_M
C31 = sigma_12_M

#####################################################################
frameRepository = odb.steps["Step-Col-2"].frames
frame = frameRepository[0]
elms_Vol = frame.fieldOutputs["IVOL"].getSubset(position=INTEGRATION_POINT)
Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
frame = frameRepository[-1]
sigma = frame.fieldOutputs["S"].getSubset(position=INTEGRATION_POINT)
sigma = np.copy(sigma.bulkDataBlocks[0].data)
sigma_11_m, sigma_22_m, sigma_33_m, sigma_12_m = (
    sigma[:, 0],
    sigma[:, 1],
    sigma[:, 2],
    sigma[:, 3],
)

sigma_11_M = (sigma_11_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_12_M = (sigma_12_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
# sigma_21_M = (sigma_21_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_22_M = (sigma_22_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_33_M = (sigma_33_m[:, None] * Volumes).sum(axis=0) / Tot_Vol

C12 = sigma_11_M
C22 = sigma_22_M
C32 = sigma_12_M

######################################################################
frameRepository = odb.steps["Step-Col-3"].frames
frame = frameRepository[0]
elms_Vol = frame.fieldOutputs["IVOL"].getSubset(position=INTEGRATION_POINT)
Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
frame = frameRepository[-1]
sigma = frame.fieldOutputs["S"].getSubset(position=INTEGRATION_POINT)
sigma = np.copy(sigma.bulkDataBlocks[0].data)
sigma_11_m, sigma_22_m, sigma_33_m, sigma_12_m = (
    sigma[:, 0],
    sigma[:, 1],
    sigma[:, 2],
    sigma[:, 3],
)
sigma_11_M = (sigma_11_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_12_M = (sigma_12_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
# sigma_21_M = (sigma_21_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_22_M = (sigma_22_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
sigma_33_M = (sigma_33_m[:, None] * Volumes).sum(axis=0) / Tot_Vol

C13 = sigma_11_M
C23 = sigma_22_M
C33 = sigma_12_M

C_tensor = np.array([
    [C11, C12, C13],
    [C21, C22, C23],
    [C31, C32, C33]
    ])


np.savez("C_tensor.npz", C_tensor = C_tensor)
np.savetxt("C_tensor", C_tensor)