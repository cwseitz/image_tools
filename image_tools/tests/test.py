from image_tools.image import Collection
from glob import glob
from skimage.io import imread
import matplotlib.pyplot as plt

"""
Make sure you run stack to hyperstack in ImageJ beforehand
Either figure out how to save as hyperstack in uM or do this
for every stack
"""

files = sorted(glob('/home/cwseitz/Desktop/20220708_Tile-10pct-Overlap/*.tif'))
print(files) #ensure it is sorted
collection = Collection(files)
stack = collection.to_stack(format_str='PXY')
tiled = stack.tile()
plt.imshow(tiled)
plt.show()

