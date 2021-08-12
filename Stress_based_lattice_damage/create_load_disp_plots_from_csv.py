import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import pdb
from pathlib import Path
import os

# direcs = [
# 	"E410_t_0_14e-4__Actual_case",
# ]
# for direc in direcs:
plt.figure()
# path = Path().absolute()
# path = path/direc
# files = path.glob("*.csv")
# for file in files:
file = "Load_Disp_SE.csv"
print(file)
df = pd.read_csv(file, delimiter = r"\s+", header=None)
# df[0] = - df[0] /1000
# df[1] = -df[1] * 1000
# print(df[1].max())

plt.plot(df[1], df[3], label = "load_disp")
plt.legend(framealpha=1, frameon=True);
# plt.show()
plt.title(" load-disp")
plt.show()
plt.savefig("load-disp.png")

plt.figure()
plt.plot(df[1], df[5], label =  "Strain_energy")
plt.legend(framealpha=1, frameon=True);
# plt.show()
plt.title("Strain energy")
plt.show()
plt.savefig(direc+"Strain_energy.png")