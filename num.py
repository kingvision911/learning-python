
from sys import argv, exit
import os
import numpy as np

app_path = os.path.dirname(os.path.realpath(__file__))

if len(argv) < 4+1:# argv[0] is the script name itself
    print('error: Need 4 command line arguments!')
    print('User provided only %d.' % len(argv))
    exit(1)
else:
    out_file = argv[1]
    N_loops = int(argv[2])
    value1 = float(argv[3])
    value2 = float(argv[4])

print('Echo commandline inputs back to user:')
print('argv[0] = %s' % argv[0])
print('argv[1] = %s' % out_file)
print('argv[2] = %d' % N_loops)
print('argv[3] = %6.4f' % value1)
print('argv[4] = %6.4f' % value2) 

print('FYI, the path to your script is:')
print('%s' % app_path)

output_data = np.zeros((N_loops,2))
for k in xrange(N_loops):
    output_data[k,0] = value1 + k*10.0
    output_data[k,1] = (value1 + k*10.0)/value2
    np.savetxt(app_path + out_file,output_data)
