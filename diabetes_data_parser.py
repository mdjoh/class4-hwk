import numpy as np

filename = 'diabetes_data.txt'

# import dataset to a numpy array called data
data = np.genfromtxt(filename, delimiter='\t', skip_header=1)

# reach homework - calculating means and std dev. for each column in dataset
means = np.mean(data, axis=0)
print(means)

stdevs = np.std(data, axis=0)
print(stdevs)
