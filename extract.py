import re
import numpy as np
import sys
import matplotlib.pyplot as plt

def extract(fn):
    with open(fn) as f:
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
        return data
data = []

for fn in sys.argv[1:]:
    data.append(extract(fn))

means = np.array([d['avg'] for d in data])

plt.plot(means)
