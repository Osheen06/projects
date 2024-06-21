import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Osheen@8090",database="osheen06")
mycursor=mydb.cursor()
"""if mydb.is_connected():
    print("successfully connected")
else:
    print("error")"""
print("WELCOME TO OSHEEN THEATRE TICKET BOOKING")
print("*"*60)
print("Choose any one option from below : ")
print("1. Sign up")
print("2. Log in")
print("3. Seat preference")
print("4. Payment")
print("5. Update seat preference")
print("6. Delete account")
ch=int(input("Enter your choice : "))
if ch==1:
    print("WELCOME TO OSHEEN THEATRE SIGN UP PAGE")
    print("*******************************************************")
    ans="yes"
    while ans.lower()=="yes":
        name=input("Enter your name : ")
        gender=input("Enter your gender : ")
        passwd=input("Enter your password (ONLY IN ALPHABETS) : ")
        tktno=int(input("Enter your ticket number : "))
        movie=input("Enter movie you want to watch: ")
        query="insert into tkt values('{0}','{1}','{2}',{3},'{4}')".format(name,gender,passwd,tktno,movie)
        mycursor.execute(query)
        mydb.commit()
        print("Your account has been added successfully!")
        print("You may proceed to book your show now")
        query2="select *from tkt"
        mycursor.execute(query2)
        data=mycursor.fetchall()
        if data!=None:
            print("Your details are : ")
            print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE")
            print("*"*150)
            for row in data:
                print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4])
                print("*"*150)
            ans=input("Do you want to add more accounts? : ")
    if ans.lower()=="no":
        print("okay bye")

if ch==2:
    print("WELCOME TO OSHEEN THEATRE LOG IN PAGE")
    print("*******************************************************")
    nrec=mycursor.rowcount
    a=int(input("Enter your ticket number: "))
    query="select *from tkt where tktno="+str(a)
    mycursor.execute(query)
    data=mycursor.fetchmany(1)
    if data!=None:
        print("Your details are : ")
        print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in data:
            print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4])
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("No record found. Kindly sign in or TRY AGAIN")

if ch==3:
    print("WECLOME TO OSHEEN THEATRE SEAT BOOKING PAGE")
    print("*******************************************************")
    print("The types of seat we provide at our theatre is :")
    print("1. Regular")
    print("2. Prime")
    print("3. Platinum")
    ch=int(input("Enter your choice of seat: "))
    if ch==1:
        tktno=int(input("Please enter your ticket number : "))
        seat=int(input("Please re-enter your seat preference : "))
        query1="insert into seat values({0},{1})".format(tktno,seat)
        mycursor.execute(query1)
        mydb.commit()
        query2="select *from tkt,seat where seat=1 and tkt.tktno={0} and seat.tktno={1}".format(tktno,tktno)
        mycursor.execute(query2)
        data=mycursor.fetchmany(1)
        if data!=None:
            print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"SEAT P.")
            print("*"*150)
            for row in data:
                print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%30s"%row[4],"%30s"%row[5],"%30s"%row[6])
                print("*"*150)
                print("## Your seat has been booked successfully!")
    if ch==2:
        tktno=int(input("Please enter your ticket number : "))
        seat=int(input("Please re-enter your seat preference : "))
        query1="insert into seat values({0},{1})".format(tktno,seat)
        mycursor.execute(query1)
        mydb.commit()
        query2="select *from tkt,seat where seat=2 and tkt.tktno={0} and seat.tktno={1}".format(tktno,tktno)
        mycursor.execute(query2)
        data=mycursor.fetchmany(1)
        if data!=None:
            print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"SEAT P.")
            print("*"*150)
            for row in data:
                print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4],"%20s"%row[5],"%20s"%row[6])
                print("*"*150)
        print("## Your seat has been booked successfully!")
    if ch==3:
        tktno=int(input("Please enter your ticket number : "))
        seat=int(input("Please re-enter your seat preference : "))
        query1="insert into seat values({0},{1})".format(tktno,seat)
        mycursor.execute(query1)
        mydb.commit()
        query2="select *from tkt,seat where seat=3 and tkt.tktno={0} and seat.tktno={1}".format(tktno,tktno)
        mycursor.execute(query2)
        data=mycursor.fetchmany(1)
        if data!=None:
            print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"SEAT P.")
            print("*"*150)
            for row in data:
                print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%20s"%row[4],"%20s"%row[5],"%20s"%row[6])
                print("*"*150)
                print("## Your seat has been booked successfully!")

if ch==4:
    print("WECLOME TO OSHEEN THEATRE SEAT PAYMENT PAGE")
    print("*****************************************************************")
    print(" RATE LIST")
    print("--------------------------------------------------------")
    print("1. Regular Seat| RS: ₹200/- (+18% GST) ")
    print("2. Prime | RS: ₹500/- (+18% GST) ")
    print("3. Platinum | RS: ₹1000/- (+18% GST) ")
    ch=int(input("Please re-enter your seat preference : "))
    if ch==1:
        a=200*18/100+200
        print("Your total amount is ₹",a)
        print("You can only pay via CASH at the counter")
        ans="yes"
        while ans=="yes":
            tktno=int(input("Enter your ticket number : "))
            ch=int(input("Please re-enter your seat preference : "))
            a=print(200*18/100+200)
            query1="insert into payment values({0},'{1}')".format(tktno,a)
            mycursor.execute(query1)
            mydb.commit()
            query="select *from tkt,payment,seat where seat.seat={} and payment.tktno={} and tkt.tktno={} and seat.tktno={}".format(ch,tktno,tktno,tktno)
            mycursor.execute(query)
            ans=input("Do you want to continue? : ")
            data=mycursor.fetchall()
            if data!=None:
                print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"PAYMENT","%20s"%"TICKET NUMBER","%20s"%"SEAT")
                print("*"*200)
                for row in data:
                    print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%30s"%row[4],"%30s"%row[5],"%30s"%row[6],"%20s"%row[7],"%20s"%row[8])
                    print("*"*200)
        if ch==2:
            b=500*18/100+500
            print("Your total amount is ₹",b)
            print("You can only pay via CASH at the counter")
            ans="yes"
            while ans=="yes":
                tktno=int(input("Enter your ticket number : "))
                ch=int(input("Please re-enter your seat preference : "))
                b=print(500*18/100+500)
                query1="insert into payment values({0},'{1}')".format(tktno,b)
                mycursor.execute(query1)
                mydb.commit()
                data=mycursor.fetchall()
                print(data)
                query="select *from tkt,payment,seat where seat.seat={} and payment.tktno={} and tkt.tktno={} and seat.tktno={}".format(ch,tktno,tktno,tktno)
                mycursor.execute(query)
                ans=input("Do you want to continue? : ")
                data=mycursor.fetchall()
                if data!=None:
                    print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"PAYMENT","%20s"%"TICKET NUMBER","%20s"%"SEAT")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    for row in data:
                        print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%30s"%row[4],"%30s"%row[5],"%30s"%row[6],"%20s"%row[7],"%20s"%row[8])
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if ch==3:
        c=1000*18/100+1000
        print("Your total amount is ₹",c)
        print("You can only pay via CASH at the counter")
        ans="yes"
        while ans=="yes":
            tktno=int(input("Enter your ticket number : "))
            c=print(1000*18/100+1000)
            query1="insert into payment values({0},'{1}')".format(tktno,c)
            mycursor.execute(query1)
            mydb.commit()
            data=mycursor.fetchall()
            print(data)
            query="select *from tkt,payment,seat where seat.seat={} and payment.tktno={} and tkt.tktno={} and seat.tktno={}".format(ch,tktno,tktno,tktno)
            mycursor.execute(query)
            ans=input("Do you want to continue? : ")
            data=mycursor.fetchall()
            if data!=None:
                print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NUMBER","%20s"%"PAYMENT","%20s"%"TICKET NUMBER","%20s"%"SEAT")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for row in data:
                    print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%30s"%row[4],"%30s"%row[5],"%30s"%row[6],"%20s"%row[7],"%20s"%row[8])
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

if ch==5:
    print("WELCOME TO OSHEEN THEATRE SEAT UPDATE PAGE")
    print("*******************************************************")
    tktno=int(input("Enter your ticket number: "))
    query="select *from seat where tktno={0}".format(tktno)
    mycursor.execute(query)
    data=mycursor.fetchmany()
    if data!=None:
        print("## RECORD FOUND. Details are : ")
        print("%30s"%"TICKET NO.","%20s"%"SEAT P. ")
        print("-----------------------------------------------------------------------------------------")
        for row in data:
            print("%30s"%row[0],"%20s"%row[1])
            print("----------------------------------------------------------------------------------------")
    ans=input("Do you want to continue? :")
    ans="yes"
    while ans.lower()=="yes":
        s=int(input("Enter new seat preference: "))
        tktno=int(input("Enter your ticket number: "))
        query="update seat set seat={0} where tktno={1}".format(s,tktno)
        mycursor.execute(query)
        mydb.commit()
        query2="select *from tkt,seat where tkt.tktno={0} and seat.seat={1}".format(tktno,s)
        mycursor.execute(query2)
        data=mycursor.fetchall()
        if data!=None:
            print("## SEAT PREFERENCE UPDATED SUCCESSFULLY! ")
            print("%30s"%"NAME","%20s"%"GENDER","%20s"%"PASSWORD","%20s"%"TICKET NUMBER","%20s"%"MOVIE","%20s"%"TICKET NO.","%20s"%"SEAT")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for row in data:
                print("%30s"%row[0],"%20s"%row[1],"%20s"%row[2],"%20s"%row[3],"%30s"%row[4],"%30s"%row[5],"%30s"%row[6])
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                break
    if ans.lower()=="no":
        print("OKAY BYE")

if ch==6:
    print("WELCOME TO OSHEEN THEATRE DELETE PAGE")
    print("*******************************************************")
    tktno=int(input("Enter your ticket number: "))
    query="delete from tkt where tktno={}".format(tktno)
    mycursor.execute(query)
    mydb.commit()
    print("## YOUR ACCOUNT HAS BEEN DELETED SUCCESSFULLY")
    
    
        
        
        
        
