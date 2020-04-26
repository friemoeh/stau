import matplotlib.pyplot as plt
import numpy as np


class Display:
    def __init__ (self):
        self.metrics = []
        self.npMetrics =  np.array([])
        self.package=50

    def addmetric (self,metric):
        self.metrics.append (metric)

    def showtimeplot (self):
        npMetrics = np.array(self.metrics)
        plt.xlabel('time')
        plt.plot(npMetrics[:,0],npMetrics[:,1], label = "Traffic Density")
        plt.plot(npMetrics[:,0],npMetrics[:,2], label = "Average Speed")
        plt.plot(npMetrics[:,0],npMetrics[:,3], label = "Traffic Intensity")

        plt.legend()
        plt.show()

    def subsample(self):
        tempMetrics = np.array(self.metrics)
        numRows = tempMetrics.shape[0]
        print("Num Rows: ", numRows)
        tempMetrics2 = []

        for i in range(0,numRows, self.package):
            bla = np.mean(tempMetrics[i:i+self.package, :],0)
            tempMetrics2.append(bla)
        self.npMetrics = np.array(tempMetrics2)

    def showplot (self):
        plt.figure()
        plt.subplot(221)
        plt.xlabel('speed')
        plt.ylabel('intensity')
        plt.plot(self.npMetrics[:,2],self.npMetrics[:,3], ',')
        z = np.polyfit(self.npMetrics[:,2],self.npMetrics[:,3],2)
        f = np.poly1d(z)
        x=np.linspace(min(self.npMetrics[:,2]),max(self.npMetrics[:,2]), 100)
        plt.plot(x,f(x), 'b')

        plt.subplot(222)
        plt.xlabel('density')
        plt.ylabel('intensity')
        plt.plot(self.npMetrics[:,1],self.npMetrics[:,3], ',')
        z = np.polyfit(self.npMetrics[:,1],self.npMetrics[:,3],2)
        f = np.poly1d(z)
        x=np.linspace(min(self.npMetrics[:,1]),max(self.npMetrics[:,1]), 100)
        plt.plot(x,f(x), 'b')

        plt.subplot(224)
        plt.xlabel('density')
        plt.ylabel('speed')
        plt.plot(self.npMetrics[:,1],self.npMetrics[:,2], ',')
        z = np.polyfit(self.npMetrics[:,1],self.npMetrics[:,2],2)
        f = np.poly1d(z)
        x=np.linspace(min(self.npMetrics[:,1]),max(self.npMetrics[:,1]), 100)
        plt.plot(x,f(x), 'b')


        plt.show()
