import numpy as np
from PIL import Image  # Python imaging library

data = np.zeros((6, 3, 3), dtype=np.uint8)  # h,w,d
data[:] = [20, 180, 200]
# data[:, 1:3] = [230,250,5]#all rows and two columns
data[0:3, 0:1]= [240, 0, 0] # all columns and three uppermost rows(total 6 rows)
img = Image.fromarray(data)
img.save('canvas.png')





