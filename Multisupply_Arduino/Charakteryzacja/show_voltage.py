import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
from tabulate import tabulate

root = Path('Measurements')


params_l = list()
for data_file in list(sorted(root.glob('*.npy'), key = lambda p: p.stem.split('--')[-1])):
    param = [ p_t.split('=')[1] for p_t in data_file.stem.split('--')[1].split()] #
        
    data = np.load(data_file)
    data = np.transpose(data)
    
    ref_data    = data[0] 
    sensor_data = data[1]  
    
    error = sensor_data - ref_data
    std = np.std(error)
    vpp = abs(np.max(error)-np.min(error))
    
    params_l.append((param[0],std,vpp)) 

    ## SIDE BY SIDE
    
    # plt.figure(figsize=(12.8, 9.6))
    # plt.title(data_file.stem.split('.')[0].split('--')[1])
    # plt.xlabel("Reference (mV)")
    # plt.ylabel("INA219 (mV)")
    # plt.plot(ref_data,sensor_data)
    # # plt.plot()
    # # plt.savefig("./img/"+channel+'_1'+'.png')
    
    ## ERROR
    

    plt.rcParams.update({'font.size': 18})
    plt.figure(figsize=(12.8, 9.6))
    _ = data_file.stem.split('.')[0].split('--')[1]
    plt.title(f'{_}  std: {std:.3f}, vpp: {vpp:.2f}')
    plt.xlabel("Reference (mV)")
    plt.ylabel("INA219 Error(mV)")
    
    plt.plot(ref_data, error,'p')
    
    plt.savefig(root / (data_file.stem +'.png'))
    plt.show()
    
summary = tabulate(params_l, headers=('pg','sadc','std','vpp'))
print(summary)
with open(summary.txt,'w') as f:
    f.write(summary)