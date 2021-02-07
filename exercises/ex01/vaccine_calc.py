"""A vaccination calculator."""

__author__ = "730279779"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
p_doses: int = int(input("Doses Administered: "))
doses_day: int = int(input("Doses Per Day: "))
target_vaccinated: int = int(input("Target Percentage Vaccined (0ut of 100): "))

end_number = ((((population*2)-p_doses)*(target_vaccinated/100))/doses_day)
today = datetime.today()
timespan: timedelta = timedelta(end_number)
end_date: datetime = today + timespan
dateoutput = str(end_date.strftime("%B %d, %Y"))
day_output = str(end_number)
count_percent = str(target_vaccinated)

print("We will reach " + count_percent + "% " + "in " + day_output + " days, which falls on " + dateoutput + ".")