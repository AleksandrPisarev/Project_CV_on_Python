import cv2

# программа считывает видеопоток с веб-камеры по нажатию на пробел
# запоминает кадр в video.jpg по нажатию Esc завершает работу
# Для работы с программой необходимо скачать OpenCV pip install opencv-python

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Не удалось открыть камеру")
    exit()
while(True):
    ret, im = cap.read()
    if not ret:
        print("Не удалось получить кадр")
        break
    cv2.imshow('Video', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('video.jpg', im)