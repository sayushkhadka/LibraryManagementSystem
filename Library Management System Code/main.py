#importing the functios.py to main program
import functions

book_record = functions.Library_list()
#callig book_record_display function
functions.book_record_display(book_record)



book_name = "" #book_name to empty string
book_total_cost = 0 #book_total_cost set to 0
enter_number = 0 #enter_number set to 0

valid_y = True 

while enter_number != 4:
    #Options provided to the user to choose carry out their work
    
    print("\nSelect an option:")
    print("\nTo display the records : ENTER 1")
    print("To borrow a book       : ENTER 2 ")
    print("To return a book       : ENTER 3")
    print("To exit                : ENTER 4")
    
    while valid_y == True:

        
        try:
            enter_number = int(input("\nMake a choice(1,2,3,4) :  ")) 
            print()

        except:
            print("\nERROR!!!Only numbers accepted.") #must choose from (1-4) (no string)
            

        #to display the records
        if(enter_number == 1):
            
            functions.book_record_display(book_record) 
                
        #to borrow the book
        elif(enter_number == 2):
            
            name = input("\nEnter the name(Customer name): ")
            cost_book,book_name = functions.book_borrow_continued(book_record,functions.book_record_display,book_total_cost,book_name)
            functions.book_bill(cost_book,book_name,name)

        #to return the book      
        elif(enter_number == 3):
            
            name = input("\nEnter the name(Customer name): ")
            functions.book_return(book_record, name, functions.book_record_display)

        #to exit the program      
        elif(enter_number == 4):
            print("\nYou have chosen to exit the program.\nThank you!!!")
            break
              
        else:
            print("ERROR!!!Please choose only form (1-4).") #must choose from (1-4) (no stirng)
                
        
            
