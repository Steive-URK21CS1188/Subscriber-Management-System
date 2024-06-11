# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:26:07 2020

@author: Steive
"""

import mysql.connector as mc
s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
cur=s.cursor()
if s.is_connected():
    print("Connected Sucessfully")
    
cur.execute("create table if not exists Subscriber(SubscriberNo varchar(25) primary key,Name varchar(25) not null,Mobile varchar(25) not null,ProductType varchar(25) not null,CreditCardNo varchar(25) not null,Address varchar(100) not null,State varchar(25) not null,EmailId varchar(25) not null,Scheme varchar(25) not null,FacilitiesReq varchar(25) not null,Validity date not null,BillReceivingMode varchar(25) not null,PaymentMode varchar(25) not null,Status varchar(25) not null)")
cur.execute("create table if not exists Payment(BillNo varchar(25) not null,BillingDate date not null,SubscriberNo varchar(25) primary key,Name varchar(25) not null,Mobile varchar(25) not null,ProductType varchar(25) not null,Recharge varchar(25) not null,DueDate date not null,Dateofpayment date not null,PaidAmount varchar(25) not null,DueTransaction varchar(25) not null,TransactionStatus varchar(25) not null)") 
s.commit()
    
def Add_Subs():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a=int(input("Enter Subscriber Number:"))
    b=input("Enter Subscriber Name:")
    c=int(input("Enter Mobile no.:"))
    d=input("Enter Product Type [Prepaid/Postpaid]:")
    e=input("Enter Credit card No.:")
    f=input("Enter Address:")
    h=input("Enter State:")
    i=input("Enter E-Mail:")
    j=input("Enter Scheme/Plan:")
    k=input("Enter Facilities required [SMS/STD/International/Conferencing/Forwarding]:")
    l=input("Enter Validity:")
    n=input("Enter Bill receiving mode [Post/SMS/E-Mail]:")
    o=input("Enter Payment mode [Cash/DD/Online]:")
    p=input("Enter Status:")
    q0="insert into Subscriber values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a,b,c,d,e,f,h,i,j,k,l,n,o,p)
    cur.execute(q0)
    s.commit()
    print("---Record Saved---")
    
def Add_Pay():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a0=input("Enter Billing Date:")
    a1=int(input("Enter Bill No:"))
    a=int(input("Enter Subscriber Number:"))
    b=input("Enter Subscriber Name:")
    c=int(input("Enter Mobile no.:"))
    d=input("Enter Product Type [Prepaid/Postpaid]:")
    m1=int(input("Enter Ammount to be Recharge:"))
    o1=input("Enter Due Date:")
    o2=input("Enter Date of Payment:")
    o3=int(input("Enter Paid Amount:"))
    o4=input("Enter Due Transaction:")
    p=input("Enter Transaction Status:")
    q1="insert into Payment values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a1,a0,a,b,c,d,m1,o1,o2,o3,o4,p)
    cur.execute(q1)
    s.commit()
    print("---Record Saved---")
    
def Modify_Subs():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a=input("Enter Subscriber Number:")
    cur.execute("select * from Payment where SubscriberNo='{}'".format(a))
    d=cur.fetchall()
    if d==():
        print("Sorry No Record Found!..")
    else:
        a1=input("Enter Product Type:")
        a2=input("Enter Scheme:")
        a3=input("Enter Facilities Required:")
        a4=input("Enter Validity:")
        a6=input("Enter Bill Received Mode:")
        a7=input("Enter Payment Mode:")
        a8=input("Enter Status:")
        q2="update Subscriber set ProductType='{}',Scheme='{}',FacilitiesReq='{}',Validity='{}',BillReceivingMode='{}',PaymentMode='{}',Status='{}' where SubscriberNo='{}'".format(a1,a2,a3,a4,a6,a7,a8,a)
        cur.execute(q2)
        s.commit()   
        print("---Record Updated---")
def Modify_Pay():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a=input("Enter Subscriber Number:")
    cur.execute("select * from Payment where SubscriberNo='{}'".format(a))
    d=cur.fetchall()
    if d==():
        print("Sorry No Record Found!..")
    else:
        a1=input("Enter Product Type:")
        a2=input("Enter Recharge:")
        a3=input("Enter Due Amount:")
        a4=input("Enter Transaction Status:")
        q2="update Payment set ProductType='{}',Recharge='{}',DueTransaction='{}',TransactionStatus='{}' where SubscriberNo='{}'".format(a1,a2,a3,a4,a)
        cur.execute(q2)
        s.commit()
        print("---Record Updated---")
    
def Delete_Subs():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a=input("Enter Subscriber No to Delete:")   
    cur.execute("select * from Subscriber where SubscriberNo='{}'".format(a))
    d=cur.fetchall()
    if d==():
        print("Sorry No Record Found!..")
    else:
        q9="delete from Subscriber where SubscriberNo='{}'".format(a)
        cur.execute(q9)
        s.commit()
        print("---Record Deleted---")
    
def Delete_Pay():
    s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
    cur=s.cursor()
    a=input("Enter Subscriber No to delete:")   
    cur.execute("select * from Payment where SubscriberNo='{}'".format(a))
    d=cur.fetchall()
    if d==():
        print("Sorry No Record Found!..")
    else:
        q9="delete from Payment where SubscriberNo='{}'".format(a)
        cur.execute(q9)
        s.commit()
        print("---Record Deleted---")

def Search_Subs():
    def name():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a=input("Enter Subscriber Name to search:")
        q5="select * from Subscriber where Name='{}'".format(a)
        cur.execute(q5)
        d=cur.fetchall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)
    def mobile():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a5=input("Enter Mobile No to Search:")
        q4="select * from Subscriber where Mobile='{}'".format(a5)
        cur.execute(q4)
        d=cur.fetchall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)
    def subsno():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a3=input("Enter Subscriber No to Search:")
        q2="select * from Subscriber where SubscriberNo='{}'".format(a3)
        cur.execute(q2)
        d=cur.fetchall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)    
    while True:
        print("\n")
        print("***WEOLCOME TO SUBSCRIBER SEARCH***")
        print("\n")
        print("1--->To Search on Name")
        print("2--->To Search on Subscriber No")
        print("3--->To Search on Mobile No")
        print("4--->Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
           name()
        elif ch==2:
             subsno()
        elif ch==3:
             mobile()
        elif ch==4:
             break
        else:
            print("invalid choice")

def Search_Pay():
    def subsno():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a3=input("Enter Subscriber No to Search:")
        q2="select * from Payment where SubscriberNo='{}'".format(a3)
        cur.execute(q2)
        d=cur.fetchall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)        
    def billno():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a1=input("Enter Bill No to Search:")
        q1="select * from Payment where BillNo='{}'".format(a1)
        cur.execute(q1)
        d=cur.fetchall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)
    def mobile():
        s=mc.connect(host="localhost",user="root",passwd="sqlpassword123",database="ios")
        cur=s.cursor()
        a5=input("Enter Mobile No to Search:")
        q4="select * from Payment where Mobile='{}'".format(a5)
        cur.execute(q4)
        d=cur.fecthall()
        if d==[]:
            print("Sorry No Record Found!..")
        else:
            print(d)    
    while True:
        print("\n")
        print("***WEOLCOME TO PAYMENTS SEARCH***")
        print("\n")
        print("1--->To Search on Billno")
        print("2--->To Search on Subscriber No")
        print("3--->To Search on Mobile No")
        print("4--->Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            billno()
        elif ch==2:
            subsno()          
        elif ch==3:
            mobile()
        elif ch==4:
            break
        else:
             print("invalid choice")

while True:
    print("\n")
    print("****WELCOME TO Mobile SYSTEM MANAGEMENT****")
    print("\n")
    print("1-->Administrator")
    print("2-->User")
    print("3-->Exit")
    ch=int(input("Enter your Choice:"))
    if ch==1:
        ad=int(input("Enter Pin:"))
        p=12345
        if ad==p:
            while True:
                print("\n")
                print("****WELCOME TO ADMIN****")
                print("\n")
                print("1-->Subscriber Details")
                print("2-->Payment Details")
                print("3-->Exit")
                c=int(input("Enter your Choice:"))
                if c==1:
                    print("\n")
                    print("****WELCOME TO SUBSCRIBER MODULE****")
                    print("\n")
                    print("1-->Add Subscriber")
                    print("2-->Modify Subscriber")
                    print("3-->Delete Subscriber")
                    print("4-->Search Subscriber")
                    print("5-->Exit")
                    c=int(input("Enter your Choice:"))
                    if c==1:
                       Add_Subs()
                    elif c==2:
                         Modify_Subs()
                    elif c==3:
                         Delete_Subs()
                    elif c==4:
                         Search_Subs()
                    elif c==5:
                         break
                    else:
                        print("Invalid Choice")        
                elif c==2:
                    print("\n")
                    print("****WELCOME TO PAYMENT MODULE****")
                    print("\n")
                    print("1-->Add Payment")
                    print("2-->Modify Payment")
                    print("3-->Delete Payment")
                    print("4-->Search Payment")
                    print("5-->Exit")
                    c=int(input("Enter your Choice:"))
                    if c==1:
                        Add_Pay()
                    elif c==2:
                        Modify_Pay()
                    elif c==3:
                        Delete_Pay()
                    elif c==4:
                        Search_Pay()
                    elif c==5:
                         break
                    else:
                        print("Invalid Choice")                   
                elif c==3:
                     break
                else:
                    print("Invalid Choice")
        else:
            print("Access Denied - Admin Only...")
    elif ch==2:
        while True:
            print("\n")
            print("****WELCOME TO USER****")
            print("\n")
            print("1-->Payment Details")
            print("2-->Exit")
            c=int(input("Enter your Choice:"))
            if c==1:
               print("\n")
               print("****WELCOME TO PAYMENT MODULE****")
               print("\n")
               print("1-->Add Payment")
               print("2-->Modify Payment")
               print("3-->Search Payment")
               print("4-->Exit")
               c=int(input("Enter your Choice:"))
               if c==1:
                   Add_Pay()
               elif c==2:
                   Modify_Pay()
               elif c==3:
                   Search_Pay()
               elif c==4:
                    break
               else:
                    print("Invalid Choice")
            elif c==2:
                break
            else:
                print("Invalid Choice")
    elif ch==3:
        break
    else:
        print("Invalid Choice")


        
cur.execute("select last_day(curdate());")
r=cur.fetchone()
cur.execute("select curdate()")
y=cur.fetchone()
if r==y:
    cur.execute("select SubscriberNo,Name,ProductType,Scheme,FacilitiesReq from Subscriber")
    f=cur.fetchall()
    print("Subscriber's Plan")    
    for row in f:      
        print(row)
    cur.execute("select SubscriberNo,Name from Subscriber where Status='Pending'")
    f=cur.fetchall()
    if f==[]:
        print("No Subscribers with Outstanding Bill")
    else:
        print("Subscriber - Outstanding Bills")
        for row in f:
            print(row)
s.commit()        
s.close()