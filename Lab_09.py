from Lab_07 import *
from tkinter import *
from tkinter import messagebox

def belepes():

    def ok_gomb_kezelese():
        dolgozo.felhasznalo_neve = f_nev.get()
        dolgozo.felhasznalo_jelszava = f_jelszo.get()
        if f_nev.get() == "" or f_jelszo.get() == "":
            messagebox.showinfo("Hiba", "Valamelyik mező üres", parent=be_ablak)
        elif " " in f_nev.get():
            messagebox.showinfo("Hiba", "Szóközt használt az emailben!", parent=be_ablak)
        elif "@" not in f_nev.get():
            messagebox.showinfo("Hiba", "Hiánzik a @ jel", parent=be_ablak)
        elif "." not in f_nev.get():
            messagebox.showinfo("Hiba", "Hiánzik a . jel", parent=be_ablak)
        else:
            be_ablak.destroy()
            if dolgozo.felh_es_jelszo_ell():
                messagebox.showinfo("Belépés", "Üdv a fedélzeten!")
            else:
                messagebox.showinfo("Belépés", "Belépés megtagadva!")


    def reg_kerese():
        be_ablak.destroy()
        regisztracio()

    be_ablak = Toplevel(app)
    be_ablak.title("Beléptetés")

    f_nev_cimke = Label(be_ablak, text="Felhasználó neve (email):")
    f_jelszo_cimke =Label(be_ablak, text="Jelszó:")

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(be_ablak, textvariable=f_nev, width=20)
    f_jelszo = StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(be_ablak, textvariable=f_jelszo, width=20)

    ok_gomb = Button(be_ablak, text="OK", command=ok_gomb_kezelese, width=10)
    reg_gomb = Button(be_ablak, text="Regisztráció", command=reg_kerese)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15)
    f_nev_be.grid(row=0, column=1, padx=15)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15)
    f_jelszo_be.grid(row=1, column=1)
    reg_gomb.grid(row=2, column=0, padx=15)
    ok_gomb.grid(row=2, column=1, pady=15)

    be_ablak.mainloop()

def regisztracio():

    def ok_gomb_kezelese():
        dolgozo.felhasznalo_neve = f_nev.get()
        dolgozo.felhasznalo_jelszava = f_jelszo.get()
        if f_nev.get() == "" or f_jelszo.get() == "" or f_jelszo2.get() == "":
            messagebox.showinfo("Hiba", "Valamelyik mező üres", parent=reg_ablak)
        elif f_jelszo.get() != f_jelszo2.get():
            messagebox.showinfo("Hiba", "Nem azonosak a jelszavak", parent=reg_ablak)
        elif " " in f_nev.get():
            messagebox.showinfo("Hiba", "Szóközt használt az emailben!", parent=reg_ablak)
        elif "@" not in f_nev.get():
            messagebox.showinfo("Hiba", "Hiánzik a @ jel", parent=reg_ablak)
        elif "." not in f_nev.get():
            messagebox.showinfo("Hiba", "Hiánzik a . jel", parent=reg_ablak)
        elif not dolgozo.jelszo_vizsgalata(8):
            messagebox.showinfo("Hiba", "Nem megfelelő a jelszó!", parent=reg_ablak)
        else:
            reg_ablak.destroy()
            dolgozo.tarolas()

    def jelszo_gen():
        dolgozo.jelszo_generalasa()
        f_jelszo.set(dolgozo.felhasznalo_jelszava)
        f_jelszo2.set(dolgozo.felhasznalo_jelszava)

    reg_ablak = Toplevel(app)
    reg_ablak.title("Regisztráció")

    f_nev_cimke = Label(reg_ablak, text="Felhasználó neve (email):")
    f_jelszo_cimke =Label(reg_ablak, text="Jelszó:")
    f_jelszo2_cimke = Label(reg_ablak, text="A jelszó ismét:")

    ok_gomb = Button(reg_ablak, text="OK", command=ok_gomb_kezelese, width=10)
    jelszo_gen_gomb = Button(reg_ablak, text="Jelszó generálása", command=jelszo_gen)

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(reg_ablak, textvariable=f_nev, width=20)
    f_jelszo = StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(reg_ablak, textvariable=f_jelszo, width=20)
    f_jelszo2 = StringVar()
    f_jelszo2.set("")
    f_jelszo2_be = Entry(reg_ablak, textvariable=f_jelszo2, width=20)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15)
    f_nev_be.grid(row=0, column=1)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15)
    f_jelszo_be.grid(row=1, column=1)
    jelszo_gen_gomb.grid(row=1, column=2, padx=15)
    f_jelszo2_cimke.grid(row=2, column=0, sticky="E", padx=15)
    f_jelszo2_be.grid(row=2, column=1)
    ok_gomb.grid(row=3, column=1, pady=15, columnspan=2)

    reg_ablak.mainloop()

def nevjegy():
    messagebox.showinfo("Néjegy", "Készítő: Én, 2024")

def sugo():
    messagebox.showerror("Súgó", "Még nincs súgó!")

# Main program
dolgozo = Felhasznalo()

app = Tk()
app.title("Dolgozói nyilvántartás")
app.geometry("600x400")

menulista = Menu(app)

hozzaferes = Menu(menulista)
hozzaferes.add_command(label="Belépés", command=belepes)
hozzaferes.add_command(label="Regisztráció", command=regisztracio)
hozzaferes.add_command(label="Kilépés", command=app.destroy)
menulista.add_cascade(label="Hozzáférés", menu=hozzaferes)

egyeb = Menu(menulista)
egyeb.add_command(label="Névjegy", command=nevjegy)
egyeb.add_command(label="Súgó", command=sugo)
menulista.add_cascade(label="Egyéb", menu=egyeb)

app.config(menu=menulista)
app.mainloop()
