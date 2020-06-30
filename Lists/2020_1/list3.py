import numpy as np
import random
import time
import multiprocessing
import pandas as pd
import utils

def get_sample(s, k):
	space = np.array(s)
	n = space.shape[0]    

	k = n if k > n else k

	for i in np.arange(k):        
		j = int(random.uniform(0, n-1))
		temp = space[j]
		space[j] = space[n-1-i]
		space[n-1-i] = temp
		
	return space[:k]

def run_experiment(param_dict):
    
    start = time.time()

    n_runs = np.arange(1e3)
    progbar = utils.ProgressBar()
    space = list(np.arange(param_dict['n']))
    k = int(param_dict['k'])
    
    # Running the experiment n_runs times
    for run in n_runs:
        progbar.update_progress(run/(n_runs.shape[0]-1))
        get_sample(space, k)        

    param_dict['elapsed_time'] = time.time() - start

    return param_dict


param_dict = []

array_n = [1e8, 1e6, 1e4]
array_k = [1e4, 1e3, 1e2, 1e1]

for n in array_n:    
    for k in array_k:
        param_dict.append({'n': n, 'k': k})

for i, param in enumerate(param_dict):
	print ('\n[{}/{}]: {}'.format(i+1, len(param_dict), param))
	result = run_experiment(param)
	param_dict[i] = result
	np.save('./temp/param_dict.npy', param_dict)

df = pd.DataFrame.from_dict(param_dict)
print (df)
df.to_csv('./temp/df_elapsed_time.csv', sep=';', index=None)

print ("PODE DESLIGAR O PC, MAYARA!!!!!!!")