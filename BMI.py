import tkinter

window= tkinter.Tk()
window.title("BMI hesaplama")
window.minsize(300,300)
def bmi_hesapla():
    try:
        agirlik_sayi=int(agirlik_entry.get())
        boy_sayi=int(boy_entry.get())
        sonuc=agirlik_sayi/((boy_sayi*boy_sayi)/10000)

        if sonuc <18.5:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       Zayıfsınız")
            hesapla_label.pack()
        elif 18.5 <= sonuc < 25:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       Normal ağırlık")
            hesapla_label.pack()
        elif 25<= sonuc <30:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       Kilolu ")
            hesapla_label.pack()
        elif 30 <= sonuc <35:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       1. Dereceden Obezite ")
            hesapla_label.pack()
        elif 35 <= sonuc <40:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       2. Dereceden obezite ")
            hesapla_label.pack()
        else:
            hesapla_label = tkinter.Label(text=f"BMI değeriniz: {sonuc:.2f}       3. Dereceden obezite")
            hesapla_label.pack()
    except:
        hesapla_label=tkinter.Label(text="Lütfen girilen değerleri kontrol edin.")
        hesapla_label.pack()


agirlik_label=tkinter.Label(text="Lütfen ağırlığınızı Girin (kg)")
agirlik_label.pack()
agirlik_entry=tkinter.Entry()
agirlik_entry.pack()

boy_label=tkinter.Label(text="Lütfen boyunuzu Girin (cm)")
boy_label.pack()
boy_entry=tkinter.Entry()
boy_entry.pack()

hesapla=tkinter.Button(text="Hesapla",command=bmi_hesapla)
hesapla.pack()

#agirlik.config()  ayarladığın şeyleri sonradan değiştirmeye yarar


window.mainloop()