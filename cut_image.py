import cv2

img = cv2.imread(r'F:\cvcv.png')
dst = img[3:-1, 0:-1]   # 裁剪坐标为[y0:y1, x0:x1]
cv2.imshow('image',dst)
cv2.imwrite('F:\cvcv1.png', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
