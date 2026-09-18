import cv2

image = 'signature.jpeg'
img = cv2.imread(image)

if img is None:
  print(f'Error: Could not load image from {image}')
else:
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  cannyedge_img = cv2.Canny(gray_img, 100, 200)

  cv2.imshow('Original Image', img)
  cv2.imshow('Grayscale Image', gray_img)
  cv2.imshow('HSV Image', hsv_img)
  cv2.imshow('Canny Edges', cannyedge_img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()