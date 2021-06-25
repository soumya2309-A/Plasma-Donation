import sqlite3
con=sqlite3.connect('PlasmaDb')
curs=con.cursor()

aadhar_No=""
def InsertDonorPersonalDetails():
    global aadhar_No
    #curs.execute(' drop table DonorpersonalTb ')
    curs.execute('''create table if not exists DonorpersonalTb(donorId integer PRIMARY KEY AUTOINCREMENT, name text,age int,city text,state text
    ,address text,addressProof text,
    addressProofImg text,mobileNo int,aadharNo int,validPhoto text,validPhotoImg text)''')


    name = input("Enter your name ")
    age = int(input("Enter the age "))
    city=input("Enter your city ")
    state=input("Enter your state ")
    address = input("Enter your address ")
    address_proof = input("Give your address proof d for driving license anf P for postcard ")
    address_proof_img = ""
    mobile_No = int(input("Enter your mobile number "))
    aadhar_No = int(input("Enter your aadhar card number "))
    valid_photo = input("Give your valid photo proof D dot driving license P for passport S for state issued ID card M for military card")

    valid_photo_img = ""

    records = (name, age,city,state, address, address_proof, address_proof_img, mobile_No, aadhar_No, valid_photo, valid_photo_img)

    curs.execute( '''insert into DonorpersonalTb(name,age,city,state,address ,addressProof ,addressProofImg ,mobileNo ,aadharNo ,validPhoto ,validPhotoImg)
     values(?,?,?,?,?,?,?,?,?,?,?)''', records)
    con.commit()

def ShowDonorpersonlRecords():
    curs.execute('SELECT * FROM DonorPersonalTb')
    rows = curs.fetchall()
    for record in rows:
        print("donor id is",record[0])
        print("name is ", record[1])
        print("age is ", record[2])
        print("city is",record[3])
        print("state is ", record[4])
        print("address is ", record[5])
        print("address_proof is ", record[6])
        print("address_proof_img is ", record[7])
        print("mobile_No is ", record[8])
        print("aadhar_No is ", record[9])
        print("valid_photo is ", record[10])
        print("valid_photo_img is ", record[11])
        print("------------*****------********---------****------------")


def DelAlldetails():
    ''' donor_id=int(input("enter the donor id "))
    curs.execute("delete from DonorPersonalTb where donorId=?",(donor_id,))
    con.commit()'''
    curs.execute("delete from DonorPersonalTb")
    con.commit()
    print("successfully deleted")

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


def UpdateYourDetails():
    donor_id = int(input("enter the donor id "))
    record=ShowDonorpersonlRecordById(donor_id)
    curs.execute('''update DonorPersonalTb set name=?,age=?,city=?,state=?
    ,address=?,addressProof=? ,
    addressProofImg=?,mobileNo=? ,aadharNo=? ,validPhoto=?,validPhotoImg=?''',record)

    con.commit()

def SearchPlasmaState():
    state1=input("Enter the state for plasma searching")
    curs.execute('SELECT * FROM DonorPersonalTb where state=?',(state1,))
    [print(row) for row in curs.fetchall()]
    print("***************************************************************")


def SearchPlasmaCityState():
    city1 = input("Enter the city+ for plasma searching")
    state2 = input("Enter the state for plasma searching")
    curs.execute('SELECT * FROM DonorPersonalTb where city=? and state=?', (city1,state2))
    [print(row) for row in curs.fetchall()]
    print("---------------------------------------------------------------")
    con.close()

if __name__=="__main__":
    while True:
        print("1. Insert many records")
        print("2. Show all Records")
        print("3. All record deletion")
        print("4. Update details")
        print("5. Search plasma by state ")
        print("6. Search plasma by city and state ")
        print("7. Exit")
        print("*********-------***********--------***********-----------************----------*************")

        choice = int(input("Enter Your choice :: "))
        if choice == 1:
            InsertDonorPersonalDetails()
        elif choice == 2:
            ShowDonorpersonlRecords()
        elif choice == 3:
            DelAlldetails()
        elif choice == 4:
            UpdateYourDetails()
        elif choice == 5:
            SearchPlasmaState()
        elif choice == 6:
            SearchPlasmaCityState()
        elif choice==7:
            con.close()
            print("End of Program")
            import sys
            sys.exit(-1)