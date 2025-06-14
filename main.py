# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

import tkinter as tk
import pandas as pd
from tkinter import filedialog





medsearch=tk.Tk()
medsearch.geometry("1000x1500")
medsearch.title("Search Medicin by Name ")

def openfile():
    global pharmacy
    path=filedialog.askopenfilename(title="choose the file ")
    cairo = pd.read_excel(path, sheet_name="القاهرة")
    shamal_gharab_delta = pd.read_excel(path, sheet_name="شمال غرب الدلتا")
    shamal_shark = pd.read_excel(path, sheet_name="شمال شرق")
    giza = pd.read_excel(path, sheet_name="الجيزة")
    west_els3ed = pd.read_excel(path, sheet_name="وسط الصعيد")
    ganoub_els3ed = pd.read_excel(path, sheet_name="جنوب الصعيد")
    kafr_elsheikh = pd.read_excel(path, sheet_name="كفر الشيخ")
    beny_swef = pd.read_excel(path, sheet_name="بنى سويف")
    qaliobya = pd.read_excel(path, sheet_name="القليوبية")
    behira = pd.read_excel(path, sheet_name="البحيرة")
    gharbia = pd.read_excel(path, sheet_name="الغربية")
    dimiat = pd.read_excel(path, sheet_name="دمياط")
    elmenia = pd.read_excel(path, sheet_name="المنيا")
    sohag = pd.read_excel(path, sheet_name="سوهاج")
    sharqia = pd.read_excel(path, sheet_name="الشرقية")
    fayom = pd.read_excel(path, sheet_name="الفيوم")
    monfya = pd.read_excel(path, sheet_name="المنوفية")
    aswan = pd.read_excel(path, sheet_name="اسوان")
    madint_nasr = pd.read_excel(path, sheet_name="مدينة نصر")
    october6 = pd.read_excel(path, sheet_name="6اكتوبر")
    awram_madint_nasr = pd.read_excel(path, sheet_name="اورام م.نصر")
    elwadi_elgdid = pd.read_excel(path, sheet_name="الوادي الجديد ")
    shamal_sina = pd.read_excel(path, sheet_name="شمال سينا")
    bahr_ahmer = pd.read_excel(path, sheet_name="البحر الاحمر")
    pharmacy = pd.concat(
        [cairo, shamal_gharab_delta, shamal_shark, giza, west_els3ed, ganoub_els3ed, kafr_elsheikh, beny_swef, qaliobya,
         behira, gharbia,
         dimiat, elmenia, sohag, sharqia, fayom, monfya, aswan, madint_nasr, october6, awram_madint_nasr, elwadi_elgdid,
         shamal_sina, bahr_ahmer]
        )
    pharmacy = pharmacy.sort_values(by="الدواء")
def medicine_sum(med):
    check1 = pharmacy[pharmacy["الدواء"].isin(med)]
    pharmacy.columns = pharmacy.columns.str.strip()
    total_elkemya = check1.groupby("الفرع")["الكمية"].sum()
    totalelkemah = check1.groupby("الفرع")["القيمة"].sum()
    s3r =check1[["الفرع", "السعر"]].drop_duplicates().sort_values(by="الفرع")
    month=check1.groupby("الفرع")["الشهر"].sum()
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, f"الكمية:\n{total_elkemya}\n\n")
    result_text.insert(tk.END, f"القيمة:\n{totalelkemah}\n\n")
    result_text.insert(tk.END, f"السعر:\n{s3r}\n")
    result_text.insert(tk.END,f"\n:الشهر{month}\n")




button=tk.Button(medsearch,text="open file ",width=20,font=("Arial", 10 ),command=openfile)
button.place(x=10,y=20)
medname=tk.Entry(medsearch,width=35)
medname.place(x=10,y=50)

searchbutton=tk.Button(medsearch,text="search ",font=("Arial",10),width=20,command=lambda: medicine_sum([medname.get()]))
searchbutton.place(x=170, y=20)


result_text = tk.Text(medsearch, height=40, width=110,font=("Arial",15))
result_text.place(x=0, y=80)

medsearch.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
