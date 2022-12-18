import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

vid = cv2.VideoCapture('walking.avi')

while(True):

    ret, frame = vid.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = faceCascade.detectMultiScale(grey)
    print(bodies)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  
    # Display the resulting frame
    cv2.imshow("Web cam", frame)

    if cv2.waitKey(25) == 32:
        break

vid.release()

cv2.destroyAllWindows()
