from tkinter import*
root=Tk()
root.title("LIBRARY MANAGEMENT SYSTEM")
root.configure(background="black")
def Add_Record():
    f=open('rupali.txt','a')
    STUDENT_NAME = s1.get()
    STUDENT_ID   = s2.get()
    BRANCH       = s3.get()
    SUBJECT      = s4.get()
    BOOK_NAME    = s5.get()
    TOTAL_BOOKS  = s6.get()
    ISSUE_DATE   = s7.get()
    RETURN_DATE  = s8.get()
    #if(STUDENT_NAME=='' or STUDENT_ID=='' or BRANCH=='' or SUBJECT=='' BOOK_NAME=='' or TOTAL_BOOKS==''or ISSUE_BOOKS==''or RETURN_BOOKS==''):
    #print("Details can't be empty!")
    #exit()
    f.writelines(STUDENT_NAME.ljust(20)+STUDENT_ID.ljust(20)+BRANCH.ljust(20)+SUBJECT.ljust(20)+BOOK_NAME.ljust(20)+TOTAL_BOOKS.ljust(20)+ISSUE_DATE.ljust(20)+RETURN_DATE.ljust(20)+"\n")
    print("Record added to the system successfully!")
    print ('Student Name: {0}'.format(STUDENT_NAME)) 
    print ('Student Id: {0}'.format(STUDENT_ID))
    print ('Branch: {0}'.format(BRANCH))
    print ('Subject: {0}'.format(SUBJECT))
    print ('Book Name: {0}'.format(BOOK_NAME))
    print ('Total Books : {0}'.format(TOTAL_BOOKS))
    print ('Issue date: {0}'.format(ISSUE_DATE))
    print ('Return date: {0}'.format(RETURN_DATE))
    f.close()
    
def get_first():
    f=open("rupali.txt",'r')
    ctr=len(f.readlines())
    if(ctr==0):
       print("There are no current details in the system!")
    else:
      f=open("rupali.txt",'r')
      k=f.readlines()[0]  
      j=k.split()
      print("The current details in the system:")
      print('Student Name: {0}'.format(j[0])) 
      print('Student Id: {0}'.format(j[1]))
      print('Branch: {0}'.format(j[2]))
      print('Subject: {0}'.format(j[3]))
      print('Book Name: {0}'.format(j[4]))
      print('Total Books : {0}'.format(j[5]))
      print('Issue date: {0}'.format(j[6]))
      print('Return date: {0}'.format(j[7]))
    f.close()


def get_last():
    f=open("rupali.txt",'r')
    ctr=len(f.readlines())
    if(ctr==0):
       print("There are no last details in the system!")
    else:
      f=open("rupali.txt",'r')
      k=f.readlines()[0]  
      j=k.split()
      print("The last details in the system:")
      print('Student Name: {0}'.format(j[0])) 
      print('Student Id: {0}'.format(j[1]))
      print('Branch: {0}'.format(j[2]))
      print('Subject: {0}'.format(j[3]))
      print('Book Name: {0}'.format(j[4]))
      print('Total Books : {0}'.format(j[5]))
      print('Issue date: {0}'.format(j[6]))
      print('Return date: {0}'.format(j[7]))
    f.close()



def get_next():
    f=open("rupali.txt",'r')
    ctr=len(f.readlines())
    if(ctr==0):
       print("There are no up coming details in the system!")
    else:
      f=open("rupali.txt",'r')
      k=f.readlines()[0]  
      j=k.split()
      print("The next details in the system:")
      print('Student Name: {0}'.format(j[0])) 
      print('Student Id: {0}'.format(j[1]))
      print('Branch: {0}'.format(j[2]))
      print('Subject: {0}'.format(j[3]))
      print('Book Name: {0}'.format(j[4]))
      print('Total Books : {0}'.format(j[5]))
      print('Issue date: {0}'.format(j[6]))
      print('Return date: {0}'.format(j[7]))
    f.close()



def get_previous():
    f=open("rupali.txt",'r')
    ctr=len(f.readlines())
    if(ctr==0):
       print("There are no previous details in the system!")
    else:
      f=open("rupali.txt",'r')
      k=f.readlines()[0]  
      j=k.split()
      print("The previous details in the system:")
      print('Student Name: {0}'.format(j[0])) 
      print('Student Id: {0}'.format(j[1]))
      print('Branch: {0}'.format(j[2]))
      print('Subject: {0}'.format(j[3]))
      print('Book Name: {0}'.format(j[4]))
      print('Total Books : {0}'.format(j[5]))
      print('Issue date: {0}'.format(j[6]))
      print('Return date: {0}'.format(j[7]))
    f.close()

def update():

    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=s5.get()
    x6=s6.get()
    x7=s7.get()
    x8=s8.get()
    f=open("rupali.txt",'r')
    k=f.readlines()
    f.close()
    f=open("rupali.txt",'w')
    z=0
    for i in k:
        j=i.split()
        if(j[0]!=x1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(20)+j[5].ljust(20)+j[6].ljust(20)+j[7].ljust(20)+"\n")
            
            
        else:
            f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(20)+x6.ljust(20)+x7.ljust(20)+x8.ljust(20)+"\n")
            z=1
            print("The deatils of the student has been successfully updated!")
            print ('Updated Student Name: {0}'.format(x1))
            print ('Updadted Student Id: {0}'.format(x2))
            print ('Updated Branch: {0}'.format(x3))
            print ('Updated Subject: {0}'.format(x4))
            print ('Updated Book Name: {0}'.format(x5))
            print ('Updated Total Books : {0}'.format(x6))
            print ('Updated Issue date: {0}'.format(x7))
            print ('Updated Return date: {0}'.format(x8))
    if(z==0):
        s9.set("The details cannot be updated")

def Search():
    k=s1.get()
    f=open('rupali.txt','r')
    h=f.readlines()
    flag=0
    for i in h: 
        j=i.split() 
        if(j[0]==k): 
            print("STUDENT DEATAILS found!")  
            print ('Student Name:{0}'.format(j[0])) 
            print ('Student Id: {0}'.format(j[1]))
            print ('Branch: {0}'.format(j[2]))
            print ('Subject: {0}'.format(j[3]))
            print ('Book Name: {0}'.format(j[4]))
            print ('Total Books : {0}'.format(j[5]))
            print ('Issue date: {0}'.format(j[6]))
            print ('Return date: {0}'.format(j[7])) 
            flag=1
    if(flag==0):
            print("Details not in the system!!\n")              
             
    f.close()        
            
def delete(): 
    x1=s1.get() 
    f=open("rupali.txt","r") 
    lines=f.readlines()  
    f.close() 
    f=open("rupali.txt","w")
    flag=0 
    for i in lines: 
        m=i.split()  
        if(m[0]!=x1): 
           f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+m[5].ljust(20)+m[6].ljust(20)+m[7].ljust(20)+"\n")
        else:
           print("The following details has been deleted!!\n")
           print ('Student Name: {0}'.format(m[0])) 
           print ('Student Id: {0}'.format(m[1]))
           print ('Branch: {0}'.format(m[2]))
           print ('Subject: {0}'.format(m[3]))
           print ('Book Name: {0}'.format(m[4]))
           print ('Total Books : {0}'.format(m[5]))
           print ('Issue date: {0}'.format(m[6]))
           print ('Return date: {0}'.format(m[7])) 
    if(flag==0):
        print("The details could not be found in the system!!\n")

         
    f.close() 

def reset():
     s1.set("")
     s2.set("") 
     s3.set("") 
     s4.set("") 
     s5.set("") 
     s6.set("")
     s7.set("")
     s8.set("")

def view_all():
     f=open("rupali.txt","r") 
     tables=f.readlines()
     k=1
     flag=0 
     for i in tables:
          print("Details",k," = ",i)
          k=k+1
          flag=1
     if(flag==0):
        print("There are no details in the system!!") 

def clear():
     f=open("rupali.txt","r+")
     f.truncate()
     print("The system has been cleared !!\n")            
    

l1=Label(root,text="LIBRARY MANAGEMENT SYSTEM",fg="black",bg="orange",font=('Algerian',26,'bold'),width="64").place(x=0,y=5)
l2=Label(root,text="STUDENT_NAME",font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=120)
l3=Label(root,text="STUDENT_ID ", font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=170)
l4=Label(root,text="BRANCH",      font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=220)
l5=Label(root,text="SUBJECT",     font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=270)
l6=Label(root,text="BOOK_NAME",   font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=320)
l7=Label(root,text="TOTAL BOOKS", font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=370)
l8=Label(root,text="ISSUE_DATE",  font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=420)
l9=Label(root,text="RETURN_DATE", font=('Ariel',18,'bold'),bg="black",fg="orange",width="13").place(x=200,y=470)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()
s9=StringVar()

e2=Entry(root,textvariable=s1,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=126)
e3=Entry(root,textvariable=s2,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=176)
e4=Entry(root,textvariable=s3,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=226)
e5=Entry(root,textvariable=s4,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=276)
e6=Entry(root,textvariable=s5,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=326)
e7=Entry(root,textvariable=s6,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=376)
e8=Entry(root,textvariable=s7,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=426) 
e9=Entry(root,textvariable=s8,width=26,font=('Ariel',12,'bold'),bg="orange").place(x=500,y=476)


b1=Button(root,text="ADD",width=22,bg="orange",font=('Ariel',12,'bold'),command=Add_Record).place(x=900,y=124)
b2=Button(root,text="SEARCH",width=22,bg="orange",font=('Ariel',12,'bold'),command=Search).place(x=900,y=174)
b3=Button(root,text="UPDATE",width=22,bg="orange",font=('Ariel',12,'bold'),command=update).place(x=900,y=224)
b4=Button(root,text="DELETE",width=22,bg="orange",font=('Ariel',12,'bold'),command=delete).place(x=900,y=274)
b5=Button(root,text="RESET",width=22,bg="white",font=('Ariel',12,'bold'),command=reset).place(x=200,y=545)
b6=Button(root,text="VIEW ALL",width=23,bg="white",font=('Ariel',12,'bold'),command=view_all).place(x=500,y=545)
b7=Button(root,text="CLEAR",width=22,bg="white",font=('Ariel',12,'bold'),command=clear).place(x=900,y=545)

b11=Button(root,text="CURRENT",width=22,bg="orange",font=('Ariel',12,'bold'),command=get_first).place(x=900,y=324)
b14=Button(root,text="LAST",width=22,bg="orange",font=('Ariel',12,'bold'),command=get_last).place(x=900,y=374)
b13=Button(root,text="NEXT",width=22,bg="orange",font=('Ariel',12,'bold'),command=get_next).place(x=900,y=424)
b12=Button(root,text="PREVIOUS",width=22,bg="orange",font=('Ariel',12,'bold'),command=get_previous).place(x=900,y=474)



root.mainloop()     
            

    




