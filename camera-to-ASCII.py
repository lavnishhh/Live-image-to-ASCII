import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
font = ImageFont.truetype("RobotoMono-Bold.ttf", 10)  

print("import finised")
print("press 'q' to end program")
image_size=512  #video ouput size for one dimesnion, other dimesnion is in ratio with second dimension of camera video
read_size=40 #number of vertical lines of ASCII in each frame
text=["#","=",":","."," "," "," "] #5 shades of grey, darkest 3 shades of grey are taken as the same shade

vid = cv2.VideoCapture(0)
while(True):
        ret, frame = vid.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('vid',frame)
        ratio=frame.shape[1]/frame.shape[0]
        frame = cv2.resize(frame,dsize=(round(ratio*read_size)*2,read_size), interpolation=cv2.INTER_CUBIC)
        img = Image.fromarray(np.zeros((image_size,round(ratio*image_size)), np.uint8))
        line=1
        draw=ImageDraw.Draw(img)
        draw.text((50,50),"hello",font=font,align="right")
        for a in frame:
                col=""
                for b in a:
                        col+=text[round((b/255)*len(text))-1]
                draw.text((0,round((line/read_size)*image_size)),col,font=font,align="left",fill=(255))
                line=line+1
        
        cv2.imshow('frame', np.array(img))
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
vid.release()
cv2.destroyAllWindows()
