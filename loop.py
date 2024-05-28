import SendToGoogle as event
import datetime as dt
from icecream import ic


def automate(shifts):
    # DECALRING CONSTANTS
    day = dt.timedelta(days=1)
    # # # set variable day to equal 1 day.
    # # # doing this ensures that as days increase over the roster period,
    # # # that at the end of the month, the month will flick over

    # input the day that the roster starts on
    startDate_str = (input("what is the Start Date of the roster?\n(YYYY-MM-DD)--> "))
    startDate_iso = dt.date.fromisoformat(startDate_str)

    # Looping through the shifts
    numevents = 0
    for shift in shifts:
        if shift[0] == "OFF":
            print(startDate_iso, "Day Off")
            startDate_iso += day
            continue
        start = shift[0] + ":00"
        end = shift[1] + ":00"
        name = shift[2]
        event.create(name, startDate_iso, start, end)
        # print(startDate_iso, name, start, end)
        numevents += 1
        startDate_iso += day

    print(f"\n\nAutomation Complete \n{numevents} Events Created")
