import cv2

image = 'signature.jpeg'
img = cv2.imread(image)

if img is None:
  print(f'Error: Could not load image from {image}')
else:
  height, width = img.shape[:2]
  new_width = int(width * 0.75)
  new_height = int(height * 0.75)

  resized_img = cv2.resize(img, (new_width, new_height))
  cv2.imwrite('resized_signature.jpeg', resized_img)

  cropped_img = img[50:250, 100:300]
  cv2.imwrite('cropped_signature.jpeg', cropped_img)

  flipped_img = cv2.flip(img, 1)
  cv2.imwrite('flipped_signature.jpeg', flipped_img)

  print('All images saved successfully.')

  cv2.imshow('Original Image', img)
  cv2.imshow('Resized Image', resized_img)
  cv2.imshow('Cropped Image', cropped_img)
  cv2.imshow('Flipped Image', flipped_img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()