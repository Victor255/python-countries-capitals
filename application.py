"""COUNTRIES AND CAPITALS"""

# coding=utf-8
# coding:utf8
# -*- coding: 850 -*-

import os
import smtplib, getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class CountriesAndCapitals(object):
    """COUNTRIES AND CAPITALS"""

    def __init__(self):
        self.country = {}

    def addcountry(self):
        """ADD THE COUNTRIES"""
        os.system("clear")
        constant = True
        while constant == True:
            countries = raw_input("Insert a country: ")
            countries = countries.title()
            try:
                text = countries.decode("utf-8") #turn into a string
                var = True
                for i in text:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if var == True: #if variable is true
                            var = True
                    else:
                        var = False #else, make it false
                if var == False: #if variable is false
                    print "Invalid Country"
                    constant = True
                    #convert the original variable in true so it can repeat itself
                elif len(countries) <= 2:
                    print "Invalid Country"
                    constant = True #if not, kill this part and go on
                else:
                    constant = False
                    self.addcapital(countries)
            except ValueError:
                print "Invalid Country" #just verifies, any possible mistake
                constant = False

    def addcapital(self, countries):
        """ADD THE CAPITALS"""
        capit = True
        while capit == True:
            capital = raw_input("Insert capital: ") #asks to insert the item
            capital = capital.title()
            try:
                text = capital.decode("utf-8") #turn into a string
                var = True #another variable to verify
                for i in text:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if var == True: #if variable is true
                            var = True #make it true
                    else:
                        var = False #else, make it false
                if var == False: #if variable is false
                    print "Invalid Capital"
                    capit = True
                    #convert the original variable in true so it can repeat itself
                elif len(capital) <= 2:
                    print "Invalid Capital"
                    capit = True
                else:
                    capit = False
            except ValueError:
                print "Invalid Capital"
                capit = False
        print "YOU HAVE ADDED CORRECTLY"
        self.country[countries] = capital
        self.anothercountry()

    def anothercountry(self):
        """ASK IF THE USER WANTS TO ADD ANOTHR COUNTRY AND CAPITAL"""
        diferents = True
        while diferents == True:
            others = raw_input("\nDo you want to add another country? yes or no: ")
            others = others.lower()
            if others == "yes" or others == "y":
                self.addcountry()
            elif others == "no" or others == "n":
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
        username = "tagbar95@gmail.com"  ##The username
        password = getpass.getpass("Pasword: ") #Not showing the password
        adress = "lgarcia@cognits.co" #the addressee of the email
        body = "Countries and Capitals: " #this shows the subject in the email

        # body of email
        for key, item in self.country.items():
            body += """
            """ + str(key) + " - " + str(item)

        # Forming the body of email
        msg = MIMEMultipart()
        msg['From'] = username #This saves the mail of the sender
        msg['To'] = adress #This saves the mail of the receiver
        msg['Subject'] = "Countries and capitals" #This saves the subject
        msg.attach(MIMEText(body, 'plain')) #This saves the message

        # This try controls if the email was sent
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, adress, text)
            server.quit()
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

ALL = CountriesAndCapitals()
ALL.menus()
