import tkinter as tk
from p1 import *
import threading
def komut():
 e1 = eposta1.get()
 e2 = eposta2.get()
 s1 = sifre.get()
 t1 = threading.Thread(target=program1,args=(e1,e2,s1))
 t1.start()


pencere2 = tk.Tk()
pencere2.title("project whatsapp")
pencere2.iconbitmap("")
pencere2.geometry("500x500")
pencere2.maxsize(500, 500)
pencere2.minsize(500, 500)
pencere2.configure(background="#ffd104")
yazi1 = tk.Label(text="e-posta 1", bg="#ffd104")
yazi1.place(x=20, y=50)
eposta1 = tk.Entry(width=30)
eposta1.place(x=130, y=50)

yazi2 = tk.Label(text="şifre", bg="#ffd104")
yazi2.place(x=20, y=90)
sifre = tk.Entry(width=30)
sifre.place(x=130, y=90)

yazi3 = tk.Label(text="e-posta 2", bg="#ffd104")
yazi3.place(x=20, y=130)
eposta2 = tk.Entry(width=30)
eposta2.place(x=130, y=130)

dugme = tk.Button(text="BAŞLAT", command=komut, bg="#7cd752", width=10)
dugme.place(x=215, y=250)

aciklama=tk.Label(text="kullanım:program başladıktan sonra 30 saniye içerisinde whatsapp web e giriş yapıp\n malum kişinin sohbetini açınız ve bekleyiniz çevrimiçi olduğunda size bildirim gelecektir\nAçıklama bu uygulamayı kullanabilmek için google güvenlik ayarlarından daha az güvenilir\n uygulamalara izin verilmelidir(iki aşamalı doğrulama kapalı olmalıdır)",width=71,height=10,bg="#ffd104")
aciklama.place(x=0,y=300)
pencere2.mainloop()