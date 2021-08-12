# Begin Post Processing
# Open the Output Data Base for the current Job
import numpy as np
from abaqus import *
from abaqusConstants import *
from odbAccess import *
from visualization import *

# path = r'E:\NN_Research\Example1_Hyperelasticity'
# file = path + "\\F_M_and_E_gl_List.npz"
# arrays = np.load(file)

# Read F_micro extracted from .dat file
file = "F_m_inv_T_and_F_det_List.npz"
array = np.load(file)
F_m_inv_T_List = array["F_m_inv_T_List"]
det_F_m_List = array["det_F_m_List"]
# Deformation gradient at microscale
F_m_List = np.load("F_m.npy")


E_gl_M_data = []
PK2_M_data = []
# load11, load12, load21, load22 = load
job_name = "Pl_w_hole_PBC"
odb = openOdb(path=job_name + ".odb")
myAssembly = odb.rootAssembly;
I = np.diag([1, 1, 1])
try:
    frameRepository = odb.steps['Step-1'].frames;
except:
    pass

frameS = [];
frameIVOL = [];
# for frame in frameRepository:
frame = frameRepository[0]
elms_Vol = frame.fieldOutputs['IVOL'].getSubset(position=INTEGRATION_POINT)
Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
# Tot_Vol = Volumes.sum(axis=0)
Tot_Vol = 1
frame = frameRepository[-1]
sigma = frame.fieldOutputs['S'].getSubset(position=INTEGRATION_POINT)
sigma=np.copy(sigma.bulkDataBlocks[0].data)
sigma_11, sigma_22, sigma_33, sigma_12 = sigma[:,0], sigma[:,1], sigma[:,2], sigma[:,3]
sigma_21 = sigma_12
F_m_inv_T_11, F_m_inv_T_12, F_m_inv_T_21, F_m_inv_T_22 = F_m_inv_T_List[:,0], F_m_inv_T_List[:,1], F_m_inv_T_List[:,2], F_m_inv_T_List[:,3]
F_m_inv_T_33 = np.ones(F_m_inv_T_11.shape)
PK1_11_m = (det_F_m_List) * (sigma_11*F_m_inv_T_11 + sigma_12*F_m_inv_T_21)
PK1_12_m = (det_F_m_List) * (sigma_11*F_m_inv_T_12 + sigma_12*F_m_inv_T_22) 
PK1_21_m = (det_F_m_List) * (sigma_21*F_m_inv_T_11 + sigma_22*F_m_inv_T_21)
PK1_22_m = (det_F_m_List) * (sigma_21*F_m_inv_T_12 + sigma_12*F_m_inv_T_22)  
PK1_33_m = (det_F_m_List) * (sigma_33*F_m_inv_T_33) 

PK1_11_M = (PK1_11_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
PK1_12_M = (PK1_12_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
# PK1_13_M = (PK1_13_m * Volumes).sum(axis=0) / Tot_Vol
PK1_21_M = (PK1_21_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
PK1_22_M = (PK1_22_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
# PK1_23_M = (PK1_23_m * Volumes).sum(axis=0) / Tot_Vol
# PK1_31_M = (PK1_31_m * Volumes).sum(axis=0) / Tot_Vol
# PK1_32_M = (PK1_32_m * Volumes).sum(axis=0) / Tot_Vol
PK1_33_M = (PK1_33_m[:, None] * Volumes).sum(axis=0) / Tot_Vol

# Validating F_M using < F_m > formula
F_m_11, F_m_12, F_m_21, F_m_22 = F_m[:,0], F_m[:,1], F_m[:,2], F_m[:,3]
F_M_11_ver = (F_m_11[:, None] * Volumes).sum(axis=0)/Tot_Vol
F_M_12_ver = (F_m_12[:, None] * Volumes).sum(axis=0)/Tot_Vol
F_M_21_ver = (F_m_21[:, None] * Volumes).sum(axis=0)/Tot_Vol
F_M_22_ver = (F_m_22[:, None] * Volumes).sum(axis=0)/Tot_Vol
.sum(axis=0)
PK1_M = np.matrix([
    [PK1_11_M[0], PK1_12_M[0], 0],
    [PK1_21_M[0], PK1_22_M[0], 0],
    [0, 0, PK1_33_M[0]]
])

F_M_temp = np.matrix([
    [F_M[0], F_M[1], 0],
    [F_M[2], F_M[3], 0],
    [0, 0, 1]
])
# F_M = np.array([load11+1, load12, 0, load21, load22 +1, 0, 0, 0, 1])
# F_M= F_M.flatten()
# PK1_M = PK1_M.flatten()
PK2_M = np.linalg.inv(F_M_temp) * PK1_M
kk = kk + 1
E_gl_M_data.append(E_gl_M)
PK2_M_data.append(PK2_M.flatten())
odb.close()
E_gl_M_data = np.array(E_gl_M_data)
PK2_M_data = np.array(PK2_M_data)
np.savez("E_gl_M_data_and_PK2_M_Data_odb", E_gl_M_data=E_gl_M_data,
         PK2__M_Data=PK2_M_data)
