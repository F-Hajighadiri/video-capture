import numpy as np
import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(1)
t0 = time.time()

while True :
    ret, frame = cap.read()

    if ret :
        frame = cv2.flip(frame, 1)

        red = frame.copy()
        red[:, :, 2] = 255
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).reshape(360, 640, 1)
        gray = np.concatenate((gray, gray, gray), 2)
        inv = 255 - frame

        row0 =  np.concatenate((frame, red), axis=1)
        row1 =  np.concatenate((inv, gray), axis=1)
        result = np.concatenate((row0, row1), axis=0)

        cv2.putText(result, "Fatemeh Hajighadiri", (700, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 100, 0), 2)
        cv2.putText(result, "current time :    " + str(datetime.now().time()), (700, 85),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 10, 10), 2)
        t1 = time.time() - t0
        cv2.putText(result, "duration :         " + str(round(t1, 2)), (700, 120), 
        cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 2)
        
        cv2.imshow("my webcam", result)
        q = cv2.waitKey(1)
        if q == ord('q') :
            break


cv2.destroyAllWindows()
cap.release()