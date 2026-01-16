import tkinter as tk
import deepl
import requests

from lxml.html import fromstring

from tkinter import *
from tkinter import ttk

Error_text = "Error"

def ErrorFensterOeffnen(Error_text_rec):
    ErrorFenster = Toplevel()
    ErrorFenster.geometry("300x70")
    ErrorVar = StringVar()
    ErrorVar.set(Error_text_rec)
    ErrorNachricht = Label(ErrorFenster, textvariable= ErrorVar)
    ErrorNachricht.pack()
    ButtonConfirm = Button(ErrorFenster, text= "OK", command=ErrorFenster.destroy)
    ButtonConfirm.pack()
    progressbar["value"] = 0
    Button1["state"] = "normal"
 
def retrieve():
    Button1["state"] = "disabled"
    with open("deepl-api-key.txt","w") as key:
        deepl_key_write = deepl_key.get()
        key.write(deepl_key_write)
    progressbar["value"] = 40
    fenster.update()
    if lang_select.get() == "Arabisch":
        lang_id = "AR"
        bible_id = "SVD"
        response1 = "عربي"
        response3 = "مقطع من العظة"
        response6 = "ملخص الخطبة"
    elif lang_select.get() == "Chinesisch":
        lang_id = "ZH-HANS"
        bible_id = "CUV"
        response1 = "中文 - Chinesisch"
        response3 = "讲道经文："
        response6 = "讲道摘要："
    elif lang_select.get() == "Englisch":
        lang_id = "EN-US"
        bible_id = "ESV"
        response1 = "English - Englisch"
        response3 = "Sermon Passage:"
        response6 = "Sermon Overview:"
    elif lang_select.get() == "Französisch":
        lang_id = "FR"
        bible_id = "NBS"
        response1 = "Français - Französisch"
        response3 = "Passage du sermon :"
        response6 = "Résumé du sermon :"
    elif lang_select.get() == "Indonesisch":
        lang_id = "ID"
        bible_id = "TB"
        response1 = "Bahasa Indonesia - Indonesisch"
        response3 = "Ayat Khotbah:"
        response6 = "Ringkasan Khotbah:"
    elif lang_select.get() == "Italienisch":
        lang_id = "IT"
        bible_id = "NR06"
        response1 = "Italiano - Italienisch"
        response3 = "Passaggio del sermone:"
        response6 = "Sommario del sermone:"
    elif lang_select.get() == "Japanisch":
        lang_id = "JA"
        bible_id = "NJB"
        response1 = "日本語 - Japanisch"
        response3 = "説教箇所："
        response6 = "説教要約："
    elif lang_select.get() == "Koreanisch":
        lang_id = "KO"
        bible_id = "RNKSV"
        response1 = "한국어 - Koreanisch"
        response3 = "설교 본문:"
        response6 = "설교 요약:"
    elif lang_select.get() == "Polnisch":
        lang_id = "PL"
        bible_id = "BW"
        response1 = "Polski - Polnisch"
        response3 = "Fragment kazania:"
        response6 = "Podsumowanie kazania:"
    elif lang_select.get() == "Portugiesisch (PT)":
        lang_id = "PT-PT"
        bible_id = "NVIPT"
        response1 = "Português - Portugiesisch (Portugal)"
        response3 = "Passagem do sermão:"
        response6 = "Resumo do sermão:"
    elif lang_select.get() == "Portugiesisch (BRA)":
        lang_id = "PT-BR"
        bible_id = "TB10"
        response1 = "Português brasileiro - Portugiesisch (Brasilien)"
        response3 = "Passagem do sermão:"
        response6 = "Resumo do sermão:"
    elif lang_select.get() == "Russisch":
        lang_id = "RU"
        bible_id = "SYNOD"
        response1 = "Русский - Russisch"
        response3 = "Отрывок из проповеди:"
        response6 = "Краткое содержание проповеди:"
    elif lang_select.get() == "Spanisch":
        lang_id = "ES"
        bible_id = "NVI"
        response1 = "Español - Spanisch"
        response3 = "Pasaje del sermón:"
        response6 = "Resumen del sermón:"
    elif lang_select.get() == "Ukrainisch":
        lang_id = "UK"
        bible_id = "PHIL"
        response1 = "Українська - Ukrainisch"
        response3 = "Уривок з проповіді:"
        response6 = "Короткий зміст проповіді:"
    else:
        print("Error - Keine Sprache ausgewählt")
        Error_text = "Error - Keine Sprache ausgewählt"
        ErrorFensterOeffnen(Error_text)
        return
    if book_select.get() == "1. Mose (Genesis)":
        book_id = 1
    elif book_select.get() == "2. Mose (Exodus)":
        book_id = 2
    elif book_select.get() == "3. Mose (Leviticus)":
        book_id = 3
    elif book_select.get() == "4. Mose (Numeri)":
        book_id = 4
    elif book_select.get() == "5. Mose (Deuteronomium)":
        book_id = 5
    elif book_select.get() == "Josua":
        book_id = 6
    elif book_select.get() == "Richter":
        book_id = 7
    elif book_select.get() == "Rut":
        book_id = 8
    elif book_select.get() == "1. Samuel":
        book_id = 9
    elif book_select.get() == "2. Samuel":
        book_id = 10
    elif book_select.get() == "1. Könige":
        book_id = 11
    elif book_select.get() == "2. Könige":
        book_id = 12
    elif book_select.get() == "1. Chronik":
        book_id = 13
    elif book_select.get() == "2. Chronik":
        book_id = 14
    elif book_select.get() == "Esra":
        book_id = 15
    elif book_select.get() == "Nehemia":
        book_id = 16
    elif book_select.get() == "Ester":
        book_id = 17
    elif book_select.get() == "Hiob":
        book_id = 18
    elif book_select.get() == "Psalmen":
        book_id = 19
    elif book_select.get() == "Sprüche":
        book_id = 20
    elif book_select.get() == "Kohelet/Prediger":
        book_id = 21
    elif book_select.get() == "Hohelied":
        book_id = 22
    elif book_select.get() == "Jesaja":
        book_id = 23
    elif book_select.get() == "Jeremia":
        book_id = 24
    elif book_select.get() == "Klagelieder":
        book_id = 25
    elif book_select.get() == "Ezechiel":
        book_id = 26
    elif book_select.get() == "Daniel":
        book_id = 27
    elif book_select.get() == "Hosea":
        book_id = 28
    elif book_select.get() == "Joel":
        book_id = 29
    elif book_select.get() == "Amos":
        book_id = 30
    elif book_select.get() == "Obadja":
        book_id = 31
    elif book_select.get() == "Jona":
        book_id = 32
    elif book_select.get() == "Micha":
        book_id = 33
    elif book_select.get() == "Nahum":
        book_id = 34
    elif book_select.get() == "Habakuk":
        book_id = 35
    elif book_select.get() == "Zefanja":
        book_id = 36
    elif book_select.get() == "Haggai":
        book_id = 37
    elif book_select.get() == "Sacharja":
        book_id = 38
    elif book_select.get() == "Maleachi":
        book_id = 39
    elif book_select.get() == "Matthäus":
        book_id = 40
    elif book_select.get() == "Markus":
        book_id = 41
    elif book_select.get() == "Lukas":
        book_id = 42
    elif book_select.get() == "Johannes":
        book_id = 43
    elif book_select.get() == "Apostelgeschichte":
        book_id = 44
    elif book_select.get() == "Römer":
        book_id = 45
    elif book_select.get() == "1. Korinther":
        book_id = 46
    elif book_select.get() == "2. Korinther":
        book_id = 47
    elif book_select.get() == "Galater":
        book_id = 48
    elif book_select.get() == "Epheser":
        book_id = 49
    elif book_select.get() == "Philipper":
        book_id = 50
    elif book_select.get() == "Kolosser":
        book_id = 51
    elif book_select.get() == "1. Thessalonicher":
        book_id = 52
    elif book_select.get() == "2. Thessalonicher":
        book_id = 53
    elif book_select.get() == "1. Timotheus":
        book_id = 54
    elif book_select.get() == "2. Timotheus":
        book_id = 55
    elif book_select.get() == "Titus":
        book_id = 56
    elif book_select.get() == "Philemon":
        book_id = 57
    elif book_select.get() == "Hebräer":
        book_id = 58
    elif book_select.get() == "Jakobus":
        book_id = 59
    elif book_select.get() == "1. Petrus":
        book_id = 60
    elif book_select.get() == "2. Petrus":
        book_id = 61
    elif book_select.get() == "1. Johannes":
        book_id = 62
    elif book_select.get() == "2. Johannes":
        book_id = 63
    elif book_select.get() == "3. Johannes":
        book_id = 64
    elif book_select.get() == "Judas":
        book_id = 65
    elif book_select.get() == "Offenbarung":
        book_id = 66
    else:
        print("Error - Keine Bibelstelle ausgewählt")
        Error_text = "Error - Keine Bibelstelle ausgewählt"
        ErrorFensterOeffnen(Error_text)
        return
    progressbar["value"] = 80
    fenster.update()
    kap = int(kapitel.get())
    vers_a = int(vers_anfang.get())
    vers_e = int(vers_ende.get())+1
    if vers_e < vers_a:
        print("Error, 'bis Vers' darf nicht kleiner sein als 'von Vers'!")
        Error_text = "Error, 'bis Vers' darf nicht kleiner sein als 'von Vers'!"
        ErrorFensterOeffnen(Error_text)
        return
    Verszahlen = int(Var1.get())
    auth_key = deepl_key.get()
    if auth_key == "":
        print("Kein DeepL-Key")
        if predigttitel_var != "" or zsf_var != "":
            Error_text = "Error - Zum Übersetzen muss ein DeepL-Key eingegeben werden!"
            ErrorFensterOeffnen(Error_text)
            return
    else:
        deepl_client = deepl.DeepLClient(auth_key)
    predigttitel_var = predigttitel.get()
    zsf_var = zsf_deutsch.get("1.0", "end")
    response4 = ""
    progressbar["value"] = 120
    fenster.update()
    progressAPI = 120 / (vers_e - vers_a)
    for x in range(vers_a, vers_e):
        url_api = "https://bolls.life/get-verse/" + bible_id + "/" + str(book_id) + "/" + str(kap) + "/" + str(x)
        if Verszahlen == 2:
            response4 = response4 + str(x) + " "
        elif Verszahlen == 3:
            response4 = response4 + "(" + str(x) + ") "
        print(requests.get(url_api))
        response4 = response4 + fromstring(requests.get(url_api).json()["text"]).text_content() + " "
        progressbar["value"] = progressbar["value"] + progressAPI
        fenster.update()
    if predigttitel_var == "":
        response2 = ""
    else:
        response2 = deepl_client.translate_text(predigttitel_var, target_lang= lang_id).text
    progressbar["value"] = 280
    fenster.update()
    if zsf_var == "":
        response7 = ""
    else:
        response7 = deepl_client.translate_text(zsf_var, target_lang= lang_id).text
    progressbar["value"] = 320
    fenster.update()
    url_api2 = "https://bolls.life/get-books/" + bible_id
    data = requests.get(url_api2).json()
    progressbar["value"] = 360
    fenster.update()
    if vers_anfang.get() == vers_ende.get():
        response5 = "(" + next((i.get("name") for i in data if i.get("bookid") == book_id), None) + " " + str(kap) + ": " + vers_anfang.get() + ", " + bible_id + ")"
    else:
        response5 = "(" + next((i.get("name") for i in data if i.get("bookid") == book_id), None) + " " + str(kap) + ": " + vers_anfang.get() + "-" + vers_ende.get() + ", " + bible_id + ")"
    response = response1 + "\n" + response2 + "\n" + response3 + "\n" + response4 + "\n" + response5 + "\n" + response6 + "\n" + response7
    progressbar["value"] = 400
    resultatfenster = Toplevel()
    resultatfenster.geometry("600x600")
    resultatframe = Frame(resultatfenster)
    resultatframe.pack(expand = True, fill = tk.BOTH)
    resultatentry = Text(resultatframe)
    resultatentry.insert("1.0", response)
    resultatentry.pack(expand = True, fill = tk.BOTH)
    Button1["state"] = "normal"
    
    


with open("deepl-api-key.txt","a") as f:
    f.write("")

deepl_key_file = open("deepl-api-key.txt","r")
deepl_key_saved = deepl_key_file.read()


fenster = tk.Tk()
fenster.title("Predigt Handout Übersetzer")
#fenster.geometry("600x850")
 
 
frame = Frame(fenster)
frame.pack()
 
vlist = ["Chinesisch",
         "Englisch", 
         "Französisch", 
         "Indonesisch", "Italienisch", 
         "Japanisch", 
         "Koreanisch", 
         "Polnisch", "Portugiesisch (PT)", "Portugiesisch (BRA)", 
         "Russisch", 
         "Spanisch", 
         "Ukrainisch"]

booklist = ["1. Mose (Genesis)",
"2. Mose (Exodus)",
"3. Mose (Leviticus)",
"4. Mose (Numeri)",
"5. Mose (Deuteronomium)",
"Josua",
"Richter",
"Rut",
"1. Samuel",
"2. Samuel",
"1. Könige",
"2. Könige",
"1. Chronik",
"2. Chronik",
"Esra",
"Nehemia",
"Ester",
"Hiob",
"Psalmen",
"Sprüche",
"Kohelet/Prediger",
"Hohelied",
"Jesaja",
"Jeremia",
"Klagelieder",
"Ezechiel",
"Daniel",
"Hosea",
"Joel",
"Amos",
"Obadja",
"Jona",
"Micha",
"Nahum",
"Habakuk",
"Zefanja",
"Haggai",
"Sacharja",
"Maleachi",
"Matthäus",
"Markus",
"Lukas",
"Johannes",
"Apostelgeschichte",
"Römer",
"1. Korinther",
"2. Korinther",
"Galater",
"Epheser",
"Philipper",
"Kolosser",
"1. Thessalonicher",
"2. Thessalonicher",
"1. Timotheus",
"2. Timotheus",
"Titus",
"Philemon",
"Hebräer",
"Jakobus",
"1. Petrus",
"2. Petrus",
"1. Johannes",
"2. Johannes",
"3. Johannes",
"Judas",
"Offenbarung",
]
 
lang_select = ttk.Combobox(frame, width = 50, values = vlist)
lang_select.set("Sprache")
lang_select.pack(padx = 5, pady = 5)

book_select = ttk.Combobox(frame, width = 50, values = booklist)
book_select.set("Bibelstelle")
book_select.pack(padx = 5, pady = 5)

kapitel = Entry(frame, width = 10)
kapitel.insert(0,'1')
kapitel.label = Label(frame, text='Kapitel:')
kapitel.label.pack()
kapitel.pack(padx = 5, pady = 5)

vers_anfang = Entry(frame, width = 10)
vers_anfang.insert(0,'1')
vers_anfang.label = Label(frame, text='von Vers:')
vers_anfang.label.pack()
vers_anfang.pack(padx = 5, pady = 5)

vers_ende = Entry(frame, width = 10)
vers_ende.insert(0,'1')
vers_ende.label = Label(frame, text='bis Vers (wenn die Bibelstelle nur einen Vers enthält, hier trotzdem nochmals den Vers eingeben):')
vers_ende.label.pack()
vers_ende.pack(padx = 5, pady = 5)

Var1 = IntVar()
 
RBttn = Radiobutton(frame, text = "Keine Verszahlen", variable = Var1,
                    value = 1)
RBttn.pack(padx = 5, pady = 5)
 
RBttn2 = Radiobutton(frame, text = "Normale Verszahlen", variable = Var1,
                     value = 2)
RBttn2.pack(padx = 5, pady = 5)

RBttn3 = Radiobutton(frame, text = "Eingeklammerte Verszahlen", variable = Var1,
                     value = 3)
RBttn3.pack(padx = 5, pady = 5)

predigttitel = Entry(frame, width = 80)
predigttitel.label = Label(frame, text='Predigttitel:')
predigttitel.label.pack()
predigttitel.pack(padx = 5, pady = 5)

zsf_deutsch = Text(frame, height = 20, width = 100)
zsf_deutsch.label = Label(frame, text='Predigtzusammenfassung:')
zsf_deutsch.label.pack()
zsf_deutsch.pack(padx = 5, pady = 5)



deepl_key = Entry(frame, width = 80)
deepl_key.insert(0, deepl_key_saved)
deepl_key.label = Label(frame, text='DeepL-API-Key (der zuletzt gesendete Key wird gespeichert):')
deepl_key.label.pack()
deepl_key.pack(padx = 5, pady = 5)


progressbar = ttk.Progressbar(frame, length=400, maximum=400, mode="determinate")
progressbar.pack(padx = 5, pady = 5)

 
Button1 = Button(frame, text = "Übersetzen", command = retrieve)
Button1.pack(padx = 5, pady = 5)




width = 600 # Width 
height = 850 # Height
 
screen_width = fenster.winfo_screenwidth()  # Width of the screen
screen_height = fenster.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = 0
 
fenster.geometry('%dx%d+%d+%d' % (width, height, x, y))

fenster.mainloop()