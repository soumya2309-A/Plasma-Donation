import sqlite3
import DonorPlasmaFunctions
import DonorPerByUsingFunctions
from DonorPerByUsingFunctions import *
from DonorPlasmaFunctions import *
#import pandas as pd
con=sqlite3.connect('PlasmaDb')
curs=con.cursor()



def ShowDetails():
    #curs.execute('SELECT donorId FROM DonorPlasmaTb')
    curs.execute('SELECT donorId FROM DonorpersonalTb')
    rows = curs.fetchall()
    print("Donor ID's are:: ",*rows)

    curs.execute('SELECT donorId FROM DonorPlasmaTb')
    rows = curs.fetchall()
    print("Donor id ", *rows)

    DonorId = input("Enter the donor id")
    curs.execute('''SELECT DonorpersonalTb.name,DonorpersonalTb.age,DonorpersonalTb.city,DonorPlasmaTb.bloodgroup 
    FROM DonorpersonalTb,DonorPlasmaTb where DonorpersonalTb.donorId=? and  DonorPlasmaTb.donorId=?''',(DonorId,DonorId) )

    row=curs.fetchone()
    print(row)

#ShowDetails()

def InsertDonor():
    #global aadhar_No
    InsertDonorPersonalDetails()
    print(aadhar_No)
    curs.execute('SELECT donorId FROM DonorpersonalTb where aadharNo=?',(DonorPerByUsingFunctions.aadhar_No,))
    row = curs.fetchone()
    print(*row)
    print("Donor id ", row[0])

    InsertDonorPlasmaDetails(row[0])

#InsertDonor()


def ShowAllDetails():

    curs.execute('SELECT donorId FROM DonorpersonalTb')
    rows = curs.fetchall()
    print("Donor id ",*rows)
    print('*===========*==============*=========*========*')

    DonorId = input("Enter the donor id ")


    curs.execute('''SELECT DonorpersonalTb.donorId,DonorpersonalTb.name,DonorpersonalTb.age,DonorpersonalTb.city,DonorpersonalTb.state,DonorpersonalTb.address,
    DonorpersonalTb.addressProof,DonorpersonalTb.addressProofImg,DonorpersonalTb.mobileNo,DonorpersonalTb.aadharNo,DonorpersonalTb.validPhoto,DonorpersonalTb.validPhotoImg,
    DonorPlasmaTb.bloodgroup,DonorPlasmaTb.weight,DonorPlasmaTb.covidpositive,DonorPlasmaTb.coviddate,DonorPlasmaTb.plasmadonate,DonorPlasmaTb.plasmadate,DonorPlasmaTb.bp,
    DonorPlasmaTb.disease FROM DonorpersonalTb,DonorPlasmaTb where DonorpersonalTb.donorId=? and  DonorPlasmaTb.donorId=?''',(DonorId,DonorId) )

    rows = curs.fetchall()
    #print(row)
    for row in rows:
        print("Donor id is: ",row[0])
        print("Name is: ", row[1])
        print("Age is: ", row[2])
        print("City is: ",row[3])
        print("State is: ", row[4])
        print("Address is: ", row[5])
        print("Address_proof is: ", row[6])
        print("Address_proof_img is: ", row[7])
        print("Mobile_No is: ", row[8])
        print("Vadhar_No is: ", row[9])
        print("Valid_photo is ", row[10])
        print("Valid_photo_img is: ", row[11])
        print("Blood group is: ", row[12])
        print("Weight is: ", row[13])
        print("Covid positive: ", row[14])
        print("Covid date: ", row[15])
        print("Plasma donate: ", row[16])
        print("Plasma donate date: ", row[17])
        print("Blood pressure is: ", row[18])
        print("Diseases are: ", row[19])





    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

#ShowAllDetails()


def ShowAllDetailsByCity():

    curs.execute('SELECT distinct city FROM DonorpersonalTb')
    rows = curs.fetchall()
    print("City ",*rows)
    '''cityDf = pd.DataFrame(rows, index=[1,2, 3,4], columns=['Cities'])
    print(cityDf)'''
    print('*===========*==============*=========*========*')



    city = input("Enter city  name ")

    curs.execute('''SELECT donorId FROM DonorpersonalTb where city=? ''', (city,))
    rowsId=curs.fetchall()

    for row in rowsId:
        donor_id=row[0]
        curs.execute('''SELECT DonorpersonalTb.name,DonorpersonalTb.age,DonorpersonalTb.address,
        DonorpersonalTb.mobileNo,DonorPlasmaTb.bloodgroup FROM DonorpersonalTb,DonorPlasmaTb where DonorpersonalTb.donorId=? and
        DonorPlasmaTb.donorId=?''',(donor_id,donor_id))

        rows=curs.fetchall()
        for row in rows:


            print("Name is: ", row[0])
            print("Age is: ", row[1])
            print("Address is: ",row[2])
            print("Mobile number is: ", row[3])
            print("Blood Group is: ", row[4])
            print("------------------------------")
        #print(*rows)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
#ShowAllDetailsByCity()

def ShowDetailsByState():

    curs.execute('SELECT distinct state FROM DonorpersonalTb')
    rows=curs.fetchall()

    print("State",*rows)
    '''stateDf=pd.DataFrame(rows,index=[1,2,3],columns=['States'])
    print(stateDf)'''
    print('*===========*==============*=========*========*')


    state=input("Enter the state name ")

    curs.execute('''SELECT donorId FROM DonorpersonalTb where state=?''',(state,))
    rowsId=curs.fetchall()

    for row in rowsId:
        donor_id=row[0]
        curs.execute('''SELECT DonorpersonalTb.name,DonorpersonalTb.age,DonorpersonalTb.address,DonorpersonalTb.city,
        DonorpersonalTb.mobileNo,DonorPlasmaTb.bloodgroup FROM DonorpersonalTb,DonorPlasmaTb where DonorpersonalTb.donorId=? and
        DonorPlasmaTb.donorId=?''',(donor_id,donor_id) )


        rows = curs.fetchall()

        for row in rows:
            print("Name is: ", row[0])
            print("Age is: ", row[1])
            print("Address is: ", row[2])
            print("City is: ", row[3])
            print("Mobile number is: ", row[4])
            print("Blood Group is: ", row[5])
            print("------------------------------")

        #print(*rows)
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
#ShowDetailsByState()

def ShowDetailsByBG():

    curs.execute('SELECT distinct bloodgroup FROM DonorPlasmaTb')
    rows=curs.fetchall()
    print("bloodGroup",*rows)
    ''' BgDf = pd.DataFrame(rows, index=[1,2,3], columns=['BG'])
    print(BgDf)'''
    print('*===========*==============*=========*========*')


    blood_group=input("Enter the blood group ")

    curs.execute('''SELECT donorId FROM DonorPlasmaTb where  bloodGroup=?''', (blood_group,))
    rowsId = curs.fetchall()

    for row in rowsId:
        donor_id=row[0]

        curs.execute('''SELECT name,age,address,city,mobileNo FROM DonorpersonalTb where donorId=? ''',(donor_id,) )

        rows = curs.fetchall()


        #BGDf = pd.DataFrame(rows, index=[1,2], columns=['Name', 'Age', 'Address', 'City', 'Mobile number'])
        #print(BGDf)

        for row in rows:

                print("Name is: ", row[0])
                print("Age is: ", row[1])
                print("Address is: ", row[2])
                print("City is: ", row[3])
                print("Mobile number is: ", row[4])
                print("------------------------------")
        #print(*rows)
    print("---------------------------------------------------------------------------------------------------------------------------------------")

#ShowDetailsByBG()

def DelAlldetails():

    curs.execute("delete from DonorPlasmaTb")
    con.commit()
    curs.execute("delete from DonorpersonalTb")
    con.commit()
    print("successfully deleted")

#DelAlldetails()

def DelRecordsById():
    donor_id = int(input("enter the donor id "))
    curs.execute("delete from DonorPlasmaTb where donorId=?", (donor_id,))
    con.commit()

    curs.execute("delete from DonorpersonalTb where donorId=?", (donor_id,))
    con.commit()
    print("successfully deleted")

#DelRecordsById()
def ShowDonorpersonlRecordById(id):
    curs.execute('SELECT * FROM DonorPersonalTb where donorId=?',(id,))
    row = curs.fetchone()
    name=row[1]
    age=row[2]
    city=row[3]
    state=row[4]
    address=row[5]
    address_proof=row[6]
    address_proof_img= row[7]
    mobileNo=row[8]
    aadharNum=row[9]
    valid_photo=row[10]
    valid_photo_img=row[11]

    print("name is ", name)
    print("age is ", age)
    print("city is",city)
    print("state is ", state)
    print("address is ", address)
    print("address_proof is ",address_proof )
    print("address_proof_img is ", address_proof_img)
    print("mobile_No is ",mobileNo )
    print("aadhar_No is ", aadharNum)
    print("valid_photo is ",valid_photo )
    print("valid_photo_img is ",valid_photo_img )
    print("------------*****------********---------****------------")

    ans=input("change in name y/n ")
    if ans[0]=='y' or ans[0]=='Y':
        name=input("Enter name :: ")

    ans = input("change in age y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        age = int(input("Enter age :: "))

    ans = input("change in city y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        city = input("Enter city :: ")

    ans = input("change in  state y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        state = input("Enter state :: ")

    ans = input("change in address y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        address = input("Enter address :: ")

    ans = input("change in addressproof y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        address_proof = input("Enter address_proof :: ")

    ans = input("change in address Proof Img y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        address_proof_img = input("Enter address_proof_img:: ")

    ans = input("change in Mobile Number y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        mobileNo = int(input("Enter mobile_No:: "))

    ans = input("change in Aadhar number y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        aadharNum = int(input("Enter aadhar_No:: "))

    ans = input("change in Valid Photo y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        valid_photo = input("Enter valid_photo:: ")

    ans = input("change in valid photo img y/n ")
    if ans[0] == 'y' or ans[0] == 'Y':
        valid_photo_img = input("Enter valid_photo_img:: ")

    record=(name,age,city,state,address,address_proof,address_proof_img,mobileNo,aadharNum,valid_photo,valid_photo_img)
    return record

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
    record1=ShowDonorpersonlRecordById(donor_id)
    record2=ShowDonorPlasmaRecordsById(donor_id)




    curs.execute('''update DonorPersonalTb set name=?,age=?,city=?,state=?,address=?,addressProof=? ,addressProofImg=?,mobileNo=? 
    ,aadharNo=? ,validPhoto=?,validPhotoImg=?''', record1)
    con.commit()
    curs.execute('''update DonorPlasmaTb set bloodGroup=? ,weight=? ,covidPositive=?,covidDate=? 
    ,plasmaDonate=? ,plasmaDate=? ,bp=?,disease=? where donorId=? ''', (record2))
    con.commit()



if __name__=="__main__":
    while True:
        print("1. Insert records::  ")
        print("2. Show record by ID's:: ")
        print("3. Show record by city:: ")
        print("4. Show record by state:: ")
        print("5. Show record by blood group:: ")
        print("6. Update records:: ")
        print("7. Delete records by Id:: ")
        print("8. Delete All details:: ")
        print("****************************************************")

        choice = int(input("Enter Your choice :: "))
        if choice == 1:
            InsertDonor()
        elif choice == 2:
            ShowAllDetails()
        elif choice == 3:
            ShowAllDetailsByCity()
        elif choice == 4:
            ShowDetailsByState()
        elif choice == 5:
            ShowDetailsByBG()
        elif choice == 6:
            UpdateYourDetails()
        elif choice == 7:
            DelRecordsById()
        elif choice == 8:
            DelAlldetails()
        elif choice==10:
            con.close()
            print("End of Program")
            import sys
            sys.exit(-1)