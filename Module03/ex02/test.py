from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor

img_procsr = ImageProcessor()
spb = ScrapBooker()

pingu = img_procsr.load("../assets/happy_pingu.png")
img_procsr.display(pingu)

pingu_crop = spb.crop(pingu, (250, 250), (800, 1500))
img_procsr.display(pingu_crop)

pingu_thin = spb.thin(pingu, 1600, 1)
img_procsr.display(pingu_thin)

pingu_juxtapose = spb.juxtapose(pingu, 2, 0)
img_procsr.display(pingu_juxtapose)

pingu_mosaic = spb.mosaic(pingu, (2, 3))
img_procsr.display(pingu_mosaic)