import tkinter

Try=0
rownum=7
colnum=7
LockedAccount=dict()

def init():
	global file
	global Block
	global LockedAccount
	global Database
	file = open("DataBase.txt","r+")
	Database = dict(eval(file.read()))
	Block = open("Blocked.txt","w+")
	
init()

def Enter_ID() :
	global ID
	ID = int(id_Entry.get())
	if ID in LockedAccount.keys():
			Block_User_Window()	
	elif ID in Database.keys():
			Pass_Window()	
	else : 
		Error_User_Window()
		
		
def Enter_Password() :
	global Try
	global LockedAccount
	password = Pass_Entry.get()
	if Database[ID][1] == password : 
		Choices_Window()
	else:
		Try+=1
		if Try>2: 
			Balance=Database[ID][0]
			Password=Database[ID][1]
			Name=Database[ID][2]
			lockid=ID
			LockedAccount[lockid] = [Balance,Password,Name]
			Block_User_Window()
			Block.write(str(LockedAccount))

		else:
			Error_Pass_Window()
	
def Password_Change() :
	global DataBase
	global ID
	global file
	passwordch = Passchange_Entry.get()
	passwordrech = Passrechange_Entry.get()
	if passwordch == passwordrech : 
		if len(passwordch)>4:
			Passchange_Window()
		else:
			Database[ID][1]=passwordch
			file.write(str(Database))
			MainwindowInit()
	else:
		Passchange_Window()

def Phone_Operation():
	global DataBase
	global ID
	global file
	phone = Phone_Fawry1_Entry.get()
	bala = int(Phone_Fawry2_Entry.get())
	if (Database[ID][0]) >= bala : 
		Database[ID][0]=((Database[ID][0])-(bala))
		file.write(str(Database))
		ThankYou_Window()
	else:
		No_Balance_Window()

def ATM_Actuator_Out():
	print('ATM')
	
def Cash_Operation():
	global DataBase
	global ID
	global file
	phone = Cash_Withdraw_Entry.get()
	balan = int(Cash_Withdraw_Entry.get())
	if balan < 5000 :
		if (Database[ID][0]) >= balan : 
			Database[ID][0]=((Database[ID][0])-(balan))
			file.write(str(Database))
			ATM_Actuator_Out()
			ThankYou_Window()
		else:
			No_Balance_Window()
	else:
		Not_Allowed()
		
def Pass_Window():
	global mainpass
	global Pass_Entry
	mainpass=tkinter.Toplevel(mainW)
	mainpass.geometry("270x100+500+200")
	mainpass.title("ATM User Password")
	mainpass.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		mainpass.grid_rowconfigure(i,minsize=60)
		i+=1
	i=0
	while i< colnum:
		mainpass.grid_columnconfigure(i,minsize=60)
		i+=1
		
	Pass_Label=tkinter.Label(mainpass, text="Password")
	Pass_Label.grid(row=0,column=0)
	Pass_Entry=tkinter.Entry(mainpass,show='*')
	Pass_Entry.grid(row=0,column=1)
	Enter_Button2 = tkinter.Button(mainpass,text="Enter",command=Enter_Password)
	Enter_Button2.grid(row=0,column=2)

def Error_User_Window():
	global erroruser
	erroruser=tkinter.Toplevel(mainW)
	erroruser.geometry("270x100+500+200")
	erroruser.title("ATM User ID Error")
	erroruser.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		erroruser.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		erroruser.grid_columnconfigure(i,minsize=40)
		i+=1
		
	Error_ID_Label=tkinter.Label(erroruser, text="Error User ID, Please Enter again.")
	Error_ID_Label.grid(row=0,column=0)
	Enter_Button3 = tkinter.Button(erroruser,text="Enter",command=MainwindowInit)
	Enter_Button3.grid(row=1,column=1)

def No_Balance_Window():
	global nobalance
	nobalance=tkinter.Toplevel()
	nobalance.geometry("270x100+500+200")
	nobalance.title("ATM No Balance")
	nobalance.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		nobalance.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		nobalance.grid_columnconfigure(i,minsize=40)
		i+=1
		
	nobalance_Label=tkinter.Label(nobalance, text="No sufficient balance")
	nobalance_Label.grid(row=0,column=0)
	nobalance_Button3 = tkinter.Button(nobalance,text="ok",command=Cash_Operation)
	nobalance_Button3.grid(row=1,column=1)
	
def Not_Allowed():
	global noallowed
	noallowed=tkinter.Toplevel()
	noallowed.geometry("270x100+500+200")
	noallowed.title("ATM Not Allowed")
	noallowed.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		noallowed.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		noallowed.grid_columnconfigure(i,minsize=40)
		i+=1
		
	noallowed_Label=tkinter.Label(noallowed, text="Not allowed per transaction")
	noallowed_Label.grid(row=0,column=0)
	noallowed_Button3 = tkinter.Button(noallowed,text="ok",command=Cash_Withdraw_Window)
	noallowed_Button3.grid(row=1,column=1)
	
def ThankYou_Window():
	global ThankYou
	ThankYou=tkinter.Toplevel()
	ThankYou.geometry("270x100+500+200")
	ThankYou.title("ATM Thanks")
	ThankYou.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		ThankYou.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		ThankYou.grid_columnconfigure(i,minsize=50)
		i+=1
		
	ThankYou_Label=tkinter.Label(ThankYou, text="Thank you")
	ThankYou_Label.grid(row=0,column=2)
	ThankYou_Button = tkinter.Button(ThankYou,text="Ok",command=MainwindowInit)
	ThankYou_Button.grid(row=1,column=2)
	
def Error_Pass_Window():
	global errorpass
	errorpass=tkinter.Toplevel(mainpass)
	errorpass.geometry("270x100+500+200")
	errorpass.title("ATM User Password Error")
	errorpass.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		errorpass.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		errorpass.grid_columnconfigure(i,minsize=40)
		i+=1
		
	Error_Pass_Label=tkinter.Label(errorpass, text="Error User Password, Please Enter again.")
	Error_Pass_Label.grid(row=0,column=0)
	Enter_Button4 = tkinter.Button(errorpass,text="ok",command=Pass_Window)
	Enter_Button4.grid(row=1,column=1)

def Cash_Withdraw_Window():
	global Cash_Withdraw
	global Cash_Withdraw_Entry
	Cash_Withdraw=tkinter.Toplevel()
	Cash_Withdraw.geometry("270x130+500+200")
	Cash_Withdraw.title("ATM Cash WithDraw")
	Cash_Withdraw.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		Cash_Withdraw.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		Cash_Withdraw.grid_columnconfigure(i,minsize=40)
		i+=1
		
	Cash_Withdraw_Label=tkinter.Label(Cash_Withdraw, text="Enter CashwithDraw")
	Cash_Withdraw_Label.grid(row=0,column=0)
	Cash_Withdraw_Entry=tkinter.Entry(Cash_Withdraw)
	Cash_Withdraw_Entry.grid(row=0,column=1)
	Cash_Withdraw_Button = tkinter.Button(Cash_Withdraw,text="OK",command=Cash_Operation)
	Cash_Withdraw_Button.grid(row=2,column=1)
	
def Balance_User_Window():
	global Balance_User
	Balance_User=tkinter.Toplevel(choice)
	Balance_User.geometry("270x130+500+200")
	Balance_User.title("ATM User Balance")
	Balance_User.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		Balance_User.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		Balance_User.grid_columnconfigure(i,minsize=50)
		i+=1
		
	Balance_Inquiry_Label=tkinter.Label(Balance_User, text=("Your Name  :  "+str(Database[ID][2])))
	Balance_Inquiry_Label.grid(row=0,column=0)
	Balance_Inquiry_Label2=tkinter.Label(Balance_User, text=("Your Balance : "+str(Database[ID][0])))
	Balance_Inquiry_Label2.grid(row=1,column=0)
	Balance_Inquiry_Button = tkinter.Button(Balance_User,text="ok",command=MainwindowInit)
	Balance_Inquiry_Button.grid(row=2,column=0)

def Passchange_Window():
	global changepass
	global Passchange_Entry
	global Passrechange_Entry
	changepass=tkinter.Toplevel()
	changepass.geometry("270x130+500+200")
	changepass.title("ATM Change Password")
	changepass.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		changepass.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		changepass.grid_columnconfigure(i,minsize=40)
		i+=1
		
	Passchange_Label=tkinter.Label(changepass, text="Enter Password")
	Passchange_Label.grid(row=0,column=0)
	Passchange_Entry=tkinter.Entry(changepass,show='*')
	Passchange_Entry.grid(row=0,column=1)
	Passrechange_Label=tkinter.Label(changepass, text="Re-Enter Password")
	Passrechange_Label.grid(row=1,column=0)
	Passrechange_Entry=tkinter.Entry(changepass,show='*')
	Passrechange_Entry.grid(row=1,column=1)
	Passchange_Label_Button = tkinter.Button(changepass,text="OK",command=Password_Change)
	Passchange_Label_Button.grid(row=2,column=1)


def Phone_Fawry_Window():
	global Phone_Fawry
	global Phone_Fawry1_Entry
	global Phone_Fawry2_Entry
	Phone_Fawry=tkinter.Toplevel()
	Phone_Fawry.geometry("270x130+500+200")
	Phone_Fawry.title("ATM Change Password")
	Phone_Fawry.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		Phone_Fawry.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		Phone_Fawry.grid_columnconfigure(i,minsize=40)
		i+=1
		
	Phone_Fawry1_Label=tkinter.Label(Phone_Fawry, text="Enter Mobile")
	Phone_Fawry1_Label.grid(row=0,column=0)
	Phone_Fawry1_Entry=tkinter.Entry(Phone_Fawry)
	Phone_Fawry1_Entry.grid(row=0,column=1)
	Phone_Fawry2_Label=tkinter.Label(Phone_Fawry, text="Enter Recharge")
	Phone_Fawry2_Label.grid(row=1,column=0)
	Phone_Fawry2_Entry=tkinter.Entry(Phone_Fawry)
	Phone_Fawry2_Entry.grid(row=1,column=1)
	Phone_Label_Button = tkinter.Button(Phone_Fawry,text="OK",command=Phone_Operation)
	Phone_Label_Button.grid(row=2,column=1)
	
def Fawry_Choice():
	chose=var1.get()
	if chose == 0 :
		Phone_Fawry_Window()
	elif chose == 1 :
		Phone_Fawry_Window()
		print('e')
	elif chose == 2 :
		Phone_Fawry_Window()
	elif chose == 3 :
		Phone_Fawry_Window()


def Enabled_Choice():
	global DataBase
	global ID
	global file
	choose=var.get()
	if choose == 0 :
		Cash_Withdraw_Window()
	elif choose == 1 :
		Balance_User_Window()
	elif choose == 2 :
		Passchange_Window()
	elif choose == 3 :
		FawryService_Window()
	elif choose == 4 :
		exit()

def FawryService_Window():
	global Fawry
	global var1
	var1=tkinter.IntVar()
	Fawry=tkinter.Toplevel()
	Fawry.geometry("270x200+500+200")
	Fawry.title("ATM User Choices")
	Fawry.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		Fawry.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		Fawry.grid_columnconfigure(i,minsize=40)
		i+=1
		
	
	Orange = tkinter.Radiobutton(Fawry , text="Orange Recharge", variable= var1 ,value=0) 
	Orange.grid(row=0,column=1)
	Etisalat = tkinter.Radiobutton(Fawry , text="Etisalat Recharge", variable= var1 ,value=1) 
	Etisalat.grid(row=1,column=1)
	Vodafone = tkinter.Radiobutton(Fawry , text="Vodafone Recharge", variable= var1 ,value=2) 
	Vodafone.grid(row=2,column=1)
	We = tkinter.Radiobutton(Fawry , text="We Recharge", variable= var1 ,value=3) 
	We.grid(row=3,column=1)
	Enter_Fawry = tkinter.Button(Fawry,text="Select",command=Fawry_Choice)
	Enter_Fawry.grid(row=4,column=1)
	
def Choices_Window():
	global choice
	global var
	var=tkinter.IntVar()
	choice=tkinter.Toplevel()
	choice.geometry("270x200+500+200")
	choice.title("ATM User Choices")
	choice.resizable(width=False, height=False)
	
	i=0
	while i< rownum:
		choice.grid_rowconfigure(i,minsize=40)
		i+=1
	i=0
	while i< colnum:
		choice.grid_columnconfigure(i,minsize=40)
		i+=1
		
	
	Cash_Draw = tkinter.Radiobutton(choice , text="Cash Draw", variable= var ,value=0) 
	Cash_Draw.grid(row=0,column=1)
	Balance_Inquiry = tkinter.Radiobutton(choice , text="Balance Inquiry", variable= var ,value=1) 
	Balance_Inquiry.grid(row=1,column=1)
	Password_Change = tkinter.Radiobutton(choice , text="Password Change", variable= var ,value=2) 
	Password_Change.grid(row=2,column=1)
	Fawry_Service = tkinter.Radiobutton(choice , text="Fawry Service", variable= var ,value=3) 
	Fawry_Service.grid(row=3,column=1)
	Exit = tkinter.Radiobutton(choice , text="Exit", variable= var ,value=4) 
	Exit.grid(row=4,column=1)
	Enter_choice = tkinter.Button(choice,text="Select",command=Enabled_Choice)
	Enter_choice.grid(row=2,column=3)
	
def MainwindowInit():
	global mainW
	global id_Entry
	mainW = tkinter.Tk()
	mainW.geometry("270x100+500+200")
	mainW.title("ATM Machine")
	mainW.resizable(width=False,height=False)
	
	i=0
	while i < rownum :
		mainW.grid_rowconfigure(i,minsize=60)
		i+=1
		
	i=0
	while i < colnum :
		mainW.grid_columnconfigure(i,minsize=60)
		i+=1

	id_Label=tkinter.Label(mainW, text="id")
	id_Label.grid(row=0,column=0)
	id_Entry=tkinter.Entry(mainW)
	id_Entry.grid(row=0,column=1)
	Enter_Button1 = tkinter.Button(mainW,text="Enter",command=Enter_ID)
	Enter_Button1.grid(row=0,column=2)
	
