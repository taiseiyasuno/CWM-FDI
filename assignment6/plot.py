import numpy as np
from matplotlib import pyplot as plt

# replace with indep var values
x = np.array([1,3])

# FOR TIMES
# replace with the log file we are reading from
# time = np.zeros(len(x))

# with open("assignment6/logs/log_channels.txt") as f: 
#     for i, line in enumerate(f):
#         time[i] = float(line)

# plt.plot(x, time,marker='o')

# # replace with independent var
# plt.xlabel("Channel size (n x n px)")
# plt.ylabel("Minimum time taken (s)")

# # replace with title
# plt.title("Effect of kernel size on runtime")
# plt.show()

# FOR ENERGIES (comment out as necessary)
# Fill in with the values we got
# energy = np.array([9.00, 13.24, 21.07, 32.34, 48.08, 67.52])
# plt.plot(x, energy,marker='o')

# # replace with independent var
# plt.xlabel("Kernel size (n x n px)")
# plt.ylabel("Minimum energy used (J)")

# # replace with title
# plt.title("Effect of kernel size on energy")
# plt.show()



# overall LOOPS plots
ops = np.array([31212, 43200, 67500, 120000, 121203, 270000, 360000, 1058508, 1080000, 2430000, 3000000, 4320000, 5880000, 6750000, 9720000, 14520000])
ops_times = np.array([0.008834830000523652, 0.012250640999809548, 0.01914842500082159, 0.06296625599952677, 0.03441963699970074, 0.07648958699974173,0.102837763000025,0.2989224060002016,0.30683478900027694,0.7011209960000997,0.7884674560000349,1.2810147820000566,1.5035275600002933,2.023473797999941,2.914380641000207,3.6436495789994297])
ops_energies = np.array([6.63, 6.86, 7.58, 9.00, 8.55, 9.26, 9.66, 13.29, 13.17, 19.83, 21.07, 28.63, 32.34, 43.31, 58.24, 67.52])
fig, ax = plt.subplots(1,2)

ax[0].plot(ops,ops_times,marker='o')
ax[1].plot(ops,ops_energies,marker='o')

ax[0].set_xlabel("Number of loops")
ax[0].set_ylabel("Minimum time taken (s)")
ax[1].set_xlabel("Number of loops")
ax[1].set_ylabel("Minimum energy used (J)")
ax[0].set_title("Operations vs runtime")
ax[1].set_title("Operations vs energy")

plt.show()