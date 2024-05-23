import tabula
import main as event

tables = tabula.read_pdf("roster.pdf", pages="all", pandas_options={"header": None})
cols = tables[0].values.tolist()[0]
cols.pop(0)

shifts = [cols[i : i + 3] for i in range(0, len(cols), 3)]

startDate = int(input("what is the Start Date? --> "))
numevents = 0
for shift in shifts:
    startDateFull = "2024-05-" + str(startDate)
    if shift[0] == "OFF":
        startDate += 1
        continue
    start = shift[0] + ":00"
    end = shift[1] + ":00"
    name = shift[2]
    event.create(name, startDateFull, start, end)
    numevents += 1
    startDate += 1

print(f"\n\nAutomation Complete \n{numevents} Events Created")
