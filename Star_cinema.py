"""
1. make a class star cinema with one class attribute that is an empty list, 
   and Make a method named entry_hall()

2. Make a class named Hall which will have 5 instance attributes


"""

class Star_Cinema:
    hall_list = []

    def entry_hall (self,hall_no):
        self.hall_list.append(hall_no)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_lis = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        

        self.entry_hall(self)

        

    def entry_show(self,id,movie_name,time):    # for entry show
        self.show_lis.append((id,movie_name,time))

        seats = [[True for j in range(self.cols)] for i in range(self.rows)]
        self.seats[id] = seats

     
        

    # seat booking method....

    def book_seats(self, customuer_name, phone, show_id, seat_list):
        isfound = False
        iserror = False
        for show in self.show_lis:
            if show_id == show[0]:
                isfound = True
                break

        if isfound == False:
            print("\nInvalide show ID")
            iserror = True
            return

        booked = False

        for seat_item in seat_list:
            if int(seat_item[0])>=self.rows or int(seat_item[1])>=self.cols:
                print("\nInvaled seat number. Try again.")
                iserror = True
                break
            
            if self.seats[show_id][int(seat_item[0])][int(seat_item[1])] == False:
                print("\nSeat already occupied.")
                iserror = True
                break
            

            if iserror == False:
                self.seats[show_id][int(seat_item[0])][int(seat_item[1])] = False
                booked = True
                
                
        if booked == True:
            print("\n##### Ticket booked successfully! #####")
            print("-"*51)
            print("Name:",customuer_name)
            print("phone: ",phone)

            for i in self.show_lis:
                if show_id == i[0]:
                    print(f"\nMovie Name: {i[1]} \t\t Time: {i[2]}")

            print("Tickets: ", seat_list)
            print("-"*51)

    # view all the shows running.

    def view_show_list(self):
        print("-"*71)
        for i,n,t in self.show_lis:
            print(f"Movie Name: {n} \t\t Show ID: {i} \t\t Time: {t}")
    
        print("-"*71)



    def view_available_seats(self,show_id):
        flag = False
        for i in self.show_lis:
            if show_id == i[0]:
                print(f"\nMovie Name: {i[1]} \t\t Time: {i[2]}")
                flag = True

        if flag == True:
            print("\nX for olready booked seats")    
            print("-"*51)
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.seats[show_id][i][j] == False:
                        print('X',end='\t\t')
                    else:
                        print(chr(i+65)+str(j),end='\t\t')
                print()

            print("-"*51)

        else:
            print("\nInvalide show ID")




hall = Hall(4,4,'mr9')   # Declaring the object
    

# Entry show 
hall.entry_show('abc','Nimo','03:50 PM')
hall.entry_show('asd','Ice Ege','10:00 AM')
hall.entry_show('bcd','Avatar','05:00 PM')


# hall.book_seats('Sakib',3436878,'abc',[(2,2),(3,1),(3,0),(1,1)])


# Replica system

while True:
    print(f"\n1. VIEW ALL SHOWS TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKETS")
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        hall.view_show_list()

    elif user_input == 2:
        id = input("Enter the show ID: ")
        hall.view_available_seats(id)

    elif user_input == 3:
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        show_id = input("Enter the show ID: ")
        seats = int(input("Enter the number of seats: "))
        seat_lst = []
        for i in range(seats):
            ele = input("Enter seat No:")   # Enter the seat No by row and col index number.
            ascii_val = str(ord(ele[0])-65)
            string = ele.replace(ele[0], ascii_val, 1)
            seat_lst.append((string))

        hall.book_seats(name,phone,show_id,seat_lst)