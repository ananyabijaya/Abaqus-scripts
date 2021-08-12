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



job_name = "triangle__1"
try:
    odb = openOdb(path=job_name + ".odb")
except:
    print("odb doesn't exists")

myAssembly = odb.rootAssembly
I = np.diag([1, 1, 1])
TOP_FACE=odb.rootAssembly.instances['TRIANGULAR_LATTICE_15_DEG-1'].nodeSets['TOP_FACE']

frameRepository = odb.steps["Step-1"].frames
RF_all_frames_list = []
Disp_all_frames_list = []
for frame in frameRepository:
    # frame = frameRepository[-1]
    reaction_forces = frame.fieldOutputs["RF"].getSubset(position=NODAL, region=TOP_FACE)
    reaction_forces = np.copy(reaction_forces.bulkDataBlocks[0].data)
    displacement = frame.fieldOutputs["U"].getSubset(position=NODAL, region =TOP_FACE)
    displacement = np.copy(displacement.bulkDataBlocks[0].data)
    damage = frame.fieldOutputs["FV1"].getSubset(position=ELEMENT_NODAL)
    damage = np.copy(damage.bulkDataBlocks[0].data)
    RF_total = reaction_forces.sum(axis = 0)
    Disp_applied = displacement[0]
    RF_all_frames_list.append(RF_total)
    Disp_all_frames_list.append(Disp_applied)

# REFERENCE: https://abaqus-docs.mit.edu/2017/English/IhrComponentMap/ihr-c-Abaqus-ExampleParametersExtractAdd.htmL
Strain_energy = odb.steps['Step-1'].historyRegions['Assembly ASSEMBLY'].historyOutputs['ALLSE'].data
Strain_energy = np.array(Strain_energy)

RF_all_frames_list = np.array(RF_all_frames_list)
Disp_all_frames_list= np.array(Disp_all_frames_list)

# COORD = frame.fieldOutputs["COORD"].getSubset(position=NODAL)
# COORD = np.copy(COORD.bulkDataBlocks[0].data)

Load_Disp = np.column_stack((Disp_all_frames_list, RF_all_frames_list, Strain_energy))
np.savez("Load_Disp_SE.npz", Load_Disp = Load_Disp)
np.savetxt("Load_Disp_SE.csv", Load_Disp)