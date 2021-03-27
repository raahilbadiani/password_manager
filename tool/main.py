# Password Manager
import random
import string
import mysql.connector
import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-p","--password",dest="Passwd",help="password for mysql")
    parser.add_option("-u","--username",dest="username",help="username for entry")
    parser.add_option("-w","--website",dest="website",help="name of website for the entry")
    parser.add_option("-i","--inputpasswd",dest="password",help="password you want to set for the account")
    parser.add_option("-c","--choice",dest="choice",help="choice\n 1: add new username,password,website\n2. add new username,website autogenerate  password\n3. search  by username\n4. search by website \n5.delete entry")
    (options,interface) = parser.parse_args()
    return options


def generate_password():
    password = ""
    for _ in range(2):
        password+=random.choice(string.digits)
    for _ in range(2):
        password+=random.choice(string.ascii_lowercase)
    for _ in range(2):
        password+=random.choice(string.ascii_uppercase)
    for _ in range(2):
        password+=random.choice(string.punctuation)
    for _ in range(6):
        password+=random.choice(string.ascii_letters)
    password = list(password)
    random.shuffle(password)
    password = ('').join(password)
    print(password)
    return password

def store_password(generate,username,website,password_u):

    # username
    # username = str(input("Your username: "))
    # # website
    # website = str(input("Website : "))

    # generate random password
    if generate == 1 :
        password_liked = False
        while(not password_liked):
            password = generate_password()
            choice = (input("Do u like the password Y/n: "))
            if choice == 'Y' or choice == 'y' :
                password_liked=True
    else :  # take pasword input from user
        # password = str(input("Password : "))   
        password = password_u
    # encrypt password
    # yet to be done

    # store account in database named pwdm
    mycursor.execute("CREATE table if not exists pwdm(website varchar(50), username varchar(50),password varchar(200))")
    mycursor.execute("insert into pwdm (website,username,password) values(%s,%s,%s)", (website,username,password))
    db.commit()

    print("Saved this entry successfully! ")


# search by username    
def search_by_username(username):
    mycursor.execute(f"select * from pwdm where username = '{username}'")
    for x in mycursor:
        print(x)
    
# search by website    
def search_by_website(website):
    mycursor.execute(f"select * from pwdm where website = '{website}'")
    for x in mycursor:
        print(x)

def delete_instance(website,username):
    mycursor.execute(f"delete from pwdm where website = '{website} and username = '{usrename}' ")
    pass

# print("Menu :")
# print("1. Add new account with password auto generate ")
# print("2. Add new  account with password of my own")
# print("3. search accounts by username")
# print("4. Search accounts by website")
# print("5. Delete instance")
# choice = int(input("Choice : "))


options = get_args()
choice = options.choice
db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd=options.Passwd,
    database="testdbpy"
)
mycursor = db.cursor()
mycursor.execute("CREATE table if not exists pwdm(website varchar(50), username varchar(50),password varchar(200))")

if choice == '1' :
    store_password(1,options.username,options.website,options.password)
elif choice == '2' :
    store_password(0,options.username,options.website,options.password)
elif choice == '3' :
    # username = str(input("username : "))
    search_by_username(options.username)
elif choice == '4' :
    # website = str(input("website : "))
    search_by_website(options.website)
elif choice == '5' :
    # website = str(input("website : "))
    # username = str(input("username : "))
    delete_instance(options.website,options.username)
