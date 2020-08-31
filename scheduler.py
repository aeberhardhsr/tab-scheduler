import schedule
import time

# general settings
start_ausg_morgen = "20:51"
ende_ausg_morgen = "11:00"


start_ausg_mittag = "11:00"
ende_ausg_mittag = "13:30"

start_ausg_nachmittag = "13:30"
ende_ausg_nachmittag = "17:00"

start_ausg_abend = "17:00"
ende_ausg_abend = "21:00"


# Functions for displaying data content
# each function stands for one daily schedule referenced in the readme
def base_page():
    pass

def clear_tabs():
    pass

def ausgabe_morgen():
    #pass
    print("It's working!")

def ausgabe_mittag():
    pass

def ausgabe_nachmittag():
    pass

def ausgabe_abend():
    pass

# task scheduling
# list all tasks
schedule.every().day.at(start_ausg_morgen).do(ausgabe_morgen)
schedule.every().day.at(start_ausg_mittag).do(ausgabe_mittag)
schedule.every().day.at(start_ausg_nachmittag).do(ausgabe_nachmittag)
schedule.every().day.at(start_ausg_abend).do(ausgabe_abend)

# loop over the tasks so that the scheduler is working
while True:
    # Check if a task is scheduled and ready to run
    schedule.run_pending()
    time.sleep(5)