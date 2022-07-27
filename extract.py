import re
import numpy as np
import sys

with open(sys.argv[1]) as f:
    filedata = f.read() #File mustn't be too big (size < RAM available)
    lines = filedata.splitlines()
    data = {}
    # Getting aggregated values
    regexp = r'Minimum \[W\],([^\n]+)\nMaximum \[W\],([^\n]+)\nMean \[W\],([^\n]+)\nStandard Deviation \[W\],([^\n]+)'
    raw_data = re.search(regexp, filedata).groups()
    data['min'] = float(raw_data[0])
    data['max'] = float(raw_data[1])
    data['avg'] = float(raw_data[2])
    data['std'] = float(raw_data[3])
    value_begin = lines.index("--Graph Data--") + 1
    raw_power_values = lines[value_begin + 1:]
    data['val'] =  np.genfromtxt(raw_power_values, delimiter=',', dtype = float)

#put analysis code here
