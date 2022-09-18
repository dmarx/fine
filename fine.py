#https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf
#!nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.free,memory.used --format=csv 

import pandas as pd
import subprocess

    
def gpu_info():
    outv = subprocess.run(['nvidia-smi', '--query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.free,memory.used', '--format=csv'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    header, rec = outv.split('\n')[:-1]
    return pd.DataFrame({k:v for k,v in zip(header.split(','), rec.split(','))}, index=[0]).T
