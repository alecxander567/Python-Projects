import time
import curses


# Function to start time
def starTime(seconds, minutes, hours):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        curses.halfdelay(1) 

        for i in range(total_seconds + 1):
            remaining_time = total_seconds - i
            
            if remaining_time < 0:  
                break
            
            hours_left = remaining_time // 3600
            minutes_left = (remaining_time // 60) % 60
            seconds_left = remaining_time % 60
            stdscr.addstr(0, 0, f"{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
            stdscr.refresh()
            time.sleep(1)
            
            # Check if the user pressed the 'q' key
            if stdscr.getch() == ord('q') or remaining_time == 0:
             break

        if i < total_seconds - 1:
            stdscr.addstr(1, 0, "Timer stopped!")
        else:
            stdscr.addstr(1, 0, "Timer finished!")

            stdscr.refresh()

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        
        print(f"\n{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
        print("\nTimer stopped!")

         
# Main Function
print("Stopwatch Python")
while True:
    try:  
        print("\n1. Start timer")
        print("0. Exit")
        
        option = input("\nSelect an option : ")
        
        if option == "1":
            print("\nSet the timer: ")
            print("Please note that to stop the timer you must press 'q' key.")
            hours = int(input("\nEnter hours : "))
            minutes = int(input("Enter minutes : "))
            seconds = int(input("Enter seconds : "))
            starTime(seconds, minutes, hours)
        elif option == "0":
            print("\nExiting...")
            break
    except ValueError:
        print("\nInvalid input! Please try again.")
        continue
            
