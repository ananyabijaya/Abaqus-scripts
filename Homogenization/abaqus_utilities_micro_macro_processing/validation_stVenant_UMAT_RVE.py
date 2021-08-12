from pathlib import Path
import numpy as np
import glob

path = Path(r"E:\NN_Research\Example1_Hyperelasticity")
file = path / "E_gl_M_data_and_PK2_M_Data_odb.npz"
arrays = np.load(file)
E_gl_M_data = arrays["E_gl_M_data"]
S_M_data = arrays["PK2__M_Data"]
Eyoung = 200e9
xnu = 0.3
Gshear = Eyoung / (2 * (1 + xnu))
Kbulk = Eyoung / (3 * (1 - 2 * xnu))
lmbda = Kbulk - (2 / 3) * Gshear

file = []
I = np.diag([1, 1])
i = 0
for E_gl, S in zip(E_gl_M_data, S_M_data):
    S = S.reshape(3, 3)
    E_gl = E_gl.reshape(2, 2)
    PK2_stV = lmbda * np.trace(E_gl) * I + 2 * Gshear * E_gl
    check = np.isclose(PK2_stV, S[:2, :2], atol=10 ** 5)

    if check.sum() != 4:
        print("Check failed")
        print("iteration", i)
        print(PK2_stV, S)
    i = i + 1
    # print("Iteration:", i)
