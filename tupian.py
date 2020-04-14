import cv2

path = r'C:\Users\Kevinliu\AppData\Local\Programs\Python\Python37\Scripts\trump.jpg'
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)

cv2.imwrite("./output_trump.jpg", edges)