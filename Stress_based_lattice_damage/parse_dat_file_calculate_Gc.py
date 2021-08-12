"""Script to extract deformation gradient from ABAQUS
generated ".dat" file
Create a vector of F_m_inv_T to be used to PK1 extraction

"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Update nrow = nelements (reduced integration)
# 		 skiprows = See the dat file

last_increment = 50
increment_size = 25 # Field output writing increment
total_increments = int(last_increment / increment_size)
nrows_sdv = 120334
nrows_rf_u = 21
skiprows = 275
skips_btw_sdv_rf_u = 20
skips_btw_rf_u__sdv = 27
#
#
inc_strain_energy = 0
inc_work_done = 0
inc_strain_energy_list = []
inc_work_done_list = []
strain_energy_prev = 0
RF1_prev = 0
u1_prev = 0
disp_list = []
load_list = []
for i in range(0, total_increments):
    print("current iteration: ", i)
    file = Path("UEL_input_file.dat")
    df = pd.read_csv(
        file,
        nrows=nrows_sdv,
        skiprows=skiprows,
        sep=r"\s+",
        header=None,
        names=["ELEMENT", "PT FOOT-NOTE", "SDV1", "SDV2", "SDV3"],
    )
    # df = df[["ELEMENT", "SDV3"]]
    inc_strain_energy = df["SDV3"].sum() - strain_energy_prev
    strain_energy_prev = df["SDV3"].sum()
    inc_strain_energy_list.append(inc_strain_energy)

    # df = np.array(df)
    # np.savez("energy_"+str((i+1)*25)+".npz", df, allow_pickle = True )
    skiprows = nrows_sdv + skiprows + skips_btw_sdv_rf_u


    df = pd.read_csv(
        file,
        nrows=nrows_rf_u,
        skiprows=skiprows,
        sep=r"\s+",
        header=None,
        names=["NODE PT FOOT-NOTE", "U1", "U2", "UR3", "RF1", "RF2", "RM3"],
    )
    u1_current = df['U1'].mean()
    RF1_current = df['RF1'].sum()
    disp_list.append(u1_current)
    load_list.append(RF1_current)
    inc_work_done = 0.5 * (RF1_prev + RF1_current) * (u1_current - u1_prev)
    inc_work_done_list.append(inc_work_done)
    u1_prev = u1_current
    RF1_prev = RF1_current

    # df = np.array(df)
    # np.savez("rf_u_" + str((i + 1) * 25) + ".npz", df, allow_pickle = True)
    skiprows = skiprows + nrows_rf_u + skips_btw_rf_u__sdv

np.savetxt("load_disp_1D.csv", np.array([
    disp_list,
    load_list
    ]).transpose())

np.savetxt("strain_energy_work_done.csv", np.array([
    inc_strain_energy_list,
    inc_work_done_list
    ]
    ).transpose())

plt.figure()
plt.plot(disp_list, load_list)
plt.savefig("load_disp_1D.png")

plt.figure()
plt.plot(inc_strain_energy_list)
plt.savefig("inc_strain_energy.png")

plt.figure()
plt.plot(inc_work_done_list)
plt.savefig("inc_work_done.png")

# crack_leh = input("Enter the measured crack length")
