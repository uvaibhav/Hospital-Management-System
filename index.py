from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideeffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medicine = StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",35,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ================================Dataframe=======================================
        DataFrame=Frame(self.root,bd=10,relief=RIDGE)
        DataFrame.place(x=0,y=100,width=1350,height=380)

        
        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE, 
                                                font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE, 
                                                font=("arial",12,"bold"),text="Prescription")
        DataFrameRight.place(x=900,y=5,width=400,height=350)

        # ======================== buttons frame=========================================


        ButtonFrame=Frame(self.root,bd=10,relief=RIDGE)
        ButtonFrame.place(x=0,y=480,width=1350,height=65)


        # ========================= Details frame======================================


        DetailsFrame=Frame(self.root,bd=10,relief=RIDGE)
        DetailsFrame.place(x=0,y=545,width=1350,height=150)

        # =========================DataframeLeft========================

        lblNameTablet=Label(DataFrameLeft,text="Names Of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),
                                                                                width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideeffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.BloodPressure,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Storage,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Medicine,width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)


        # ===========================DataframeRight======================================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=38,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        # ==============================================Buttons======================================================================
        
        btnPrescription= Button(ButtonFrame,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnExit.grid(row=0,column=5)


        # ===============================================Table==================================================
        # ====================================Scrollbar============================================
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
       
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                    "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        # =======================Functionality Declaration=======================================================
        def iPrescriptionData(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.Nameoftablets.get(),
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberofTablets.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.nhsNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateOfBirth.get(),
                                                                                                        self.PatientAddress.get(),
                                                                                                        

                                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")










root=Tk()
ob=Hospital(root)
root.mainloop()
