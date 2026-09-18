import cv2

image='C:\\Users\\shour\\Downloads\\OpenCV\\signature.jpeg'
img = cv2.imread(image)

if img is None:
  print(f'Error: Could not load image from {image}')
else:
  cv2.imshow('Loaded Image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  height, width, channels = img.shape
  print('Image Properties:')
  print(f'- Height: {height} pixels')
  print(f'- Width: {width} pixels')
  print(f'- Number of Channels: {channels}')

  signature_copy = 'C:\\Users\\shour\\Downloads\\OpenCV\\signature_copy.jpeg'
  cv2.imwrite(signature_copy, img)
  print(f"Image successfully saved as '{signature_copy}'")