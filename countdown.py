import datetime
import time


class CountdownTimer:
    def __init__(self,total_seconds:int):
        self.total_seconds=total_seconds

    def start(self):
        for time_left in range (self.total_seconds,-1,-1):
            minutes,seconds=divmod(time_left,60)

            displayed_time=f"{minutes:02d}:{seconds:02d}"
            #\r overites previous lines instead of spamming new ones
            print(f"\r time left   {displayed_time}",end=" ")
            if time_left>0:
                time.sleep(1)

        print("Time up !!!!!!!!!!")

def get_valid(prompt:str):
    while True:
        raw_sec=input(prompt)
        if raw_sec.isdigit() and int(raw_sec)>0:
            return int(raw_sec)
        else:
            print("Enter a valid number of seconds")

def main():
    print("**Welcome to our Countdown Program**")
    total_time=get_valid("Enter the number of seconds of the countdown:")
    count=CountdownTimer(total_seconds=total_time)
    count.start()


if __name__=="__main__":
    main()


    