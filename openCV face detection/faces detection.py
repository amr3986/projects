from cv2 import cv2
from mtcnn_cv2 import MTCNN

detector = MTCNN()
cap = cv2.VideoCapture(0)


while (True):
    
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    boxes = detector.detect_faces(frame)

    for box in boxes:
        
        x, y, w, h = box['box']
        conf = box['confidence']
         
 
        if conf > 0.8:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame,str(conf)[:4],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX ,1,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow('Face Detection', frame)
     
 
    key = cv2.waitKey(1) & 0xFF
    # Press `q` to exit
    if key == ord("q"):
        break
 
cap.release()
cv2.destroyAllWindows()