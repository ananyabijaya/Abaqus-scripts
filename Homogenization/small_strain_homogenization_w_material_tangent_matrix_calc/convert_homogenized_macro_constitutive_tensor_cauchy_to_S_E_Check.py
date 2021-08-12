import numpy as np

det_F_M = 1.1
F_M_inv = np.array([[1, 0.5], [0.5, 1.2]])
F_M_inv
get_from_abq = np.array([[1, 2, 4], [2, 4, 0], [4, 0, 8]])
c_mat_cs_2d = get_from_abq




# C_column related to epsilon 12 is multiplied by 2
# c_mat_cs_2d[:, 2] = c_mat_cs_2d[:, 2]

c_mat_cs = np.zeros([2, 2, 2, 2])
c_mat_cs[0, 0, 0, 0] = c_mat_cs_2d[0, 0]
c_mat_cs[1, 1, 1, 1] = c_mat_cs_2d[1, 1]
c_mat_cs[0, 0, 1, 1] = c_mat_cs_2d[0, 1]
c_mat_cs[1, 1, 0, 0] = c_mat_cs_2d[1, 0]

c_mat_cs[0, 1, 0, 1] = c_mat_cs_2d[2, 2]
c_mat_cs[0, 1, 1, 0] = c_mat_cs_2d[2, 2]
c_mat_cs[1, 0, 0, 1] = c_mat_cs_2d[2, 2]
c_mat_cs[1, 0, 1, 0] = c_mat_cs_2d[2, 2]

c_mat_cs[0, 0, 0, 1] = c_mat_cs_2d[0, 2]
c_mat_cs[0, 0, 1, 0] = c_mat_cs_2d[0, 2]
c_mat_cs[1, 1, 0, 1] = c_mat_cs_2d[1, 2]
c_mat_cs[1, 1, 1, 0] = c_mat_cs_2d[1, 2]

c_mat_cs[0, 1, 0, 0] = c_mat_cs_2d[2, 0]
c_mat_cs[1, 0, 0, 0] = c_mat_cs_2d[2, 0]
c_mat_cs[0, 1, 1, 1] = c_mat_cs_2d[2, 1]
c_mat_cs[1, 0, 1, 1] = c_mat_cs_2d[2, 1]


C_mat_S_cs_mat_terms = np.zeros([2, 2, 2, 2])
C_mat_S_cs_terms = np.zeros([2, 2, 2, 2])

for X, Y, M, N in [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
]:
    print(X, Y, M, N)
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                for l in range(0, 2):
                    C_mat_S_cs_mat_terms[X, Y, M, N] = C_mat_S_cs_mat_terms[
                        X, Y, M, N
                    ] + det_F_M * (
                        (
                            F_M_inv[X, i]
                            * F_M_inv[Y, j]
                            * F_M_inv[M, k]
                            * F_M_inv[N, l]
                            * c_mat_cs[i, j, k, l]
                        )
                    )

C_mat_S = C_mat_S_cs_mat_terms


F_dash = np.array(
    [
        [F_M_inv[0, 0] ** 2, F_M_inv[0, 1]**2, 2 * F_M_inv[0, 0] * F_M_inv[0, 1]],
        [F_M_inv[1, 0] ** 2, F_M_inv[1, 1] ** 2, 2 * F_M_inv[1, 1] * F_M_inv[1, 0]],
        [
            F_M_inv[0, 0] * F_M_inv[1, 0],
            F_M_inv[0, 1] * F_M_inv[1, 1],
            F_M_inv[0, 0] * F_M_inv[1, 1] + F_M_inv[0, 1] * F_M_inv[1, 0],
        ],
    ]
)
C_mat_S_alt = det_F_M* @ get_from_abq @ F_dash.T
