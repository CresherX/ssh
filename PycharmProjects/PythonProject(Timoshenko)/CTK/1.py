from pathlib import Path
import datetime
from PIL import Image
import customtkinter as ctk
from customtkinter import set_default_color_theme
useless_date_title = ['111','222','333','444']
useless_data = ['123','321','321','123123']
set_default_color_theme("dark-blue")
btn_names = ["Все заметки","Избранные","Корзина"]
btn_names2 = ["Настройки","О приложении"]
app = ctk.CTk()
app.geometry("800x500")
app.title("  ")
img = ctk.CTkImage(dark_image=Image.open(Path("src") / "images.png"), size=(30,30))
frame1 = ctk.CTkFrame(app)
frame2 = ctk.CTkFrame(app)
frame3 = ctk.CTkFrame(app)
frames = ctk.CTkFrame(frame1)
frames2 = ctk.CTkFrame(frame1)
frames3 = ctk.CTkScrollableFrame(frame2, orientation='vertical',width=300)
search_frame = ctk.CTkFrame(frame2)
icon = ctk.CTkLabel(search_frame,text='', image=img)
entry = ctk.CTkEntry(search_frame, width=200)
btn1 = ctk.CTkButton(frame1,text="Новая заметка",image=img,font=("Arial",16))
for i, widget in enumerate(btn_names, start=0):
    f_1 = ctk.CTkFrame(frames, cursor="hand2")
    lbl_f= ctk.CTkLabel(f_1, text=' ', image=img)
    btn_f = ctk.CTkLabel(f_1, text=widget, font=("Arial",16), width=150)
    count = ctk.CTkLabel(f_1, text="1")
    f_1.pack(padx=5,pady=5)
    lbl_f.pack(side='left',padx=5,pady=5)
    btn_f.pack(side='left',padx=5,pady=5)
    count.pack(side='right',padx=5,pady=5)
    btn_f.propagate(False)
for i, widget in enumerate(btn_names2, start=0):
    f_1 = ctk.CTkFrame(frames2, cursor="hand2")
    lbl_f= ctk.CTkLabel(f_1, text=' ', image=img)
    lbl2_f = ctk.CTkLabel(f_1, text=widget, font=("Arial",16), width=150)
    f_1.pack(padx=5,pady=5)
    lbl_f.pack(side='left',padx=5,pady=5)
    lbl2_f.pack(side='left',padx=5,pady=5)
    lbl2_f.propagate(False)
for i, (val1,val2) in enumerate(zip(useless_date_title,useless_data), start=0):
    f_1 = ctk.CTkFrame(frames3, cursor="hand2")
    lbl_f= ctk.CTkLabel(f_1, text=val1, font=("Arial",16), width=200)
    lbl2_f = ctk.CTkLabel(f_1, text=val2, width=200)
    time = ctk.CTkLabel(f_1, text=f"{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}",font=("Arial",8))
    f_1.pack(padx=5,pady=5, fill='x')
    lbl_f.grid(column=0,row=0,padx=5,pady=5, sticky='w')
    lbl2_f.grid(column=0,row=1,padx=5,pady=5,sticky='w')
    time.grid(column=1,row=0,padx=5, sticky='ne')
frame1.pack(side='left', fill='y')
frame2.pack(fill='y')
frame3.pack(side='right', fill='both', expand=1)
frames.grid(column=0,row=1,padx=10,pady=10)
frames2.grid(column=0,row=2,padx=10,pady=10, sticky="s")
frames3.pack(padx=10,pady=10, fill='y')
search_frame.pack(padx=10,pady=10)
icon.pack(side='left')
entry.pack()
btn1.grid(column=0,row=0,padx=10,pady=10)

app.mainloop()