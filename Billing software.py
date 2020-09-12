from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #============variables=======================
        #============cosmatics=======================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()

        #===============grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.sugar=IntVar()
        self.wheat=IntVar()
        self.tea=IntVar()

        #===============cold drinks======================
        self.maaza=IntVar()
        self.thumsup=IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()
        self.frooti=IntVar()
        self.coke=IntVar()

        #==========Total price and tax varialbes==================

        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_taxx=StringVar()

        #========customer=========================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #=========Customer detail frame==============
        F1=LabelFrame(self.root,text="Customer details",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,bd=7,relief=SUNKEN,font=("arial 15 bold")).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phone, bd=7, relief=SUNKEN, font=("arial 15 bold")).grid(row=0, column=3, padx=10,pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, bd=7, relief=SUNKEN, font=("arial 15 bold")).grid(row=0, column=5, padx=10,pady=5)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        #============ Cosmeics frame ===================

        F2=LabelFrame(self.root, text="Cosmetics", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",15,"bold"),bg=bg_color,fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)


        hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10,textvariable=self.hair_spray, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)


        hair_gel_lbl = Label(F2, text="Hair Gel", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_gel_txt = Entry(F2, width=10,textvariable=self.gel, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)


        body_l_lbl = Label(F2, text="Body Loshan", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_l_txt = Entry(F2, width=10,textvariable=self.loshan, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        #============ Grocery frame ===================

        F3=LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=330, y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="green").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl= Label(F3, text="Food oil", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt= Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)


        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)


        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)


        g6_lbl = Label(F3, text="Tea", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # ============ Cold drinks frame ===================

        F4 = LabelFrame(self.root, text="Cold Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=655, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Thums Up", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.thumsup, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl=Label(F4, text="Sprite", font=("times new roman", 15, "bold"), bg=bg_color,fg="green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt=Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4, text="Limca", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        c5_lbl = Label(F4, text="Coke", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.coke, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4, text="Maaza", font=("times new roman", 15, "bold"), bg=bg_color, fg="green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.maaza, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Bill Area =========================
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1000,y=180, width=340, height=380)

        bill_title=Label(F5,text="Bill Area",font=("arial 15 bold"),bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #========Bill Menu=============================
        F6 = LabelFrame(self.root,text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=1,pady=0)
        m1_txt=Entry(F6,width=15,font="arial 15 bold",bd=7,relief=GROOVE).grid(row=0,column=1,padx=1,pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=("times new roman", 15, "bold"), bg=bg_color,fg="white").grid(row=1, column=0, padx=1, pady=0)
        m2_txt = Entry(F6, width=15, font="arial 15 bold", bd=7, relief=GROOVE).grid(row=1, column=1, padx=1, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drink Price", font=("times new roman", 15, "bold"), bg=bg_color,fg="white").grid(row=2, column=0, padx=1, pady=0)
        m3_txt = Entry(F6, width=15, font="arial 15 bold", bd=7, relief=GROOVE).grid(row=2, column=1, padx=10, pady=0)

        n1_lbl=Label(F6,text="Cosmetic Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=1,pady=0)
        n1_txt=Entry(F6,width=15,font="arial 15 bold",bd=7,relief=GROOVE).grid(row=0,column=4,padx=10,pady=1)

        n2_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 15, "bold"), bg=bg_color,fg="white").grid(row=1, column=3, padx=1, pady=0)
        n2_txt = Entry(F6, width=15, font="arial 15 bold", bd=7, relief=GROOVE).grid(row=1, column=4, padx=10, pady=1)

        n3_lbl = Label(F6, text="Cold Drink Tax", font=("times new roman", 15, "bold"), bg=bg_color,fg="white").grid(row=2, column=3, padx=1, pady=0)
        n3_txt = Entry(F6, width=15, font="arial 15 bold", bd=7, relief=GROOVE).grid(row=2, column=4, padx=1, pady=0)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=550,height=100)

        total_btn=Button(btn_F,text="Total",command=self.total,font="arial 15 bold",bd=7,relief=GROOVE,width=8,bg="cadetblue",fg="white").grid(row=0,column=0,padx=3,pady=10)
        Gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,font="arial 15 bold",bd=7,relief=GROOVE,width=12,bg="cadetblue",fg="white").grid(row=0,column=1,padx=3,pady=10)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,font="arial 15 bold",width=8,bd=7,relief=GROOVE,bg="cadetblue",fg="white").grid(row=0,column=2,padx=3,pady=10)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,font="arial 15 bold",width=8,bd=7,relief=GROOVE,bg="cadetblue",fg="white").grid(row=0,column=3,padx=3,pady=10)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.hair_spray.get()*180
        self.c_hg_p=self.gel.get()*140
        self.c_bl_p=self.loshan.get()*180
        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
        )
        self.cosmetic_price.set(str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.05),2)
        self.cosmetic_tax.set(str(self.c_tax))


        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*85
        self.g_w_p=self.wheat.get()*50
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*120
        self.total_grocery_price=float(
            self.g_r_p+
            self.g_fo_p+
            self.g_d_p+
            self.g_w_p+
            self.g_s_p+
            self.g_t_p
        )
        self.grocery_price.set(str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price* 0.1),2)
        self.grocery_tax.set(str(self.g_tax))

        self.d_thu_p=self.thumsup.get()*65
        self.d_f_p=self.frooti.get()*55
        self.d_s_p=self.sprite.get()*65
        self.d_c_p=self.coke.get()*60
        self.d_l_p=self.limca.get()*55
        self.d_m_p=self.maaza.get()*60
        self.total_drinks_price=float(
            self.d_thu_p+
            self.d_f_p+
            self.d_s_p+
            self.d_c_p+
            self.d_l_p+
            self.d_m_p
        )
        self.cold_drinks_price.set(str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price * 0.05),2)
        self.cold_drinks_taxx.set(str(self.d_tax))

        self.Total_bill=float ( self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                                )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Ali's Shop\n")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()} ")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n=====================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n=====================================")

    #==================cosmetics==========================
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="0.0" and self.grocery_price.get()=="0.0" and self.cold_drinks_price.get()=="0.0":
            messagebox.showerror("Error","No Items purchased")


        else:
            self.welcome_bill()
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
        #=======================grocery==========================
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

        #===============cold drinks====================================
            if self.thumsup.get()!=0:
                self.txtarea.insert(END,f"\n Thums Up\t\t{self.thumsup.get()}\t\t{self.d_thu_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.soap.get()}\t\t{self.d_l_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.maaza.get()}\t\t{self.d_m_p}")

            self.txtarea.insert(END, f"\n-------------------------------------")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END, f"\nCosmetic tax\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "0.0":
                self.txtarea.insert(END, f"\nGrocery tax\t\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_taxx.get() != "0.0":
                self.txtarea.insert(END, f"\nCold Drink tax\t\t\t\t{self.cold_drinks_taxx.get()}")
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.txtarea.insert(END, f"\nTotal Bill :\t\t\t{self.Total_bill}")
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you  want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill.no : {self.bill_no.get()} Saved Successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
             messagebox.showerror("Error","invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear?")
        if op > 0:

            # ============cosmatics=======================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.gel.set(0)
            self.loshan.set(0)

            # ===============grocery========================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.sugar.set(0)
            self.wheat.set(0)
            self.tea.set(0)

            # ===============cold drinks======================
            self.maaza.set(0)
            self.thumsup.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            self.coke.set(0)

            # ==========Total price and tax varialbes==================

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_taxx.set("")

            # ========customer=========================

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def  Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit?")
        if op>0:
            self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
