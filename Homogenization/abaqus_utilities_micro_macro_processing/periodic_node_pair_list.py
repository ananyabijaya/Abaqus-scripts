import pandas as pd
import os
import csv
import numpy as np

# Copy paste node list from input ".inp" file to a 'node_coord.csv'
df = pd.read_csv('node_coord.csv', header=None, names=['id', 'x', 'y'])

tol = 10**(-7)
x_max = df[['x']].max().round(8)-tol
y_max = df[ ['y']].max().round(8) - tol
x_min = df[['x']].min().round(8)+tol
y_min = df[ ['y']].min().round(8)+tol

back_nodes_mask = df['x'] <= x_min.values[0]
left_nodes = df[back_nodes_mask].sort_values(by ='y', )

front_nodes_mask = df['x'] >= x_max.values[0]
right_nodes = df[front_nodes_mask].sort_values(by ='y', )

bottom_nodes_mask = df['y'] <= y_min.values[0]
bottom_nodes = df[bottom_nodes_mask].sort_values(by ='x', )
top_nodes_mask =df['y'] >= y_max.values[0]
top_nodes = df[top_nodes_mask].sort_values(by ='x', )


left_nodes = left_nodes[ ['id']].values
right_nodes = right_nodes[ ['id']].values
bottom_nodes = bottom_nodes[ ['id']].values
top_nodes = top_nodes[ ['id']].values

left_nodes = np.delete(left_nodes,  [0, left_nodes.shape[0]-1], axis = 0)
right_nodes = np.delete(right_nodes,  [0, right_nodes.shape[0]-1], axis = 0)
bottom_nodes = np.delete(bottom_nodes,  [0, bottom_nodes.shape[0]-1], axis = 0)
top_nodes = np.delete(top_nodes,  [0, top_nodes.shape[0]-1], axis = 0)
# # Run logs
file = 'node_pairs_for_pbc.csv'
file_exists = os.path.isfile(file)
try:
    csvfile = open(file, "w+", newline="")
except:
    print("Can't write in run log file. Creating a templog file", )
csvfile.truncate()
csv_writer = csv.writer(csvfile, delimiter = ',')
csv_writer.writerow( left_nodes.flatten())
csv_writer.writerow(right_nodes.flatten())
csv_writer.writerow(bottom_nodes.flatten())
csv_writer.writerow(top_nodes.flatten())
csvfile.close()