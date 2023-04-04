from ImageProcessor import ImageProcessor

img_procsr = ImageProcessor()

print("test1______________________")
bad_data = img_procsr.load("non_existing.png")
img_procsr.display(bad_data)

print()

print("test2______________________")
good_data = img_procsr.load("../assets/happy_pingu.png")
img_procsr.display(good_data)
print(good_data)