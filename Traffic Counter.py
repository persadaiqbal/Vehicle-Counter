import cv2
subtractor = cv2.createBackgroundSubtractorMOG2()
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cap = cv2.VideoCapture("traffic.mp4")
mobil = 0
tampak = 0
ada = False
count = 0
while(True):
    ret, frame = cap.read()
    mask = subtractor.apply(frame)
    mask = cv2.GaussianBlur(mask.copy(), (5, 5), 0)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, (5,5))
    mask = cv2.inRange(mask, 140, 255)
    conts, p = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    tampak = 0
    for cnt in conts:
        if (cv2.contourArea(cnt) > 300):
            x, y, w, h = cv2.boundingRect(cnt)
            if y > 200:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "count : "+str(count), (30, 30), font, 1,(255, 0, 0), 1, cv2.LINE_AA)
            cv2.line(frame, (0, 300), (510, 300), (0, 0, 255), 2)
            if (y > 300 and y < 360):
                tampak += 1
                if mobil < tampak:
                    mobil = tampak
    if (tampak == 0 and ada == False):
        pass
    elif (tampak == 0 and ada):
        ada = False
        mobil = 0
        count+=1
    elif (tampak > 0 and ada == False):
        ada = True
    cv2.imshow("Car Counter Monitoring [tekan q untuk keluar]", frame)
    if cv2.waitKey(29) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()