#to import date and time
import datetime


#function list split
def Library_list():
    file = open("book_list.txt","r") #open and r=mode for file
    list_one = []   #empty list
    list_two = []   #empty list
    for line in file:
        line = line.replace("\n","")
        list_one.append(line.split(",")) #to split string
    for i in range(len(list_one)):
        for j in range(len(list_one[i])):
            list_two.append(list_one[i][j])
    return list_two

#title
print("\n\t\t\t\tLibrary Management System\n")  

print("Learning never stops.")

#to display the records in the Library Management System
def book_record_display(book_record):  
    print("-------------------------------------------------------------------------------------------\nBook ID  Book Name                 Author                      Book Price       Quantity\n-------------------------------------------------------------------------------------------")
    print(" ",book_record[0],"    ",book_record[1],"           ",book_record[2],"              ",book_record[3],"             ",book_record[4])
    print(" ",book_record[5],"    ",book_record[6],"         ",book_record[7],"             ",book_record[8],"            ",book_record[9])
    print(" ",book_record[10],"    ",book_record[11],"                  ",book_record[12],"        ",book_record[13],"            ",book_record[14])
    print(" ",book_record[15],"    ",book_record[16],"               ",book_record[17],"              ",book_record[18],"            ",book_record[19])
    print(" ",book_record[20],"    ",book_record[21],"              ",book_record[22],"                ",book_record[23],"             ",book_record[24])
    print(" ",book_record[25],"    ",book_record[26],"           ",book_record[27],"               ",book_record[28],"            ",book_record[29])
    print(" ",book_record[30],"    ",book_record[31],"            ",book_record[32],"            ",book_record[33],"             ",book_record[34])
    print(" ",book_record[35],"    ",book_record[36],"          ",book_record[37],"              ",book_record[38],"            ",book_record[39])
    print(" ",book_record[40],"    ",book_record[41],"         ",book_record[42],"           ",book_record[43],"            ",book_record[44])
    print(" ",book_record[45],"   ",book_record[46],"             ",book_record[47],"              ",book_record[48],"            ",book_record[49])


#for available books
def book_available(book_record,book_quantity,book_ID):
    book_quantity1 = book_record[4]
    book_quantity2 = book_record[9]
    book_quantity3 = book_record[14]
    book_quantity4 = book_record[19]
    book_quantity5 = book_record[24]
    book_quantity6 = book_record[29]
    book_quantity7 = book_record[34]
    book_quantity8 = book_record[39]
    book_quantity9 = book_record[44]
    book_quantity10 = book_record[49]

    
    file = open("book_list.txt","w") #open file in write mode

    
    if book_ID == 1:
        book_quantity1 = int(book_record[4])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+str(book_quantity1)+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 2:
        book_quantity2 = int(book_record[9])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+str(book_quantity2)+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 3:
        book_quantity3 = int(book_record[14])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+str(book_quantity3)+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
        
    elif book_ID == 4:
        book_quantity4 = int(book_record[19])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+str(book_quantity4)+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
        
    elif book_ID == 5:
        book_quantity5 = int(book_record[24])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+str(book_quantity5)+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 6:
        book_quantity6 = int(book_record[29])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+str(book_quantity6)+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 7:
        book_quantity7 = int(book_record[34])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+str(book_quantity7)+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 8:
        book_quantity8 = int(book_record[39])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+str(book_quantity8)+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 9:
        book_quantity9 = int(book_record[44])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+str(book_quantity9)+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 10:
        book_quantity10 = int(book_record[49])-1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+str(book_quantity10)+"")
        
         
    file.close()
    
    
    book_quantity_remaining = book_quantity - 1
    for i in range(len(book_record)):
        for j in range(len(book_record[i])):
            if book_ID == 1:
                book_record[4] = str(book_quantity_remaining)
                
            elif book_ID == 2:
                book_record[9] = str(book_quantity_remaining)
                
            elif book_ID == 3:
                book_record[14] = str(book_quantity_remaining)
                
            elif book_ID == 4:
                book_record[19] = str(book_quantity_remaining)
                
            elif book_ID == 5:
                book_record[24] = str(book_quantity_remaining)
                
            elif book_ID == 6:
                book_record[29] = str(book_quantity_remaining)

            elif book_ID == 7:
                book_record[34] = str(book_quantity_remaining)

            elif book_ID == 8:
                book_record[39] = str(book_quantity_remaining)

            elif book_ID == 9:
                book_record[44] = str(book_quantity_remaining)

            elif book_ID == 10:
                book_record[49] = str(book_quantity_remaining)


#number of books(book count)
def book_counts(book_record,book_ID):
    book_name = "" #book name to empty string
    
    if book_ID == 1:
        book_name = book_record[1]
        
    elif book_ID == 2:
        book_name = book_record[6]
        
    elif book_ID == 3:
        book_name = book_record[11]
        
    elif book_ID == 4:
        book_name = book_record[16]
        
    elif book_ID == 5:
        book_name = book_record[21]
        
    elif book_ID == 6:
        book_name = book_record[26]

    elif book_ID == 7:
        book_name = book_record[31]

    elif book_ID == 8:
        book_name = book_record[36]

    elif book_ID == 9:
        book_name = book_record[41]

    elif book_ID == 10:
        book_name = book_record[46]
        
    return book_name

    

#for book price
def book_price(book_record,book_ID):
    
    if book_ID == 1:
        book_price = book_record[3]
        book_price = book_price.replace("$","")
        
    elif book_ID == 2:
        book_price = book_record[8]
        book_price = book_price.replace("$","")
        
    elif book_ID == 3:
        book_price = book_record[13]
        book_price = book_price.replace("$","")
        
    elif book_ID == 4:
        book_price = book_record[18]
        book_price = book_price.replace("$","")
        
    elif book_ID == 5:
        book_price = book_record[23]
        book_price = book_price.replace("$","")
        
    elif book_ID == 6:
        book_price = book_record[28]
        book_price = book_price.replace("$","")

    elif book_ID == 7:
        book_price = book_record[33]
        book_price = book_price.replace("$","")

    elif book_ID == 8:
        book_price = book_record[38]
        book_price = book_price.replace("$","")

    elif book_ID == 9:
        book_price = book_record[43]
        book_price = book_price.replace("$","")

    elif book_ID == 10:
        book_price = book_record[48]
        book_price = book_price.replace("$","")
        
    return book_price



#borrow book
def book_borrow(book_record):
    price_of_book = 0
    book_Name = ""
    flag = True
    valid_y = True
    valid_n = True
    
    while valid_y == True:

        #try,except
        try:
            book_ID = int(input("\nEnter the book ID: "))
            break
        
        except:
            print("Enter a valid ID from the record.")
            
    while flag == True:
        if book_ID == 1:
            book_quantity = int(book_record[4])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                    try:
                        book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                        break
                    except:
                        print("Enter a valid ID from the record.")
                        
        elif book_ID == 2:
            book_quantity = int(book_record[9])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")
                
                
        elif book_ID == 3:
            book_quantity = int(book_record[14])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break

            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")
                            
        elif book_ID == 4:
            book_quantity = int(book_record[19])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")
                            
                            
        elif book_ID == 5:
            book_quantity = int(book_record[24])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")
                            
        elif book_ID == 6:
            book_quantity = int(book_record[29])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")
                            
        elif book_ID == 7:
            book_quantity = int(book_record[34])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")

        elif book_ID == 8:
            book_quantity = int(book_record[39])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")

        elif book_ID == 9:
            book_quantity = int(book_record[44])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")

        elif book_ID == 10:
            book_quantity = int(book_record[49])
            if book_quantity > 0:
                book_record_displayAvailable()
                book_available(book_record,book_quantity,book_ID)
                book_record_display(book_record)
                price_of_book = book_price(book_record,book_ID)
                book_Name = book_counts(book_record,book_ID)
                break
            
            else:
                while valid_n == True:
                        try:
                            book_ID = int(input("\nOut of stock.Please enter the book ID of another book you want to borrow:"))
                            break
                        except:
                            print("Enter a valid ID from the record.")


        
        else:
            print("\nError!!!No book with such book ID.")
            break
        
    return price_of_book,book_Name



#to borrow multiple books
def book_borrow_continued(book_record,book_record_display,book_total_cost,book_name):
    flag = True
    book_cost,book_Name = book_borrow(book_record)
    book_total_cost += int(book_cost)
    book_name += book_Name+"\n"
    
    while flag == True:
        Yes_No = input("\nIf you want to borrow another book 'Y' else type 'N':")
        if (Yes_No.upper() == "Y"):
            book_cost,book_Name = book_borrow(book_record)
            book_total_cost += int(book_cost)
            book_name += "\t\t\t\t "+book_Name+"\n"
            
        elif (Yes_No.upper() == "N"):
            print("\nThank you for borrowing the books. Happy reading :).\n\n")
            break
        else:
            break
        
    return book_total_cost,book_name



#bill of books borrowed
def book_bill(cost_book,book_name,name):
    bill_date_time = datetime.datetime.now().replace(microsecond=0) #to exclude microsecond

    #to have unique name in the file
    hour = str((datetime.datetime.now().hour))
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    unique_file_number = hour+minute+second 

    #bill and structure
    file = open("b_"+name+"_"+unique_file_number+".txt","w")
    file.write("----------------------------------LIBRARY MANAGEMENT SYSTEM----------------------------------")
    file.write("\nBILL FOR BORROW:")
    file.write("\n\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nCustomer name \t\t\t: "+name)
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nDate and Time   \t\t\t: "+str(bill_date_time))
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nName of the borrowed book    \t:"+book_name)
    file.write("--------------------------------------------------------------------------------------------------------------------")
    file.write("\nTotal Cost     \t\t\t: $"+str(cost_book))
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\n\nHope you have a good time reading the book.")
    
    file.close()


def book_record_displayAvailable():
    print("\nGlad to know.The book is available.")




#Start for returning the book

def book_add(book_record, book_quantity, book_ID):
    book_quantity1 = book_record[4]
    book_quantity2 = book_record[9]
    book_quantity3 = book_record[14]
    book_quantity4 = book_record[19]
    book_quantity5 = book_record[24]
    book_quantity6 = book_record[29]
    book_quantity7 = book_record[34]
    book_quantity8 = book_record[39]
    book_quantity9 = book_record[44]
    book_quantity10 = book_record[49]
    
    file = open("book_list.txt", "w")
    
    if book_ID == 1:
        book_quantity1 = int(book_record[4])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+str(book_quantity1)+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 2:
        book_quantity2 = int(book_record[9])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+str(book_quantity2)+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 3:
        book_quantity3 = int(book_record[14])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+str(book_quantity3)+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 4:
        book_quantity4 = int(book_record[19])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+str(book_quantity4)+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 5:
        book_quantity5 = int(book_record[24])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+str(book_quantity5)+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

        
    elif book_ID == 6:
        book_quantity6 = int(book_record[29])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+str(book_quantity6)+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")
        
    elif book_ID == 7:
        book_quantity7 = int(book_record[34])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+str(book_quantity7)+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 8:
        book_quantity8 = int(book_record[39])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+str(book_quantity8)+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 9:
        book_quantity9 = int(book_record[44])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+str(book_quantity9)+"\n10,On the Road,Jack Kerouac,$10,"+book_quantity10+"")

    elif book_ID == 10:
        book_quantity10 = int(book_record[49])+1
        file.write("1,The Alchemist,Paulo Coelho,$5,"+book_quantity1+"\n2,Song of Solomon,Toni Morrison,$10,"+book_quantity2+
                   "\n3,Gilead,Marilynne Robinson,$15,"+book_quantity3+"\n4,Elevation,Stephen King,$15,"+book_quantity4+
                   "\n5,Ghost Wall,Sarah Moss,$4,"+book_quantity5+"\n6,War and Peace,Leo Tolstoy,$14,"+book_quantity6+
                   "\n7,East of Eden,John Steinbeck,$9,"+book_quantity7+"\n8,Mortal Engines,Philip Reeve,$11,"+book_quantity8+
                   "\n9,The Kite Runner,Khaled Hosseini,$13,"+book_quantity9+"\n10,On the Road,Jack Kerouac,$10,"+str(book_quantity10)+"")

    
    file.close()

    
    
    book_quantity_remaining = book_quantity + 1
    for i in range(len(book_record)):
        for j in range(len(book_record[i])):
            if book_ID == 1:
                book_record[4] = str(book_quantity_remaining)
                
            elif book_ID == 2:
                book_record[9] = str(book_quantity_remaining)
                
            elif book_ID == 3:
                book_record[14] = str(book_quantity_remaining)
                
            elif book_ID == 4:
                book_record[19] = str(book_quantity_remaining)
                
            elif book_ID == 5:
                book_record[24] = str(book_quantity_remaining)
                
            elif book_ID == 6:
                book_record[29] = str(book_quantity_remaining)

            elif book_ID == 7:
                book_record[34] = str(book_quantity_remaining)

            elif book_ID == 8:
                book_record[39] = str(book_quantity_remaining)

            elif book_ID == 9:
                book_record[44] = str(book_quantity_remaining)

            elif book_ID == 10:
                book_record[49] = str(book_quantity_remaining)


#Return book
def book_return(book_record, name, book_record_display):
    flag = True
    valid_y = True
    valid_n = True
    
    while valid_y == True:
        try:
            book_ID = int(input("\nEnter the book ID: "))
            break
        
        except:
            print("\nEnter a valid ID from the record.")
            
   
            
            
    
    while flag == True:
        if book_ID == 1:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
            
            book_quantity = int(book_record[4])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        elif book_ID == 2:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[9])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        elif book_ID == 3:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[14])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        elif book_ID == 4:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[19])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        elif book_ID == 5:


            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[24])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        elif book_ID == 6:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[29])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break

        elif book_ID == 7:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[34])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break

        elif book_ID == 8:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[39])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break

        elif book_ID == 9:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[44])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break

        elif book_ID == 10:

            while valid_n == True:
        
                try:
                    book_no_of_day = int(input("\nFor how many days has been the book borrowed??? "))
                    break
        
                except:
                    print("\nEnter a valid day.")

            book_fine(book_no_of_day, name, book_record, book_ID)
                    
            book_quantity = int(book_record[49])
            book_add(book_record, book_quantity, book_ID)
            book_record_display(book_record)
            break
        
        else:
            print("Error!!!No book with such book ID.")
            break
            


#Fine for book
def book_fine(book_no_of_day, name, book_record, book_ID):
    if int(book_no_of_day) > 10:
        book_fine_bill(name, book_record, book_ID, book_no_of_day)
        
    else:
        book_no_fine_bill(name, book_record, book_ID)


#Fine bill for book
def book_fine_bill(name, book_record, book_ID, book_no_of_day):
    name_of_book = book_counts(book_record, book_ID)
    book_fine_amount = (int(book_no_of_day) - 10) * 1
    bill_date_time = datetime.datetime.now().replace(microsecond=0)

    #to have unique name in the file
    hour = str((datetime.datetime.now().hour))
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    unique_file_number = hour+minute+second
    

    
    file = open("r_"+name+"_"+unique_file_number+".txt", "w")
    file.write("----------------------------------LIBRARY MANAGEMENT SYSTEM----------------------------------")
    file.write("\nBILL FOR FINE:")
    file.write("\n\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nCustomer name \t\t\t: "+name)
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nDate and Time   \t\t\t: "+str(bill_date_time))
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nName of the borrowed book    \t:"+name_of_book)
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nFine amount     \t\t\t: $"+str(book_fine_amount))
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\n\nHope you had a good time reading the book.")
    file.close()


#No fine bill for book
def book_no_fine_bill(name, book_record, book_ID):
    name_of_book = book_counts(book_record, book_ID)
    bill_date_time = datetime.datetime.now().replace(microsecond=0) #excluding microsecond

    
    hour = str((datetime.datetime.now().hour))
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    unique_file_number = hour+minute+second

    #bill and structure
    file = open("r_"+name+"_"+unique_file_number+".txt", "w")
    file.write("----------------------------------LIBRARY MANAGEMENT SYSTEM----------------------------------")
    file.write("\nNO FINE:")
    file.write("\n\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nCustomer name \t\t\t: "+name)
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nDate and Time   \t\t\t: "+str(bill_date_time))
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nName of the borrowed book    \t:"+name_of_book)
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\nNO FINE :D. The book was returned on time.")
    file.write("\n--------------------------------------------------------------------------------------------------------------------")
    file.write("\n\nHope you had a good time reading the book.")
    
    file.close()

    
