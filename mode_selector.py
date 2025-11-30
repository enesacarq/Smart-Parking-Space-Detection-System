import tkinter as tk

form=tk.Tk()
form.title("Baslangic secimi")
form.geometry("450x400+500+200")
form.configure(bg="#8FE791")


label=tk.Label(form,text="Menü",bg="#8FE791",font=("Arial",20,"bold"))
label.pack()

def mevcut():
    pass

def ekle():
    pass

def yeni():
    pass

#Mevcut Alanları kullan butonu
buton1=tk.Button(form,text="***Mevcut Park Yerlerini Kullan***",fg="white",font=("Arial",17),bg="#0C2A0D",width=30,height=2,command=mevcut())
buton1.place(relx=0.5,y=90,anchor="center")

#Yeni yer ekleme butonu
buton2=tk.Button(form,text="Yeni Park Yeri Ekle",fg="white",font=("Arial",17),bg="#0C2A0D",width=30,height=2,command=ekle())
buton2.place(relx=0.5,y=192,anchor="center")

#Yeniden çizme butonu
buton3=tk.Button(form,text="Park Yerlerini Yeniden Çiz",fg="white",font=("Arial",17),bg="#0C2A0D",width=30,height=2,command=yeni())
buton3.place(relx=0.5,y=294,anchor="center")





form.mainloop()
