import numpy as np

bases = np.array([256, 128, 64, 32, 16, 8, 4, 2, 1])

algorithm, data = open('input.txt').read().strip().split('\n\n')
algorithm = [1 if c =='#' else 0 for c in algorithm.strip()]
data = np.array([[1 if c =='#' else 0 for c in line] for line in data.strip().split('\n')])
data = np.pad(data, 3, constant_values=0)
for it in range(50):
    data = np.pad(data, 2, mode='reflect')
    new_data = np.zeros((data.shape[0]-2, data.shape[1]-2))
    for x in range(data.shape[0]-2):
        for y in range(data.shape[1]-2):
            index = int(data[x:x+3,y:y+3].flatten() @ bases.T)
            new_data[x,y] += algorithm[index]
    data = new_data
print(int(np.sum(data)))
