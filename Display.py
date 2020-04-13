import matplotlib.pyplot as plt
import numpy as np


class Display:
    def __init__ (self):
        self.metrics = []

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

    def showplot (self):
        npMetrics = np.array(self.metrics)
        plt.plot(npMetrics[:,1],npMetrics[:,2], ',')

        plt.show()
