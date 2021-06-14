import webbrowser
uname=input('ENTER YOUR NAME :\n') #asking user to enter name 

upass=input('ENTER YOUR PASSWORD :\n') #asking user to enter password



credentialcount=0 
credentialcount+=1

while uname==uname and upass==upass:
    if credentialcount==3:
        print('\n YOU HAVE REACHED THE LIMIT PLEASE TRY AGAIN LATER')  #if the user enters password or name wrong three times than it will print this and exit the program
        break

    elif uname=='abhi' and upass=='xyz6969':
        webbrowser.open("file:///C:/Users/win%2010/Desktop/Website/index.html") #in brackets you can add any link or file location

        break

    elif uname!='abhi' and upass!='xyz6969':
        print('WRONG USER NAME AND PASSWORD TRY AGAIN')
       uname=input("ENTER YOUR USERNAME :\n")
        upass=input('ENTER YOUR PASSWORD :\n')
        credentialcount+=1


    elif uname=='abhi' and upass!='xyz6969':
        print('WRONG PASSWORD TRY AGAIN')
        upass=input('ENTER YOUR PASSWORD :\n')
        credentialcount+=1

    elif uname != 'abhi' and upass== 'xyz6969' :
        print('WRONG USERNAME TRY AGAIN')
        upass=input('ENTER YOUR USERNAME :\n')
        upass=input('ENTER YOUR PASSWORD :\n')
