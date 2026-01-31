import time
import os

def study_timer(minutes):
    seconds = minutes * 60
    print(f"Study session started for {minutes} minutes. Focus time!")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f'{mins:02d}:{secs:02d}'
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up! Take a break, you've earned it!")
    # Optional: Adds a beep sound (works on most Windows/Mac)
    print('\a') 

if __name__ == "__main__":
    try:
        user_input = int(input("How many minutes do you want to study? "))
        study_timer(user_input)
    except ValueError:
        print("Please enter a valid number of minutes.")
