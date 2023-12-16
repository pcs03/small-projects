import cv2

img = cv2.imread("./pixelart.png", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Couldn't load image")

image = img.tolist()
for line in image:
    print("".join(list(map(str, line))))
