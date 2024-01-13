from pathlib import Path
import numpy as np
import time, json, os
from datetime import datetime

DELAY = 3

# program configuration
cfg_file_path = list(Path('.').glob('configuration_*.py'))[0]
print('Program configuration: ',cfg_file_path.stem)
with open(cfg_file_path) as f:
    prog_config = f.read()
    exec(prog_config)

# devices creation
stimulus         = Stimulus()
meter_under_test = MeterUnderTest()
meter_reference  = MeterReference()

for dev_under_test_config in map(lambda l: l.strip('#'), filter(lambda l: l.startswith('#'),prog_config.splitlines())):    

    # device configuration
    
    meter_under_test.config(dev_under_test_config)
    print('Device configured: ',dev_under_test_config,'\n')
    
    # calibration
    stim_value = list(stimulus_range)[-1]
    stimulus.set(stim_value)
    time.sleep(1*DELAY)
    ref_value = meter_reference.measure()
    meter_under_test.callib(ref_value)
    test_value = meter_under_test.measure()
    print(f'calibrated at')
    print(f'S:{stim_value}, R:{ref_value:0.3f}, T:{test_value:0.3f}, E:{(ref_value-test_value):0.3f}')
    print()
    
    time.sleep(1*DELAY)
        
    # acquisition
    print(f'measurement ')
    measurement = list()
    for stim_value in stimulus_range:
        stimulus.set(stim_value)
        time.sleep(1*DELAY)
        ref_value = meter_reference.measure()
        test_value = meter_under_test.measure()
        measurement.append((ref_value,test_value))
        print(f'S:{stim_value}, R:{ref_value:0.3f}, T:{test_value:0.3f}, E:{(ref_value-test_value):0.3f}')
    
    # archivization
    date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S")
    path = Path('Measurements') / f'{date}--{dev_under_test_config}.npy'
    os.makedirs(path.parent,exist_ok=True )
    np.save(path, np.array(measurement))
    print(f'Data saved in "{path}"\n')

