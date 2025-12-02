import cv2
import numpy as np
import json

with open("park_yerleri.json","r") as f:
    park_yerleri=json.load(f)

def yerleri_ciz():
    for item in park_yerleri:
        park_id = item["park_id"]
        pts = np.array(item["pts"], np.int32).reshape((-1,1,2))

        cv2.polylines(img, [pts], True, (0,0,255), 2)

        sol_alt = pts[1][0]  
        yazi_konum = (int(sol_alt[0]) + 5, int(sol_alt[1]) - 7)
        cv2.putText(img, str(park_id), yazi_konum, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1)

cap = cv2.VideoCapture("otopark1.mp4")
ret, img = cap.read()  
img=cv2.resize(img,(1080,720))
cap.release()







cv2.imshow("a",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
