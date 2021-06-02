import shutil
from faker import Faker
import re
fake=Faker('en_US')

# potential_contacts = ""

# existing_contacts = ""






# for i in range(100):
    
#     email=fake.email()
#     phone_number=fake.phone_number()
#     potential_contacts+=fake.paragraph()
#     potential_contacts+=" "+email+" "
#     potential_contacts+=fake.ssn()
#     potential_contacts+=fake.sentence()
#     potential_contacts+=phone_number
#     potential_contacts+=fake.paragraph()
    
    
#     if i%7 ==0:
#         potential_contacts+=" "+email+""
#         potential_contacts +fake.sentence()
        
#     if i%9 ==0:
#         potential_contacts+=phone_number
#         potential_contacts+=fake.paragraph()
        
#     if i%5 ==0:
#         existing_contacts+=email+"\n"
#         existing_contacts+=phone_number +"\n"
        
            
        
#     potential_contacts+="\n"
    
    
# with open("potential_contacts.txt","w+") as f:
#     f.write(potential_contacts)
    
# shutil.copy('potential_contacts.txt', '/home/raneem/codefellows/401/labs/Automation/assets/potential_contacts.txt')


# Feature Tasks and Requirements
# klajdso@hdsfkj.ksajd

# [a-zA-z0-9.-]\w+@[a-zA-z-]\w+[-_]\w*.

# craigthomas@hamilton-rodriguez.com
# Given a document potential-contacts, find and collect all email addresses and phone numbers.

email_pattern=re.compile(r'\w*@\w*(-)?(\w)*\.[a-zA-Z]*(-)?(\w)*')

# 123-456-7890
# 206-678-9012
num='''
luvhbj234-843-8901
cygvkhjb lm,
123-456-7890sf ghjk
206-  -9012
521 879 3254
'''

phone_pattern=re.compile(r'(\d{3}).(\d{3}).(\d{4})')
phone_matches=phone_pattern.finditer(num)
for i in phone_matches:
    print(i)




with open('assets/potential_contacts.txt','r') as f:
    contacts=f.read()
email_matches=email_pattern.finditer(contacts)
phone_matches=phone_pattern.finditer(contacts)


def email_fun():
    emai_list=[]  
    phone_list=[]  
    for match in email_matches:
            emai_list.append(match)
    #         print(match)
    # print(len(emai_list))
    
    for p_match in phone_matches:
        print(p_match)
        phone_list.append(p_match)
    print(len(phone_list))
        

email_fun()




# Phone numbers may be in various formats.

# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.

# phone numbers with missing area code should presume 206


# phone numbers should be stored in xxx-yyy-zzzz format.

# Once emails and phone numbers are found they should be stored in two separate documents.
# The information should be sorted in ascending order.
# Duplicate entries are not allowed.