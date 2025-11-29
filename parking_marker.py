import cv2
import numpy as np
import json 


noktalar = []  #kordinatların ilk seçimi
son_dortgen=[] #en son işaretlenen dörtgen
park_yerleri=[] #ParkYeri sınıfının nesnelerini tutan liste
park_id=1 #Park numarları

#Park yerlerinin bilgilerini tutan sınıf
class ParkYeri:
    def __init__(self,park_id,pts):
        self.park_id=park_id
        self.pts=pts

#Dörtgenin daha doğru çizilmesi için ek fonksiyon-sıralar
def sirala_noktalar(noktalar):
    noktalar = np.array(noktalar)
    toplam = noktalar.sum(axis=1)
    fark = np.diff(noktalar, axis=1).flatten()
    
    sol_ust = noktalar[np.argmin(toplam)]
    sag_alt = noktalar[np.argmax(toplam)]
    sol_alt = noktalar[np.argmin(fark)]
    sag_ust = noktalar[np.argmax(fark)]
    
    return [sol_ust, sag_ust, sag_alt, sol_alt]


#Mouse tıklamalarının ana fonksiyonu -çizimler
def mouse(event, x, y, flags, params):
    global noktalar,son_dortgen,park_id,park_yerleri  #Bu değişkenleri değiştirebilmek için globale alıyoruz
    if event == cv2.EVENT_LBUTTONDOWN:
        noktalar.append((x, y))
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

        #4 köşe seçildiyse çizer ve kayıt eder
        if len(noktalar) == 4:
            sirali = sirala_noktalar(noktalar)
            pts = np.array(sirali, np.int32).reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (0, 0, 255), 2)
            son_dortgen = pts.copy()  # Son dörtgeni kaydet
            noktalar.clear()  #noktaları sıfırla
        
            park_yerleri.append(ParkYeri(park_id,pts)) #ana kayıt listesine Nesneyi ekleme

            sol_alt = pts[1][0]   
            yazi_konum = (int(sol_alt[0]) + 5, int(sol_alt[1]) - 7) #Idnin yazılacağı konumu ayarlamak
            cv2.putText(img, str(park_id),yazi_konum, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
            park_id+=1
    #Sağ tıklama ile son dörtgenin aynı boyutlarında çizen ve kaydeden        
    elif event == cv2.EVENT_RBUTTONDOWN:
        if son_dortgen is not None:
    
            offset = np.array([x - son_dortgen[0][0][0], y - son_dortgen[0][0][1]])
            yeni_pts = son_dortgen + offset
            cv2.polylines(img, [yeni_pts], True, (0, 0, 255), 2)

            park_yerleri.append(ParkYeri(park_id, yeni_pts))#ana kayıt listesine Nesneyi ekleme

            sol_alt=yeni_pts[1][0]
            yazi_konum=(int(sol_alt[0])+5,int(sol_alt[1])-7)#Idnin yazılacağı konumu ayarlamak
            cv2.putText(img, str(park_id), yazi_konum, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
            park_id+=1
            




img = cv2.imread("fotopark.png")
cv2.namedWindow("isaret")
cv2.setMouseCallback("isaret", mouse)




while True:
    cv2.imshow("isaret", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break
cv2.destroyAllWindows()

park_data = []
for p in park_yerleri:
    pts_list = p.pts.reshape(-1,2).tolist()
    park_data.append({"park_id": p.park_id, "pts": pts_list})

with open("park_yerleri.json", "w") as f:
    json.dump(park_data, f, indent=4)

print("Park yerleri JSON dosyasina kayit edildi.")