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








#Pencereyi kapat
pencere.mainloop()
