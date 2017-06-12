from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

tsv1 = Image.open('TSV_jan03_natCol.jpg')
tsv2 = Image.open('TSV_jan15_natCol.jpg')

imarr1 = np.array(tsv1)
imarr2 = np.array(tsv2)

diff = imarr1 - imarr2

diffIm = Image.fromarray(diff)

diffIm.show()
