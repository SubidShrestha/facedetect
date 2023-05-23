import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

while True:
    cam = cv2.VideoCapture(0)
    result, img = cam.read()
    text = "Face not detected"
    if result:
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

        for (x, y, w, h) in face:
            text = "Face Detected"
            cv2.rectangle(img, (x, y), (x + w, y + h), (2, 250, 2), 2)
        
        image = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Face Detection", image)
    
    key = cv2.waitKey(10)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()