"""Script to extract deformation gradient from ABAQUS 
generated ".dat" file
Create a vector of F_m_inv_T to be used to PK1 extraction

"""
from pathlib import Path
import numpy as np
import pandas as pd
from glob import glob
import os
import pathlib

#####################################################
# Update nrow = nelements (reduced integration)
#        skiprows = See the dat file# nrows = 4504
# skiprows = 21871
#####################################################

path = Path().absolute()
# files = path.glob("*.dat")
# fn = r'E:\NN_Research\microstructural_response_testing\triangular_rve4x4_t_l_0_1\load_governed.dat'
fn = r'E:\NN_Research\microstructural_response_testing\triangular_rve4x4_t_l_0_1\Uniaxial_test_with_PBC.dat'
df_data_dir = "df_data"
pathlib.Path(df_data_dir).mkdir(parents=True,
													exist_ok=True)
path_saving = path / df_data_dir

# start_skip = 47764
# skiprows = 10325
# nrows = 10298

start_skip = 51388
skiprows = 10447
nrows = 10420
# considering 5, 10, 15 ..., 40 increments 
n_skips = 1
n_inc = 165



print("Current file being processed:", fn)
frame_no = 0
skiprow_inc = start_skip
# for inc in range(0, n_skips+1):
for inc in range(n_inc):
	frame_no = (inc+1) * n_skips
	skiprow_inc = start_skip + inc * skiprows
	print(skiprow_inc)
	df = pd.read_csv(
		fn,
		nrows=nrows,
		skiprows=skiprow_inc,
		sep=r"\s+",
		header=None,
		names=["ELEMENT", "PT FOOT-NOTE", "DG11", "DG22", "DG33", "DG12", "DG21"],
	)
	# Check if the data is correct; (0,0) entry should be element 1
	if df["ELEMENT"].values[0] == 1:
		df = df[["DG11", "DG12", "DG21", "DG22"]]
		df = np.array(df)
		F_m_inv_T_List = []
		det_F_m_List = []
		for F_m in df:
			F_m_mat = F_m.reshape(2, 2)
			det_F_m_List.append(np.linalg.det(F_m_mat))
			F_m_mat_inv_T = (np.linalg.inv(F_m_mat)).T
			F_m_inv_T_List.append(F_m_mat_inv_T.flatten())
		np.savez(
			os.path.join(path_saving, str(frame_no) + "_frame_F_m_&_F_m_inv_T_&_F_det.npz"),
			F_m_List = df,
			F_m_inv_T_List=F_m_inv_T_List,
			det_F_m_List=det_F_m_List,
		)
	else:
		print("Failed analysis or modify skiprows. Filename:", fn)
