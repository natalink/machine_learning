import numpy
import matplotlib.pyplot as plt

a = numpy.loadtxt("subject101.dat")

b=numpy.transpose(numpy.vstack((a[:,1],a[:,2])))

c=b[~(numpy.isnan(b[:,1]))]

#print b[0]

#print c[:,1]

plt.scatter(c[:,0],c[:,1])

plt.show()