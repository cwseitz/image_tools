import numpy as np
from skimage.io import imread

###############################################
# 
# This is a collection of functions for
# manipulating image stacks generated using 
# MicroManager v1.4
#
################################################

################################################
# A collection of individual images or stacks
################################################

class Collection:
    def __init__(self, files):
        self.files = files
        self.images = []
        self.read_collection()
    def read_collection(self):
        for file in self.files:
             self.images.append(imread(file))
    def to_stack(self,format_str):
        self.images_ = np.array(self.images)
        stack = Stack(self.images_,format_str)
        return stack
            

######################
# Image stack objects
#####################

class Stack: 
    def __init__(self,stack,format_str,base_str='PTZCXY'):
        self.data = stack
        self.format_str = format_str
        self.base_str = base_str
        self.parse_format()
        self.np,self.nt,self.nz,self.nc,self.nx,self.ny = self.data.shape
    def parse_format(self):
        self.format = np.array([1 if x in self.format_str else 0 for x in self.base_str])
        self.fidx = np.argwhere(self.format == 0).flatten()
        self.data = np.expand_dims(self.data,tuple(self.fidx))
    def tile(self,snake=False):
        tile_dim = int(np.sqrt(self.np))
        tiled = self.data.reshape(tile_dim,tile_dim,self.nx,self.ny)
        tiled = tiled.swapaxes(1, 2)
        tiled = tiled.reshape(self.nx*tile_dim, self.ny*tile_dim)
        return tiled


