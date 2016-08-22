import scipy.io
import numpy as np

# matfile: name of the matlab file which has the variables
# keyname: name of the variable which is present in the matlab file.
# returns the contents held by the variable <keyname>
# Error handling not done so far. Please make necessary changes.

def parsematlabFile(matfile,keyname):
    #  x contains a list of segments that are created from matlab file createSegmentsFromFile.m
    x=scipy.io.loadmat(matfile)
    return x.get(keyname)

allFives=parsematlabFile('results.mat','allFives')
allFours=parsematlabFile('results.mat','allFours')
allThrees=parsematlabFile('results.mat','allThrees')
allTwos=parsematlabFile('results.mat','allTwos')

