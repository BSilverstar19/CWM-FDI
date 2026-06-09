# NOTE: This is code generated using ChatGPT 5.5

import re
import numpy as np

times = []

with open("ping_3.log") as f:
    for line in f:
        m = re.search(r'time=([0-9.]+)', line)
        if m:
            times.append(float(m.group(1)))

times = np.array(times)

np.savetxt("times.txt", times)
