import cv2
import numpy as np

print("import finised")

vid = cv2.VideoCapture(0)
image_size=512
read_size=40
text=["#","=",": ",". "]

while(True):
        ret, frame = vid.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('vid',frame)
        ratio=frame.shape[1]/frame.shape[0]
        frame = cv2.resize(frame,dsize=(round(ratio*read_size),read_size), interpolation=cv2.INTER_CUBIC)
        image = np.zeros((image_size,round(ratio*image_size)), np.uint8)
        line=1
        for a in frame:
                col=""
                for b in a:
                        col+=text[round((b/255)*len(text))-1]
                image = cv2.putText(image, col, org=(0,round((line/read_size)*image_size)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255), thickness=1)
                line=line+1
        cv2.imshow('frame', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
vid.release()
cv2.destroyAllWindows()

