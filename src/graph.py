import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import numpy as np

with open('../figures/objects_magntiude.txt', 'r') as file:
    lines = file.readlines()
    magnitudes = []
    for line in lines[1:]:
        columns = line.split()
        try:
            if columns[6]!="nan":
                magnitudes.append(float(columns[6]))
        except:
            continue

magnitudes= sorted(magnitudes)


x=[]
y=[]
y_e = []
for i in range(0,len(magnitudes),20):
    i += 1
    if 8<magnitudes[i]<100:
        x.append(magnitudes[i])
        #if magnitudes[i]<11.6:
            #print(i)
        y.append(math.log(i+1,10))
        y_e.append(1/(np.sqrt(i+1)*math.log(10,math.e)))



#print(x)

def log_mag(m):
    return 0.6*m 

def line(a,m,c):
    return m*a +c

def exp_dec(x,c,d):
    a=x
    return np.log(a-d) +c

def split_line(x,m1,c1,m2,c2,d):
    if x<d:
        return m1*x+c1
    else:
        return m2*x+c2

y2=[]
for x1 in x:
    y2.append(log_mag(x1))

x=np.array(x)
y=np.array(y)

x_f = x[:45]
x_s = x[45:]
y_f = y[:45]
y_s = y[45:]

po,po_cov = curve_fit(line,x,y)

plt.errorbar(x,y,yerr = y_e,fmt = "x")

plt.plot(x,line(x,po[0],po[1]))
ax = plt.gca()
ax.tick_params(axis='both', which='both', labelsize=12)

plt.xlabel("Magnitude", fontsize=14)
plt.ylabel("Logarithm of the Number of Galaxies", fontsize=14)
plt.grid()
plt.legend(["Line of Best Fit", "Data"], fontsize=10)
plt.savefig("../figures/plots/magnitudes.png")

print(f"The gradient is: {po[0]} +- {np.sqrt(po_cov[0][0])}")
print(f"The y-intercept is: {po[1]} +- {np.sqrt(po_cov[1][1])}")