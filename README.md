## Password Manager 

# Varities  :

1.  normal python code : 
    - runs in terminal and machines must have mysql installed and added to environment variables.
    - runs locally
2. parser version of normal code :
    - runs in terminal as proper terminal command with flags such as --help or -h to get help about tool and other flags to decide the action to be performed by the command
    - needs  mysql installed locally and added to path
3. webhosted :
    - data to be saved on cloud server
    - no need to have mysql installed locally
4. chrome/firefox plugin :
    - easy to use
    - automtically pastes password in password input on webpages with some shortcut key combination

# current status :
    5 options available in 2 versions(normal code, parser version (this behaves like terminal command. to get more info type python main.py --help))
    1. save a new entry with username,website,password
    2. save a new entry with username,website,auto generated strong password
    3. query to get all passwords by username
    4. query to get all passwords by website
    5. remove some entry by giving combination of username,website


# upcoming goals :
    1. encrypt the password before saving it in database and decrypt it with some master password
    2. do something to directly copy the queried password to clipboard (maybe use something like xclip or something else)
    3. convert the normal python code to make it a GUI application.
    4. create users (for online version) so multiple people can use this tool in same device and decide whether each user will have separate table in database or single table would be better
    5. try to improve auto password generation to make password more strong also try to run several attacks on password using rockyou.txt list of passwords to avoid commonly used passwords that maybe generated randomly
    6. make the interface better and more user friendly 

