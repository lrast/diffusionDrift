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

def runSim(v, D, timesteps=15, particles=30, initial= [0,0] ):
    # runs the simulation for the given parameters

    positions = np.zeros((particles, 2, timesteps))

    current = initialize(particles, initial)
    positions[:,:,0] = current

    for index in range(1, timesteps):
        nextPositions = stepSim(current, v, D, particles)
        positions[:,:, index] = nextPositions
        current = nextPositions

    return positions

