import sqlite3
con=sqlite3.connect('PlasmaDb')
curs=con.cursor()


def InsertDonorPlasmaDetails(donor_id):
    #curs.execute(' drop table DonorPlasmaTb ')
    curs.execute('''create table if not exists DonorPlasmaTb(donorId int primary key,bloodGroup text,weight float,covidPositive text,
    covidDate text,plasmaDonate text,plasmaDate text,bp text,disease text)''')

    #donor_id=int(input("Enter your donar id  "))
    blood_group = input("Enter your blood group ")
    weight = float(input("Enter your weight "))
    covid_positive = input("Covid positive,Enter yes or no ")
    if covid_positive.__eq__("yes"):
        covid_date = input("Enter date ")
    else :
        covid_date=None
    plasma_donate = input("Previously donated plasma Y for yes and N for no ")
    if plasma_donate.__eq__("yes"):
        plasma_date = int(input("Enter the date you donated plasma "))
    else :
       plasma_date=None
    bp = input("Enter your bloop pressure ")
    n = int(input("Enter the number of diseases"))
    disease = ""
    for i in range(n):
        disease += input("Name the diseases you have ")

    records = (donor_id,blood_group, weight, covid_positive, covid_date, plasma_donate, plasma_date, bp, disease)

    curs.execute('''insert into DonorPlasmaTb(donorId,bloodGroup ,weight ,covidPositive ,
    covidDate,plasmaDonate ,plasmaDate ,bp ,disease ) values(?,?,?,?,?,?,?,?,?)''', records)
    con.commit()

def ShowDonorPlasmaRecords():
    curs.execute('SELECT * FROM DonorPlasmaTb')
    rows = curs.fetchall()

    for record in rows:
        print("Donor id is::  ",record[0])
        print("Blood group is::  ", record[1])
        print("Weight is::  ", record[2])
        print("Covid positive::  ", record[3])
        print("Covid date::  ", record[4])
        print("Plasma donate::   ", record[5])
        print("Plasma donate date::  ", record[6])
        print("Blood pressure is:: ", record[7])
        print("Diseases are::  ", record[8])
        print("------------------------------------------")

def DelAlldetails():
    '''donor_id = int(input("enter the donor id "))
    curs.execute("delete from DonorPlasmaTb where donorId=?", (donor_id,))
    con.commit()'''
    curs.execute("delete from DonorPlasmaTb")
    con.commit()
    print("successfully deleted")



def ShowDonorPlasmaRecordsById(id):
    curs.execute('SELECT * FROM DonorPlasmaTb where donorId=?',(id,))
    row = curs.fetchone()
    blood_group=row[1]
    weight=row[2]
    covid_positive=row[3]
    covid_date=row[4]
    plasma_donate=row[5]
    plasma_date=row[6]
    bp=row[7]
    disease= row[8]


    print("Your blood group is::  ", blood_group)
    print("Your weight is:: ", weight)
    print("Your  covid report is(positive or negative)::  ",covid_positive)
    print("Covid Date is::  ", covid_date )
    print("Donated plasma previously::  ", plasma_donate)
    print("Plasma donated Date is::  ",plasma_date)
    print("Your Blood pressure is::  ",bp )
    print("Diseases you have::   ", disease)

    print("------------*****------********---------****------------")

    ans=input("Change in Blood Group y/n ")
    if ans[0]=='y' or ans[0]=='Y':
        blood_group=input("Enter Blood group :: ")

    ans = input("change in weight y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        weight = int(input("Enter weight :: "))

    ans = input("change in covid_positive y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        covid_positive = input("Enter yes or no :: ")

    ans = input("change in  covid_date y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
         covid_date = input("Enter covid_date :: ")

    ans = input("change in plasma_donate y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        plasma_donate = input("Enter plasma_donate :: ")

    ans = input("change in plasma_date y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        plasma_date = input("Enter plasma_date :: ")

    ans = input("change in bp y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        bp = input("Enter bp :: ")

    ans = input("change in disease name y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        disease = int(input("Enter disease :: "))

    record=( blood_group,weight,covid_positive,covid_date,plasma_donate,plasma_date,bp,disease,id)

    return record

def UpdateYourDetails():
    donor_id = int(input("enter the donor id "))
    record = ShowDonorPlasmaRecordsById(donor_id)
    curs.execute('''update DonorPlasmaTb set bloodGroup=? ,weight=? ,covidPositive=?,
    covidDate=? ,plasmaDonate=? ,plasmaDate=? ,bp=?,disease=? where donorId=? ''', (record))
    #rows=curs.fetchall()
    con.commit()

def SearchPlasmaBlood():
    bg=input("Enter the blood group for plasma searching ")
    curs.execute('SELECT * FROM DonorPlasmaTb where bloodGroup=? ',(bg,))
    rows = curs.fetchall()
    if len(rows)==0:
        print("NO SUCH RECORD FOR  BLOOD GROUP",bg)
        print("------------------------------------------")

    for record in rows:
        print("Donor id  ",record[0])
        print("Blood group   ", record[1])
        print("Weight is ", record[2])
        print("Covid positive  ", record[3])
        print("Covid Date  ", record[4])
        print("Plasma Donate ", record[5])
        print("Plasma date ", record[6])
        print("Bp ", record[7])
        print("Disease ", record[8])

        print("------***********---------**********---------************--------")
    #[print(row) for row in curs.fetchall()]
    con.close()

if __name__=="__main__":
    while True:
        print("1. Insert many records")
        print("2. Show all Records")
        print("3. All record deletion")
        print("4. Update details")
        print("5. Search plasma by blood ")
        print("6. Exit")
        print("****************************************************")

        choice = int(input("Enter Your choice :: "))
        if choice == 1:
            InsertDonorPlasmaDetails()
        elif choice == 2:
            ShowDonorPlasmaRecords()
        elif choice == 3:
            DelAlldetails()
        elif choice == 4:
            UpdateYourDetails()
        elif choice == 5:
            SearchPlasmaBlood()
        elif choice==6:
            con.close()
            print("End of Program")
            import sys
            sys.exit(-1)