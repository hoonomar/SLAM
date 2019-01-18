import numpy as np
import cv2


cap = cv2.VideoCapture('drive.mp4')
while(cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 

orb = cv2.ORB_create()
kp, des  = orb.detectAndCompute(frame, None)
for p in kp:
    u,v = map(lambda x: int(round(x)), p.pt)
    cv2.circle(frame, (u,v), color=(0,255,0), radius=3)


cap.release()
cv2.destroyAllWindows()




