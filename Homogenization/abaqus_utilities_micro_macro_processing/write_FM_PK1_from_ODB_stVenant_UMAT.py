#Begin Post Processing
#Open the Output Data Base for the current Job
from visualization import *
import numpy as np
from abaqus import *
from abaqusConstants import *
from odbAccess import *
import pickle as pkl
import numpy as np
import os
# F11_m_I11 = np.linspace(-0.25, 0.25, 11)
# F22_m_I22 = np.linspace(-0.25, 0.25, 11)
# F12_m_I12 = np.linspace(-0.25, 0.25, 11)
# F21_m_I21 = np.linspace(-0.25, 0.25, 11)

# disp_bc_11 = np.repeat( F11_m_I11, 11**3, axis = 0)
# disp_bc_12 = np.repeat( F12_m_I12, 11**3, axis = 0)
# disp_bc_21 = np.repeat( F21_m_I21, 11**3, axis = 0)
# disp_bc_22 = np.repeat( F22_m_I22, 11**3, axis = 0)
# # disp_bc_11 = disp_bc_11.reshape(11**3 , -1)
# disp_bc_12 = disp_bc_12.reshape(11**3, -1)
# disp_bc_21 = disp_bc_21.reshape(11**2 , -1)
# disp_bc_22 = disp_bc_22.reshape(11 , -1)

# disp_bc = np.column_stack(( disp_bc_11.T.flatten(), disp_bc_12.T.flatten(), disp_bc_21.T.flatten(), disp_bc_22.T.flatten() ))
# det_F = (disp_bc[:,0] + 1) * (disp_bc[:,3] +1) - disp_bc[:,1] * disp_bc[:,2]
# disp_bc = np.delete(disp_bc, np.where(det_F <= 0), axis = 0)

path = os.getcwd()
file = path+"\\F_M_and_E_gl_List.npz"
arrays = np.load(file)
# E_gl_List = arrays["E_gl_List"]
# F_M_List = arrays["F_M_List"]

saving_dir = "E_gl_M_and_PK2_M_data"
try: 
    os.mkdir(saving_dir)
except OSError as error: 
    print(error)  

E_gl_M_data = []
PK2_M_data = []
kk = 0
for F_M, E_gl_M in zip(arrays["F_M_List"], arrays["E_gl_List"]):
	# load11, load12, load21, load22 = load
	print(kk)
	# try:
	# 	job_name = "Ex1"+"_"+str(load11)[0:6]+"_"+str(load12)[0:6]+"_"+str(load21)[0:6]+"_"+str(load22)[0:6]
	# 	job_name = job_name.replace(".","__")
	# 	print(job_name)
	# 	odb = openOdb(path=job_name+".odb")
	# except: continue
	job_name = str(kk)
	odb = openOdb(path=job_name+".odb")
	myAssembly = odb.rootAssembly;
	I = np.diag([1,1,1])
	try:
		frameRepository = odb.steps['Step-1'].frames;
	except: continue
	frameS=[];
	frameIVOL=[];
	# for frame in frameRepository:
	frame = frameRepository[0]
	elms_Vol=frame.fieldOutputs['IVOL'].getSubset(position=INTEGRATION_POINT)
	Volumes = np.copy(elms_Vol.bulkDataBlocks[0].data)
	# Tot_Vol  = Volumes.sum(axis=0)
	Tot_Vol =  2.E-03 *  2.E-03
	frame = frameRepository[-1]
	PK1_11 = frame.fieldOutputs['SDV10'].getSubset( position=INTEGRATION_POINT)
	PK1_11 = np.copy(PK1_11.bulkDataBlocks[0].data)
	PK1_12 = frame.fieldOutputs['SDV11'].getSubset( position=INTEGRATION_POINT)
	PK1_12 = np.copy(PK1_12.bulkDataBlocks[0].data)
	PK1_13 = frame.fieldOutputs['SDV12'].getSubset( position=INTEGRATION_POINT)
	PK1_13 = np.copy(PK1_13.bulkDataBlocks[0].data)
	PK1_21 = frame.fieldOutputs['SDV13'].getSubset( position=INTEGRATION_POINT)
	PK1_21 = np.copy(PK1_21.bulkDataBlocks[0].data)
	PK1_22 = frame.fieldOutputs['SDV14'].getSubset( position=INTEGRATION_POINT)
	PK1_22 = np.copy(PK1_22.bulkDataBlocks[0].data)
	PK1_23 = frame.fieldOutputs['SDV15'].getSubset( position=INTEGRATION_POINT)
	PK1_23 = np.copy(PK1_23.bulkDataBlocks[0].data)
	PK1_31 = frame.fieldOutputs['SDV16'].getSubset( position=INTEGRATION_POINT)
	PK1_31 = np.copy(PK1_31.bulkDataBlocks[0].data)
	PK1_32 = frame.fieldOutputs['SDV17'].getSubset( position=INTEGRATION_POINT)
	PK1_32 = np.copy(PK1_32.bulkDataBlocks[0].data)
	PK1_33 = frame.fieldOutputs['SDV18'].getSubset( position=INTEGRATION_POINT)
	PK1_33 = np.copy(PK1_33.bulkDataBlocks[0].data)
	PK1_11_M = (PK1_11 * Volumes).sum(axis=0)/Tot_Vol
	PK1_12_M = (PK1_12 * Volumes).sum(axis=0)/Tot_Vol
	PK1_13_M = (PK1_13 * Volumes).sum(axis=0)/Tot_Vol
	PK1_21_M = (PK1_21 * Volumes).sum(axis=0)/Tot_Vol
	PK1_22_M = (PK1_22 * Volumes).sum(axis=0)/Tot_Vol
	PK1_23_M = (PK1_23 * Volumes).sum(axis=0)/Tot_Vol
	PK1_31_M = (PK1_31 * Volumes).sum(axis=0)/Tot_Vol
	PK1_32_M = (PK1_32 * Volumes).sum(axis=0)/Tot_Vol
	PK1_33_M = (PK1_33 * Volumes).sum(axis=0)/Tot_Vol		
	PK1_M = np.matrix([ 
		[PK1_11_M[0], PK1_12_M[0], PK1_13_M[0]],
		[PK1_21_M[0], PK1_22_M[0], PK1_23_M[0]],
		[PK1_31_M[0], PK1_32_M[0], PK1_33_M[0]]
		])
	F_M_temp = np.matrix([ 
		[F_M[0], F_M[1], 0 ],
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
np.savez(saving_dir+"//E_gl_M_data_and_PK2_M_data_odb",  E_gl_M_data = E_gl_M_data , PK2_M_data = PK2_M_data)
