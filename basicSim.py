# runs the initial simulation of drift diffusion
import numpy as np


def initialize( particles, initial):
    positions = np.zeros([particles,2])
    positions[:,:] = initial
    return positions

def getDeltas(v, D, particles):
    mean = v.squeeze();
    covs = D * np.eye(2)
    return np.random.multivariate_normal(mean, covs, (particles) )

def stepSim(current, v, D, particles):
    nextSpots = current + getDeltas(v, D, particles)
    return nextSpots

def makeHists(positions, xyind):
    # set up the bins of the histogram
    histmin = int( np.min(positions[:,xyind,:])) -1
    histmax = int( np.max(positions[:,xyind,:])) +1
    bins = np.linspace(histmin, histmax, histmax-histmin+1)
    middles = 0.5 + bins[:-1]

    # one dictionary per time point
    fullList = []
    for timepoint in range(positions.shape[2]):
        currDict = {middles[i]: np.histogram( positions[:,xyind,timepoint], bins)[0][i] for i in range(len(middles)) }
        fullList.append(currDict)

    return fullList



def runSim(v, D, timesteps=15, particles=30, initial= [0,0]):
    # runs the simulation for the given parameters

    v = np.array(v)

    positions = np.zeros((particles, 2, timesteps))

    current = initialize(particles, initial)
    positions[:,:,0] = current

    for index in range(1, timesteps):
        nextPositions = stepSim(current, v, D, particles)
        positions[:,:, index] = nextPositions
        current = nextPositions


    xyhist = {'x': makeHists(positions, 0), 'y': makeHists(positions, 1) }

    return positions, xyhist

