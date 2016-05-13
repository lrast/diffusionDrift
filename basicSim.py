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
    histmin = np.min(positions[:,xyind,:])
    histmax = np.max(positions[:,xyind,:])
    delta = (histmax - histmin) / 21
    bins = np.linspace(histmin, histmax, 21)  # we want 20 bins total

    # one dictionary per bar per time point

    fullList = []
    for timepoint in range(positions.shape[2]):
        currPoints = [ { 't': timepoint, 'dx': delta, 'x': bins[i], 'y': np.histogram( positions[:,xyind,timepoint], bins)[0][i]} for i in range(len(bins[:-1]))  ] 
        fullList.extend(currPoints)

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

