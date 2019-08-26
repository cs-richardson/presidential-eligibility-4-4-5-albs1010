#Albert
'''
this function asks for age, citizen, and residency. If the age is atleast 35,
the person is an American citizen, and years of residency is atleast 14, the
person is elgible to run for president. If these requirements are not met, there
would be text indicating what the person is missing.
'''

def president(name=None):
    
    age = int(input("Age: "))
    citizen = input("Born in the U.S.? (Yes/No): ")
    residency = int(input("Years of Residency: "))
    
    if age >= 35 and citizen == "Yes" and residency >= 14:
        print("You are eligible to run for president!")
        
    else:
        print("You are not eligible to run for president.")
        
    if age < 35:
        print("You are too young.")
        
    if citizen == "No":
        print("You must be born in the U.S. to run for president.")
        
    if residency < 14:
        print("You have not been a resident for long enough.")
        
president()
