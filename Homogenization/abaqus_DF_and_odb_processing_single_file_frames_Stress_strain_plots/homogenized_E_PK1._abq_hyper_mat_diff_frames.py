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
# Change file name
#############################################################


path = os.getcwd()
saving_dir = "F_M_E_gl_M_and_PK2_M_data"
try:
	os.mkdir(saving_dir)
except OSError as error:
	print(error)

# job_name = "load_governed"
job_name = 'Uniaxial_test_with_PBC'
odb = openOdb(path=job_name+".odb")
myAssembly = odb.rootAssembly


I = np.matrix([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]
	])    

F_M_data = []
E_gl_M_data = []
PK2_M_data = []

frameRepository = odb.steps["Step-1"].frames
frame = frameRepository[0]
elms_Vol = frame.fieldOutputs["IVOL"].getSubset(position=INTEGRATION_POINT)
Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
# every n increments field output is 
frame_inc = 1
frames_considered= 165
Tot_Vol =  4.33E-3 * 4.0E-3
# Tot_Vol = Volumes.sum(axis = 0)

for kk, frame in enumerate(frameRepository):
# if True:
	# kk =12
	# frame = frameRepository[-1]
	if kk == 0: continue
	if(kk > frames_considered):
		break
	print(frame.frameId)
	print(kk)
	filename = str(frame_inc* (kk))+"_frame_F_m_&_F_m_inv_T_&_F_det.npz"
	path_df_data = path + "\\df_data\\" + filename
	array = np.load(path_df_data)
	F_m_List = array["F_m_List"]
	F_m_inv_T_List = array["F_m_inv_T_List"]
	det_F_m_List = array["det_F_m_List"]
	#
	#
	sigma = frame.fieldOutputs["S"].getSubset(position=INTEGRATION_POINT)
	sigma = np.copy(sigma.bulkDataBlocks[0].data)
	sigma_11, sigma_22, sigma_33, sigma_12 = (
		sigma[:, 0],
		sigma[:, 1],
		sigma[:, 2],
		sigma[:, 3],
	)
	sigma_21 = sigma_12
	F_m_inv_T_11, F_m_inv_T_12, F_m_inv_T_21, F_m_inv_T_22 = (
		F_m_inv_T_List[:, 0],
		F_m_inv_T_List[:, 1],
		F_m_inv_T_List[:, 2],
		F_m_inv_T_List[:, 3],
	)
	F_m_inv_T_33 = np.ones(F_m_inv_T_11.shape)
	#
	PK1_11_m = ( det_F_m_List) * (sigma_11 * F_m_inv_T_11 + sigma_12 * F_m_inv_T_21)
	PK1_12_m = ( det_F_m_List) * (sigma_11 * F_m_inv_T_12 + sigma_12 * F_m_inv_T_22)
	PK1_21_m = ( det_F_m_List) * (sigma_21 * F_m_inv_T_11 + sigma_22 * F_m_inv_T_21)
	PK1_22_m = ( det_F_m_List) * (sigma_21 * F_m_inv_T_12 + sigma_22 * F_m_inv_T_22)
	PK1_33_m = ( det_F_m_List) * (sigma_33 * F_m_inv_T_33)
	#
	PK1_11_M = (PK1_11_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
	PK1_12_M = (PK1_12_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
	# PK1_13_M = (PK1_13_m * Volumes).sum(axis=0) / Tot_Vol
	PK1_21_M = (PK1_21_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
	PK1_22_M = (PK1_22_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
	# PK1_23_M = (PK1_23_m * Volumes).sum(axis=0) / Tot_Vol
	# PK1_31_M = (PK1_31_m * Volumes).sum(axis=0) / Tot_Vol
	# PK1_32_M = (PK1_32_m * Volumes).sum(axis=0) / Tot_Vol
	PK1_33_M = (PK1_33_m[:, None] * Volumes).sum(axis=0) / Tot_Vol
	#
	#
	F_m_11, F_m_12, F_m_21, F_m_22 = F_m_List[:,0], F_m_List[:,1], F_m_List[:,2], F_m_List[:,3]
	F_M_11 = (F_m_11[:, None] * Volumes).sum(axis=0)/Tot_Vol
	F_M_12 = (F_m_12[:, None] * Volumes).sum(axis=0)/Tot_Vol
	F_M_21 = (F_m_21[:, None] * Volumes).sum(axis=0)/Tot_Vol
	F_M_22 = (F_m_22[:, None] * Volumes).sum(axis=0)/Tot_Vol
	F_M = np.matrix([
			[F_M_11[0], F_M_12[0], 0],
			[F_M_21[0], F_M_22[0], 0],
			[0, 0, 1]
		])
	#
	PK1_M = np.matrix(
		[
			[PK1_11_M[0], PK1_12_M[0], 0],
			[PK1_21_M[0], PK1_22_M[0], 0],
			[0, 0, PK1_33_M[0]],
		]
	)
	#
	PK2_M = np.linalg.inv(F_M) * PK1_M
	E_gl_M = 0.5 * ((F_M.T* F_M) - I)
	F_M_data.append(F_M.flatten())
	E_gl_M_data.append(E_gl_M.flatten())
	PK2_M_data.append(PK2_M.flatten())
	# odb.close()

F_M_data = np.array(F_M_data)
E_gl_M_data = np.array(E_gl_M_data)
PK2_M_data = np.array(PK2_M_data)
np.savez(
	saving_dir + "//E_gl_M_data_and_PK2_M_data_odb",
	F_M_data = F_M_data,
	E_gl_M_data=E_gl_M_data,
	PK2_M_data=PK2_M_data,
)
