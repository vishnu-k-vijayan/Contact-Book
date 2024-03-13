print()
a="            ************ CONTACT BOOK ***********"
print(a)

contactdict={}
#print(contactdict)

#########################################################

while True: # its for repeating many times 
    print()
    print("1.ADD CONTACT")
    print("2.VIEW CONTACT")
    print("3.EDIT CONTACT")
    print("4.DELETE CONTACT")
    print("5.EXIT")

#########################################################
    print()  # new line;
    try:
        n=int(input("<<<<<<<<<< ENTER YOUR CHOICE : "))    
        print()
    except:
        print()
        print('SOMTHING WENT WRONG') 
        continue   
    
# ADD CONTACT       
#   print(n)
    if(n==1):
        print("                **** ADD CONTACT ****")
        print()
        
        name=input("ENTER  NAME : ") # inputing a name in variable
        
        if(name in contactdict):
            print()
            print('********* THIS NAME ALLREADY EXISTED ***********')
            
        else:
            num=0 #/False
            while(num==0): #/ == False
                try:
                    number=int(input("ENTER NUMBER : ")) # input number in a variable
                except:
                    print()
                    print('SOMTHING WENT WRONG')
                else:
                    num=1  #/ False
            contactdict[name]=number #*
        
                
# VIEW CONTACT
    if(n==2):
        print('               ******* VIEW CONTACT ********')
        print()
        for y,z in contactdict.items():     # print the dictionary
            print('.',y,'   - ',z)         # x , y access the elements in the dict
        
# EDIT CONTACT           
    if(n==3):
        print('             ******* EDIT CONTACT*******')
        print()
                                # dict edit for update or item fun
        
        a="1.CHANGE NAME"
        print(a)
        b="2.CHANGE NUMBER"
        print(b)
        print()
        num=0
        while(num==0):
            try:
                n1=int(input("<<<<< ENTER YOUR CHOICE : "))
            except:
                print()
                print('SOMTHING WENT WRONG')
            else:
                num=1        
        if(n1==1):
            
            c=input('WHICH NAME YOU WANT TO CHANGE:')
            
            print()
            if(c in contactdict):
                print()
                x=contactdict[c]
                
                del contactdict[c] 
                name_1=input("CHNAGE  NAME : ")
                contactdict[name_1]=x
                
            else:
                print()
                print('This name not exist in contact book')
                
        else:
            if(n1==2):                
                c1=input('WHICH NAME NUMBER YOU WANT TO CHANGE:')
                if(c1 in contactdict):
                    num=0
                    while(num==0):
                        try:
                            number_1=int(input("CHANGE NUMBER : "))
                        except:
                            print()
                            print('SOMTHING WENT WRONG')
                        else:
                            num=1    
                    contactdict[c1]=number_1    
                    
                else:
                    print()
                    print('********** THIS NAME NOT EXISTED ***********')
                    
            else:
                
                print('*******WRONG SELECTION*******')
                
                
# DELETE CONTACT        
    if(n==4):
        print("             ****** DELETE CONTACT *******")
        print()
        c2=input('WHICH CONTACT NAME  YOU WANT TO DELETE:')
       
        print()
        if(c2 in contactdict):
            del contactdict[c2]  
            print()                       
            print("------DELETE SUCCESFULLY-----")
            
        else:
            print()
            print("********NAME NOT EXISTED******")
            
# EXIT CONTACT       
    if(n==5):
        print('              ****** EXIT ******')
        print(exit()) # EXIT for the pgm
        
    if(n>=6):
        print("               **** YOUR WRONG SELECTION ****")


