# -------------IMPORTING MODULES-----------
# Declaring numpy as np
import numpy as np
# Declaring matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import csv
# Declaring mysql.connector as sql
import mysql.connector as sql

# Program for transfering csv data to mysql table

# defining funtion
def csv_to_sql():
    # Connecting python to mysql using my_db variable and connect function of sql library
    my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
    # Using cursor func to make the connection for executing SQL queries.
    my_cur=my_db.cursor()
    # Opening the file using open func
    file1=open("csv_to_sql.csv","r")
    # Reading file using reader func
    csv_cur=csv.reader(file1)
    # Using for loop for transfering each value to sql table 
    for i in csv_cur:
       query=("insert into METEORITES values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
       data=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]]
       my_cur.execute(query,data)
       my_cur.execute("commit")
    print("done..")
#Calling defined func (only one time otherwise it will keep on adding same values again and again)
#csv_t0_sql()
    
# Printing statements for user
print("-------------Enter your choice-------------")
print("1...USER")
print("2...EMPLOYEE")

# Asking user to enter it's choice
ch=int(input("Enter your choice: "))

# --------------USER---------------

# Applying if condition according to user's choice
if ch==1:
    # Showing visualised data according to user's choice

    # Giving choice to user 
    print("--------Enter your Choice---------")
    print("1...meteorite data acc. to year")
    print("2...meteorite data acc. to mass")
    print("3...meteorite data acc. to name and mass")
    print("4...Exit")

    # Asking user to enter it's choice
    choice=int(input("enter your choice...."))
    
    # Compairing user's choice using if condition
    # -------------------GRAPH ACCORDING TO YEAR--------------
    if choice==1:
        
        # stablizing connection between python and mysql
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        # Asking user to enter starting range for graph
        a=int(input("Enter starting year to see meteorite data: "))
        # Asking user to enter ending range for graph
        b=int(input("Enter ending year to see meteorite data: "))
        # Executing query using execute funtion
        my_cur.execute("select count(year), year from METEORITES group by year having year between {} and {};".format(a,b))
        # Fetching or getting all the data from mysql to python using fetchall func
        result=my_cur.fetchall()
        
        # Declaring two empty list
        x=[]
        y=[]
        # Using for loop for adding each and every value in the list
        for i in result:
            # appending value in list named x
            x.append(i[0])
            # appending value in list named y
            y.append(i[1])
        # printing both list   
        print(x)
        print(y)
        
        # Plotting bar graph using bar function of plt library
        plt.bar(y,x)
        # The ylim() function in pyplot module of matplotlib library is used to get or set the y-limits of the current axes.
        plt.ylim(0,50)
        # Giving label to x axsis
        plt.xlabel("year")
        # Giving label to y axsis
        plt.ylabel("no. of meteroites per year")
        # Giving tittle to the graph
        plt.title("METEORITES")
        # Displaying graph on screen using show func of plt library
        plt.show()

# --------------GRAPH ACCORDING TO MASS--------------

    if choice==2:
        # stablizing connection between python and mysql
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        a=int(input("Enter starting range of mass to see meteorite data: "))
        b=int(input("Enter ending range of mass to see meteorite data: "))
        # Executing query using execute funtion
        my_cur.execute("select count(mass_gm), mass_gm from METEORITES group by mass_gm having mass_gm between {} and {};".format(a,b))
        result=my_cur.fetchall()

        # appending values in the list
        x=[]
        y=[]
        for i in result:
            x.append(i[0])
            y.append(i[1])
        print(x)
        print(y)

        # Plotting Graph
        plt.bar(y,x)
        plt.ylim(0,5)
        plt.xlabel("mass")
        plt.ylabel("no. of meteroites acc. to mass")
        plt.title("METEORITES")
        plt.show()
        
#--------------GRAPH ACCORDING TO MASS AND NAME--------------
    if choice==3:
        # Connecting python to mysql using my_db variable and connect function of sql library
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        a=int(input("Enter no. of meteorites to see meteorite data: "))
        # Executing query using execute funtion
        my_cur.execute("select mass_gm, name from METEORITES limit {};".format(a))
        result=my_cur.fetchall()
    
        # appending values in the list
        x=[]
        y=[]
        for i in result:
            x.append(i[0])
            y.append(i[1])
        print(x)
        print(y)

        # Plotting Graph
        plt.bar(y,x)
        plt.ylim(0,5)
        plt.xlabel("mass")
        plt.ylabel("name of meteroites acc. to mass")
        plt.title("METEORITES")
        plt.show()
# -------------EXITING-------------------
    if choice==4:
        print("Exiting program...")
        exit()

# --------------EMPLOYEE---------------

if ch==2:
    
    # Giving choice to user
    print("--------Enter your Choice---------")
    print("1...Add")
    print("2...Update")
    print("3...Delete")
    print("4...Exit")

    # Asking user to enter it's choice
    c=int(input("Enter your choice..."))

# --------ADDING---------   
    if c==1:
        
        # stablizing connection between python and mysql
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        ch1='y'
        while ch1=='y':

            # Asking user to enter according to field
            name=input("Enter new name: ")
            id1=int(input("Enter new ID: "))
            n_type=input("Enter new name type: ")
            recclass=input("Enter new recclass: ")
            mass= float(input("Enter new mass in gm and only in integer type not in float: "))
            fall=input("Enter new fall type i.e, fell or found: ")
            year= int(input("Enter new year: "))
            reclat=float(input("Enter new reclat: "))
            reclong= float(input("Enter new reclong: " ))
            gloc=input("Enter new geoloction in brackets: ")
            
            # Executing query using execute funtion
            my_cur.execute("insert into METEORITES values('"+name+"','"+str(id1)+"','"+n_type+"','"+recclass+"','"+str(mass)+"','"+fall+"','"+str(year)+"','"+str(reclat)+"','"+str(reclong)+"','"+gloc+"');")
            my_db.commit()
            my_db.close()
            print("DETAILS ADDED....")
            ch1=input("Want to add more records y/n: ")

# -----------UPDATING-----------
    if c==2:
        # Connecting python to mysql using my_db variable and connect function of sql library
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        
        u_name=input("Enter name of meteorite for which you want to update record")

        # Giving choice to user
        print("--------Enter your Choice---------")
        print("1...Want to update few fields")
        print("2...Want to update 1 full record")
        print("3...Exit")

        # Asking user to enter it's choice
        n1=int(input("Enter your choice"))
        
        if n1==1:

            # Giving choice to user
            print("--------Enter your Choice---------")
            print("1...Change Name")
            print("2...Change Id")
            print("3...Change name type")
            print("4...Change mass")
            print("5...Exit")
            
            n2=int(input("Enter your choice..."))
            
            if n2==1:
                upd_name=input("Enter name...")
                # Executing query using execute funtion
                my_cur.execute("update METEORITES set name='"+upd_name+"' where name='"+u_name+"';")
                # saving the changes using commit func
                my_db.commit()
                my_db.close()
                
                print("RECORD UPDATED")
                
            if n2==2:
                upd_id=int(input("Enter Id..."))
                my_cur.execute("update METEORITES set id='"+str(upd_id)+"' where name='"+u_name+"';")
                # saving the changes using commit func
                my_db.commit()
                my_db.close()
                print("RECORD UPDATED")
            if n2==3:
                upd_n_type=input("Enter name type...")
                # Executing query using execute funtion
                my_cur.execute("update METEORITES set name_type='"+upd_n_type+"' where name='"+u_name+"';")
                # saving the changes using commit func
                my_db.commit()
                # Closing file
                my_db.close()
                
                print("RECORD UPDATED")
                
            if n2==4:
                upd_mass=float(input("Enter mass..."))
                
                # Executing query using execute funtion
                my_cur.execute("update METEORITES set mass_gm='"+str(upd_mass)+"' where name='"+u_name+"';")
                # saving the changes using commit func
                my_db.commit()
                # Closing file
                my_db.close()
                
                print("RECORD UPDATED")
                
            if n2==5:
                print("Exiting...")
                # Exiting the program
                exit()
                
        if n1==2:
            # stablizing connection between python and mysql
            my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
            # Using cursor func to make the connection for executing SQL queries.
            my_cur=my_db.cursor()

            # Asking user to enter according to field
            id1=int(input("Enter new ID: "))
            n_type=input("Enter new name type: ")
            recclass=input("Enter new recclass: ")
            mass= float(input("Enter new mass in gm and only in integer type not in float: "))
            fall=input("Enter new fall type i.e, fell or found: ")
            year= int(input("Enter new year: "))
            reclat=float(input("Enter new reclat: "))
            reclong= float(input("Enter new reclong: " ))
            gloc=input("Enter new geoloction in brackets: ")
            
            # Executing query using execute funtion
            my_cur.execute("update METEORITES set id='"+str(id1)+"',name_type='"+n_type+"',recclass='"+recclass+"',mass_gm='"+str(mass)+"',fall='"+fall+"',year='"+str(year)+"',reclat='"+str(reclat)+"',reclong='"+str(reclong)+"',Geolocation='"+gloc+"' where name='"+u_name+"'")
            # saving the changes using commit func
            my_db.commit()
            # Closing file
            my_db.close()
            
            print("RECORD UPDATED...")

# -------------DELETING-------------            
    if c==3:
        # Connecting python to mysql using my_db variable and connect function of sql library
        my_db= sql.connect(user="root",host="localhost",password="mysql@2005",database="janvi")
        # Using cursor func to make the connection for executing SQL queries.
        my_cur=my_db.cursor()
        ch='y'
        while ch=='y':
            d_record=input("Enter name of meteorite to delete record of that meteorite: ")
            
            # Executing query using execute funtion
            my_cur.execute("delete from METEORITES where name='"+d_record+"'")
            # saving the changes using commit func
            my_db.commit()
            # Closing file
            my_db.close()
            
            print("RECORD DELETED...")
            ch=input("Want to delete more record y/n: ")

# -----------EXITING-----------
    if c==4:
        # Exiting the program
        print("Exiting...")
        exit()


# THANK YOU
