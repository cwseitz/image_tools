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
        stack.parse_format()
            

######################
# Image stack objects
#####################

class Stack: 
    def __init__(self, stack,format_str):
        self.format_str = format_str
        self.stack = stack
    def parse_format(self):
        #mandatory format TCXYZ (T used as a tile index for mosaics)
        frmt_ls = self.format_str.split()
        #determine transform needed to make format strings match
        
    def view(self,format_str):
        pass
        
"""
class TiledStack(Stack): 

    def __init__(self, stack):
        super().__init__(stack)
        self.stack = stack

    def stitch(self):

        nt = im.shape[0]
        dx = im.shape[1]
        dy = im.shape[2]
        s = int(np.sqrt(nt))
        new_shape = (int(s*dx), int(s*dy))

        for i in range(1,s+1):
            y = self.stack[(i-1)*s:i*s,:,:]
            y = np.concatenate(y,axis=0).T
            if i == 1:
                x = y
            else:
                x = np.concatenate([x, y],axis=0)
        return x

"""

