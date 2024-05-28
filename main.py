import tabula
import datetime as dt
from icecream import ic
from loop import automate


# Start
tables = tabula.read_pdf("roster.pdf", pages="all", pandas_options={"header": None})
cols = tables[0].values.tolist()[1]
cols.pop(0)

shifts = [cols[i : i + 3] for i in range(0, len(cols), 3)]
ic(shifts)

# pass the shifts array into the automate function which creates calendar events
automate(shifts)
