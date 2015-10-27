"""COUNTRIES AND CAPITALS"""

# coding=utf-8
# coding:utf8
# -*- coding: 850 -*-

import os
import smtplib, getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class countriesandcapitals(object):
    """COUNTRIES AND CAPITALS"""

    def __init__(self):
        self.country = {}

    def addcountry(self):
        """ADD COUNTRIES AND CAPITALS"""
        os.system("clear")
        CONSTANT = True
        while CONSTANT == True:
            COUNTRIES = raw_input("Insert a country: ")
            COUNTRIES = COUNTRIES.title()
            try:
                TEXT = COUNTRIES.decode("utf-8") #turn into a string
                VAR = True
                for i in TEXT:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if VAR == True: #if variable is true
                            VAR = True
                    else:
                        VAR = False #else, make it false
                if VAR == False: #if variable is false
                    print "Invalid Country"
                    CONSTANT = True
                    #convert the original variable in true so it can repeat itself
                elif len(COUNTRIES) <= 2:
                    print "Invalid Country"
                    CONSTANT = True #if not, kill this part and go on
                else:
                    CONSTANT = False

            except ValueError:
                print "Invalid Country" #just verifies, any possible mistake
                CONSTANT = False
        CAPIT = True
        while CAPIT == True:
            CAPITAL = raw_input("Insert capital: ") #asks to insert the item
            CAPITAL = CAPITAL.title()
            try:
                TEXT = CAPITAL.decode("utf-8") #turn into a string
                VAR = True #another variable to verify
                for i in TEXT:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if VAR == True: #if variable is true
                            VAR = True #make it true
                    else:
                        VAR = False #else, make it false
                if VAR == False: #if variable is false
                    print "Invalid Capital"
                    CAPIT = True
                    #convert the original variable in true so it can repeat itself
                elif len(CAPITAL) <= 2:
                    print "Invalid Capital"
                    CAPIT = True
                else:
                    CAPIT = False
            except ValueError:
                print "Invalid Capital"
                CAPIT = False
        print "YOU HAVE ADDED CORRECTLY"
        self.country[COUNTRIES] = CAPITAL
        self.anothercountry()

    def anothercountry(self):
        """ASK IF THE USER WANTS TO ADD ANOTHR COUNTRY AND CAPITAL"""
        DIFERENTS = True
        while DIFERENTS == True:
            OTHERS = raw_input("\nDo you want to add another country? yes or no: ")
            OTHERS = OTHERS.lower()
            if OTHERS == "yes" or OTHERS == "y":
                self.addcountry()
            elif OTHERS == "no" or OTHERS == "n":
                os.system("clear")
                self.menus()
            else:
                print "Insert only yes or no"

    def countries(self):
        """SHOWS THE LIST OF COUNTRIES"""
        os.system("clear")
        print "COUNTRIES"
        for i in self.country: #lists the countries
            print "-", i #prints a star and the countries
        raw_input("\nPress enter to continue")
        os.system("clear")
        self.menus()

    def capitals(self):
        """SHOWS THE LIST OF CAPITALS"""
        os.system("clear")
        print "CAPITALS"
        for i in self.country: #list of capitals
            print "-", self.country[i] #prints a star and the capitals
        raw_input("\nPress enter to continue")
        os.system("clear")
        self.menus()

    def all(self):
        """SHOWS THE LIST OF COUNTRIES AND CAPITALS"""
        os.system("clear")
        print "COUNTRIES AND CAPITALS"
        for i in self.country: #list of capitals
            print "\n-", i, "-", self.country[i] #prints a dash and the capitals
        raw_input("\nPress enter to continue")
        os.system("clear")
        self.menus()

    def allordered(self):
        """SHOWS THE LIST OF COUNTRIES AND CAPITALS ORDERED"""
        os.system("clear")
        print "List of all Countries with Capitals in Order"
        for key, value in sorted(self.country.iteritems(), key=lambda (k, v): (v, k)):
            print "%s - %s" % (key, value) #internet way to sort a dic by its valu
        raw_input("\nPress enter to continue")
        os.system("clear")
        self.menus()

    def instructions(self):
        """SHOWS THE INSTRUCTIONS"""
        os.system("clear")
        print "______________________________________________________________________________"
        print "                         Choose an Option                                     |"
        print """1- If you want to add a country and capital, insert "COUNTRY"                 |"""
        print """2- If you want the list of countries added, insert "COUNTRIES"                |"""
        print """3- If you want the list of capitals added, insert "CAPITALS"                  |"""
        print """4- If you want both countries and capitals added, insert "ALL"                |"""
        print """5- If you want both alphabetically ordered, insert "AllORDERED"               |"""
        print """6- If you want to send list of countries and capitals to lgarcia@cognits.co,
    insert the word "SENDMAIL"                                                |"""
        print """7- If you want to close the program, insert "EXIT"                            |"""
        print "______________________________________________________________________________|"

    def sendmail(self):
        """SEND THE EMAIL"""
        USERNAME = "tagbar95@gmail.com"
        PASSWORD = getpass.getpass("Pasword: ")
        ADRESS = "lgarcia@cognits.co"
        BODY = "Countries and Capitals: "

        # Body of email
        for key, item in self.country.items():
            BODY += """
            """ + str(key) + " - " + str(item)

        # Forming the body of email
        MSG = MIMEMultipart()
        MSG['From'] = USERNAME
        MSG['To'] = ADRESS
        MSG['Subject'] = "Countries and capitals"
        MSG.attach(MIMEText(BODY, 'plain'))

        # This try controls if the email was sent
        try:
            SERVER = smtplib.SMTP("smtp.gmail.com", 587)
            SERVER.starttls()
            SERVER.login(USERNAME, PASSWORD)
            text = MSG.as_string()
            SERVER.sendmail(USERNAME, ADRESS, text)
            SERVER.quit()
            print "Email sent correctly"
            raw_input("\nPress enter to continue...")
            self.menus()
        except ValueError:
            print "Error ocurred"
            self.menus()

    def menus(self):
        """MENU OF OPTIONS"""
        self.instructions()
        menu = True
        while menu == True:
            option = raw_input("\nInsert here the Option:  ")
            option = option.lower()
            if option == "country" or option == "1":
                self.addcountry()
                menu = False
            elif option == "countries" or option == "2":
                self.countries()
                menu = False
            elif option == "capitals" or option == "3":
                self.capitals()
                menu = False
            elif option == "all" or option == "4":
                self.all()
                menu = False
            elif option == "allordered" or option == "all ordered" or option == "5":
                self.allordered()
                menu = False
            elif option == "sendmail" or option == "send mail" or option == "6":
                self.sendmail()
                menu = False
            elif option == "exit" or option == "7":
                print "THANK AND BYE"
                exit()
            else:
                print "Please insert a valid Option"
                menu = True
                os.system("clear")
                self.instructions()
                print "Please insert a valid Option"

ALL = countriesandcapitals()
ALL.menus()
