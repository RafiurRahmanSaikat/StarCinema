class Star_Cinema:
    def __init__(self):
        self._hall_list=[]

    def entry_hall(self,hall):
        self._hall_list.append(hall)
        return f'Hall No {hall._hall_no} Inserted Successfully'

    def view_all_running_shows(self):
        print("All Shows")
        for hall in self._hall_list:
            print(f'\nHall: {hall}')
            hall.view_show_list()

class Hall:
    def __init__(self,rows,cols,hall_no):

        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no

    def __str__(self):
        return f"{self._hall_no} \nShow List:{self._show_list}\nSeats={self._seats}"

    def entry_show(self,id,movie_name,time):
        self._show_list.append((id,movie_name,time))
        self._seats[id]=[["Available" for x in range(self._cols)] for y in range(self._rows)]

    def  book_seats(self,id,seat_list):
        if id not in self._seats:
            raise ValueError("Invalid show ID")

        booked__seats=[]
        for row,col in seat_list:
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                raise ValueError("Invalid Seat location")

            if self._seats[id][row][col]!="Available":
                raise ValueError("Already Booked")

            self._seats[id][row][col]="Booked"
            booked__seats.append((row,col))

        print(f'Your Booked Seats: {booked__seats} for {id}')

    def view_show_list(self):
        if not self._show_list:
            print("No Show Found.")
            return

        for show in self._show_list:
            print(f"Show ID : {show[0]}, Movie Name : {show[1]}, Time: {show[2]}")

    def view_available_seats(self,id):
        if id not in self._seats:
            raise ValueError("Invalid Show ID")

        print(f"Available Seats for Show {id}:")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col]=="Available":
                    print(f" Row: {row + 1}, Col: {col + 1}")





cinema = Star_Cinema()
hall1 = Hall(2,2,1)
hall1.entry_show(100, "Zinga Lala", "Ajibon Colbe")
cinema.entry_hall(hall1)
# cinema.view_all_running_shows()



# print(cinema.entry_hall(hall1))
# print(cinema.view_all_running_shows())


def run():
    while True:
        print("1. VIEW ALL SHOWS")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. Exit")
        try:
            option = int(input("ENTER OPTION: "))
            if option == 1:
                cinema.view_all_running_shows()
            elif option == 2:
                sid = int(input("Enter  Show ID: "))
                hall1.view_available_seats(sid)
            elif option == 3:
                hall_no = int(input("Enter Hall Number: "))
                num_seats = int(input("Enter the number of seats to book: "))
                booked_seats = []
                for i in range(num_seats):
                    row = int(input(f"Enter row number for seat {i+1}: "))
                    col = int(input(f"Enter column number for seat {i+1}: "))
                    booked_seats.append((row - 1, col - 1))
                try:
                    hall_no = int(input("Enter Hall Number: "))
                    hall_found = False
                    for hall in cinema._hall_list:
                        if hall._hall_no == hall_no:
                            hall.book_seats(show_id, booked_seats)
                            hall_found = True
                            break
                    if not hall_found:
                        print("Hall not found.")
                except ValueError as err:
                    print(err)
            elif option == 4:
                break
            else:
                print("Invalid option. Try again.")
        except ValueError as err:
            print(err)




run()