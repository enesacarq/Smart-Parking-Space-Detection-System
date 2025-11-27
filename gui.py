import tkinter as tk

#Ana pencere
pencere=tk.Tk()
pencere.title("Smart Parking Sytem")
pencere.geometry("1024x720+250+50")

#Kamera1 butonu
def kamera1():
    pass
buton1=tk.Button(pencere,text="Kamera1",fg="white",bg="#234C6A",activebackground="#327093")
buton1.place(x=10,y=15,width=200)


#Kamera2 butonu
def kamera2():
    pass

buton2=tk.Button(pencere,text="Kamera2",fg="white",bg="#234C6A",activebackground="#327093")
buton2.place(x=220,y=15,width=200)

#Kamera3 butonu
def kamera3():
    pass

buton3=tk.Button(pencere,text="Kamera3",fg="white",bg="#234C6A",activebackground="#327093")
buton3.place(x=430,y=15,width=200)

#Analiz frame 
frame1=tk.Frame(pencere,bg="#86C0E9",width=374,height=700)
frame1.place(x=640,y=15)



#Bilgi ekranı frame
frame2=tk.Frame(frame1,bg="white",width=354,height=50)
frame2.place(x=10,y=10)

#Bilgi ekranı labeli
bilgiekranlabel=tk.Label(frame2,text="BİLGİ EKRANI",font=("Arial",30),bg="white")
bilgiekranlabel.place(relx=0.5,rely=0.5,anchor="center")






#Dolu frame
frame3=tk.Frame(frame1,bg="white",width=172,height=140)
frame3.place(x=10,y=70)

#Dolu labeli
dolulabel=tk.Label(frame3,bg="white",text="DOLU",font=("Arial",30))
dolulabel.place(relx=0.5,anchor="n")

#Dolu sayısı
dolusayi=tk.Label(frame3,bg="white",text="20",font=("Ariel",40))
dolusayi.place(relx=0.5,rely=0.90,anchor="s")






#Boş frame
frame4=tk.Frame(frame1,bg="white",width=172,height=140)
frame4.place(x=192,y=70)

#Boş labeli
boslabel=tk.Label(frame4,bg="white",text="BOŞ",font=("Arial",30))
boslabel.place(relx=0.5,anchor="n")

#Boş sayısı
bossayi=tk.Label(frame4,bg="white",text="20",font=("Ariel",40))
bossayi.place(relx=0.5,rely=0.90,anchor="s")








#Doluluk frame
frame5=tk.Frame(frame1,bg="white",width=354,height=50)
frame5.place(x=10,y=220)

#Doluluk labeli
doluluklabel=tk.Label(frame5,text="Doluluk= %50",font=("Arial",30),bg="white")
doluluklabel.place(relx=0.5,rely=0.5,anchor="center")





#Pencereyi kapat
pencere.mainloop()
