"""Script to extract deformation gradient from ABAQUS 
generated ".dat" file
Create a vector of F_m_inv_T to be used to PK1 extraction

"""
from pathlib import Path
import numpy as np
import pandas as pd

# Update nrow = nelements (reduced integration)
# 		 skiprows = See the dat file
nrows = 35975
skiprows = 157956
file = Path("E:/NN_Research/Prob_YvonnetPlwholeRVE/HetergenousRVE/Pl_w_hole_PBC.dat")
df = pd.read_csv(
    file,
    nrows=nrows,
    skiprows=skiprows,
    sep=r"\s+",
    header=None,
    names=["ELEMENT", "PT FOOT-NOTE", "DG11", "DG22", "DG33", "DG12", "DG21"],
)

df = df[["DG11", "DG12", "DG21", "DG22"]]
df = np.array(df)
np.save("F_m.npy", df)
F_m_inv_T_List = []
det_F_m_List = []
for F_m in df:
    F_m_mat = F_m.reshape(2, 2)
    det_F_m_List.append(np.linalg.det(F_m_mat))
    F_m_mat_inv_T = (np.linalg.inv(F_m_mat)).T
    F_m_inv_T_List.append(F_m_mat_inv_T.flatten())
np.savez(
    "F_m_inv_T_and_F_det_List.npz",
    F_m_inv_T_List=F_m_inv_T_List,
    det_F_m_List=det_F_m_List,
)
