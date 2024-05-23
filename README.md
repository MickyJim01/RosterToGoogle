# Python Project #2

> ## Aim:
>
> Create a prgram that reads my roster in .pdf form, then extract the data to create Google Calendar events for my rostered shifts.

## Method

### Creating a Calendar Event in Google Calendar

1. Watch Youtube
2. Try to understand what youtube man is doing
3. Follow along blindly in youtube mans footsteps
4. Somehow setup Google Cloud and Google Develper and grab API Key
    - [Python/Google Quickstart Guide](https://developers.google.com/calendar/api/quickstart/python)
    - [Python/Google Creating an Event](https://developers.google.com/calendar/api/guides/create-events#python)
    - [Parameters for Creating an Event](https://developers.google.com/calendar/api/v3/reference/events/insert)
5. Downlaod `.json` file with API Key inside
    - Rename to `"credentials.json"`
    - Put inside working directory
6. Write the creating event function.
    - Add some parameters like `name`, `date`, and `start` & `end` times.
    - Re-learn how to spell ~~Calender~~ **Calendar**

### Reading the `.pdf`

1. Import `Tabula`[^1] and the main event function from `main.py`
2. Read the `.pdf`
3. Isolating my shift row:

    ```
    cols = tables[0].values.tolist()[0]
    cols.pop(0)
    ```

    > `cols.pop(0)` is required because the first column in the row is my name.

    - Where `Table[0]` is the index for the first table on the page

        &

    - Where `.values.tolist()[0]` is the index for the first row in the table

4. Split the lenth of my roster into groups of 3 (start time, end time, and description)
    - Should be 7 groups
    ```
    shifts = [cols[i:i+3] for i in range(0, len(cols), 3)]
    ```
    > Note: `range(start, end, increment)`
5. Create a _for loop_ to iterate through the previously sliced shift groups
6. Create an _if_ function to skip days that i have off
    ```
    if shift[0] == "OFF":
        startDate += 1
        continue
    ```
    > `shift[0]` is index for start time
    >
    > `startdate += 1` increments the declared `startdate` variable so as to make sure that a _'day off'_ event is not added, but the date still increases
7. Declare varaibles to used later in `create()` function while looping through
    ```
    start = shift[0] + ":00"
    end = shift[1] + ":00"
    name = shift[2]
    ```
    > `start`, `end`, and `name`
    >
    > Add seconds to format correctly for Google API (`+ ":00"`)
8. Call `create()` from event import and input arguments with declared variables
    ```
    event.create(name, startDateFull, start, end)
    ```
9. Increase counters
    ```
    numevents += 1
    startDate += 1
    ```
    > Most importantly `startDate` counter to keep track of days
    >
    > `numevents` counter just counts how many events will be created.

### I Hate Git blugh argh pee pee

[^1]: `pip install tabula-py`
