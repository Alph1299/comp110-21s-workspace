"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730279779"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    time = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date = future_date(time)
    # TODO 5: Print the expected output using the variables above.
    t = str(int(time))
    tar = str(target)
    print("We will reach " + tar + "% vaccination in " + t + " days, which falls on " + date + ".")

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Takes inputs to return days until percentage target."""
    end_number = ((((population * 2) * (target / 100)) - doses) / doses_per_day)
    return end_number

   

# TODO 3: Define future_date function
def future_date(x: int) -> str:
    """Takes an int and returns a str value."""
    today = datetime.today()
    timespan: timedelta = timedelta(x)
    end_date: datetime = today + timespan
    date = str((end_date.strftime("%B %d, %Y")))
    return date

if __name__ == "__main__":
    main()
