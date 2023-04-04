from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor

img_procsr = ImageProcessor()
cf = ColorFilter()

pingu = img_procsr.load("../assets/happy_pingu.png")
img_procsr.display(pingu)

# pingu_invert = cf.invert(pingu)
# img_procsr.display(pingu_invert)

pingu_blue = cf.to_blue(pingu)
img_procsr.display(pingu_blue)