import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy
#tải mô hình được train
from keras.models import load_model
model = load_model('model_insect.h5')

# Classes
class_Insect ={ 1: 'Bọ Cánh Cứng Khổng Lồ',
                2: 'Bọ Cánh Cứng Tiger',
                3: 'Bọ Cạp',
                4: 'Bọ Hung',
                5: 'Bọ Ngựa Phong Lan',
                6: 'Bọ Ngựa',
                7: 'Bọ Rùa',
                8: 'Bướm Đêm',
                9: 'Bướm',
                10: 'Cào Cào',
                11: 'Châu Chấu',
                12: 'Chuồn Chuồn',
                13: 'Dế',
                14: 'Dễ Trũi',
                15: 'Đom Đóm',
                16: 'Gián',
                17: 'Kiến Ba Khoang',
                18: 'Kiến Đen',
                19: 'Kiến Vàng',
                20: 'Mọt Cao Cổ',
                21: 'Muỗi',
                22: 'Ong',
                23: 'Ong Bắp Cày',
                24: 'Rết',
                25: 'Ruồi',
                26: 'Sâu',
                27: 'Ve Sầu',
                28: 'Nhện'}


# Khoi tao GUI
win = tk.Tk()
win.geometry('700x500')
win.title('Insect')
win.configure()
truong = Label(win, text='TRƯỜNG ĐH SƯ PHẠM KỸ THUẬT TP.HCM',font=('arial', 13, 'bold'), fg='red')
truong.pack(side= TOP)
khoa = Label(win, text='KHOA CƠ KHÍ CHÉ TẠO MÁY',font=('arial', 13, 'bold'), fg='BLUE')
khoa.pack(side= TOP)
bo = Label(win, text='BỘ MÔN CƠ ĐIỆN TỬ',font=('arial', 13, 'bold'), fg='BLACK')
bo.pack(side= TOP)

inf_gv= Label(win, text='GVHD: PGS.TS Nguyễn Trường Thịnh',font=('arial', 13), fg='#808080')
inf_gv.place(x= 0, y= 440)
inf= Label(win, text='SVTH: Huỳnh Anh Kiệt-20146499',font=('arial', 13), fg='#808080')
inf.place(x= 0, y= 470)

logo_import = (Image.open('LOGO.png'))
resize_logo = logo_import.resize((150,150), Image.ANTIALIAS)
img_logo = ImageTk.PhotoImage(resize_logo)
logo = Label(win, image= img_logo,text=' ',font=('arial', 10))
logo.place(x= 0, y= 0)

khoa_import = (Image.open('khoa.png'))
resize_khoa = khoa_import.resize((150,150), Image.ANTIALIAS)
img_khoa = ImageTk.PhotoImage(resize_khoa)
logo_khoa = Label(win, image= img_khoa,text=' ',font=('arial', 10))
logo_khoa.place(x= 545, y= 0)

label = Label(win,background='#808080', font= ('arial', 15, 'bold'))
sign_image = Label(win)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((128,128))
    image = numpy.expand_dims(image, axis= 0)
    image = numpy.array(image)
    print(image.shape)
    pred = numpy.argmax(model.predict([image])[0])
    sign = class_Insect[pred]
    print(sign)
    label.configure(foreground= '#011638', text=sign)

def show_classify_button(file_path):
    classify_b= Button(win, text='Classify Image',command=lambda:classify(file_path), padx= 20, pady= 5)
    classify_b.configure(background='#C0C0C0', foreground='white', font=('arial', 10, 'bold')) 
    classify_b.place(relx=0.79, rely=0.55)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        upload = Image.open(file_path)
        upload.thumbnail(((win.winfo_width()/2.25),(win.winfo_height()/2.25)))
        img = ImageTk.PhotoImage(upload)

        sign_image.configure(image=img)
        sign_image.image=img
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload = Button(win, text='Upload',command=upload_image, padx= 10, pady= 5)
upload.configure(background='#C0C0C0', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM,pady=50)

sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(win, text='Insect Result', pady= 20, font=('arial', 10, 'bold'))
#heading.configure(foreground='#C0C0C0')
heading.pack()


win.mainloop()
