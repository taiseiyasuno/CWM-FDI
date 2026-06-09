# !/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import sys

# parameters to modify 
filename=f"/home/ubuntu/Documents/CWM/CWM-FDI/assignment2/{sys.argv[1]}.txt"
label='C'
xlabel = 'Time gap (ns)'
ylabel = 'Probability'
fig_name=f'{sys.argv[2]}.png'
bins=100 #adjust the number of bins to your plot

## load data from input file
t = np.loadtxt(filename, delimiter=" ", dtype="float")

per_90 = np.nanpercentile(t, 90)
per_99 = np.nanpercentile(t, 99)

## if your data is "X Y" (2 cols), use the following line
#plt.plot(t[:,0], t[:,1], label=label)  # Plot some data on the (implicit) axes.

## if your data is "X" (1 col), use the following line
#plt.plot(t, label=label)  # Plot some data on the (implicit) axes.

## comment the lines above and uncomment the line below to plot a simple CDF
#plt.hist(t[:], bins, density=True, histtype='step', cumulative=True, label=label)

## comment the lines above and uncomment the 4 lines below for a nicer CDF

if int(sys.argv[3]) == 100:
    ts = np.sort(t)
    title=f'CDF of time gaps (ns) ({label}) (all values)'
elif int(sys.argv[3]) == 99:
    t_99 = t[t <= per_99]
    ts = np.sort(t_99)
    title=f'CDF of time gaps (ns) ({label}) (99th percentile)'
else:
    t_90 = t[t <= per_90]
    ts = np.sort(t_90)
    title=f'CDF of time gaps (ns) ({label}) (90th percentile)'

n = np.arange(1,len(ts)+1) / float(len(ts))

fig, ax = plt.subplots()
ax.step(ts,n)

print(f"Min is {np.min(t)}, max is {np.max(t)} ns")
print(f"Average is {np.mean(t)} ns")
print(f"90th percentile value: {per_90} ns")
print(f"99th percentile value: {per_99} ns")
print(f"Number of 0 check: {np.count_nonzero(t==0)}")

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend()
plt.savefig(fig_name)
plt.show()
