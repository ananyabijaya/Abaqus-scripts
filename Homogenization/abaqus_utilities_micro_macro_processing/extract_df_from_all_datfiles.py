"""Script to extract deformation gradient from ABAQUS 
generated ".dat" file
Create a vector of F_m_inv_T to be used to PK1 extraction

"""
from pathlib import Path
import numpy as np
import pandas as pd
from glob import glob
import os

# Update nrow = nelements (reduced integration)
# 		 skiprows = See the dat file
print(" Check if nrows and skiprows are correct ...")
nrows = 35975
skiprows = 157956
path = Path().absolute()
files = path.glob("*.dat")
df_data_dir = "df_data"
try:
    os.mkdir(df_data_dir)
except OSError as error:
    print(error)
path_saving = path / df_data_dir
# print( "Total no. of successfull analysis = " files.__len__() )

for fn in files:
    # Update nrow = nelements (reduced integration)
    # 		 skiprows = See the dat file
    print("Current file being processed:", fn.name)
    nrows = 35975
    skiprows = 157956
    df = pd.read_csv(
        fn,
        nrows=nrows,
        skiprows=skiprows,
        sep=r"\s+",
        header=None,
        names=["ELEMENT", "PT FOOT-NOTE", "DG11", "DG22", "DG33", "DG12", "DG21"],
    )
    # Check if the data is correct; (0,0) entry should be element 1
    if df["ELEMENT"].values[0] == 1:
        df = df[["DG11", "DG12", "DG21", "DG22"]]
        df = np.array(df)
        np.save(os.path.join(path_saving, "F_m" + fn.name[:-4] + ".npy"), df)
        F_m_inv_T_List = []
        det_F_m_List = []
        for F_m in df:
            F_m_mat = F_m.reshape(2, 2)
            det_F_m_List.append(np.linalg.det(F_m_mat))
            F_m_mat_inv_T = (np.linalg.inv(F_m_mat)).T
            F_m_inv_T_List.append(F_m_mat_inv_T.flatten())
        np.savez(
            os.path.join(path_saving, fn.name[:-4] + "_F_m_inv_T_and_F_det_List.npz"),
            F_m_inv_T_List=F_m_inv_T_List,
            det_F_m_List=det_F_m_List,
        )
    else:
        print("Failed analysis or modify skiprows. Filename:", fn.name)
