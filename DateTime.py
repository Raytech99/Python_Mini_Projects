import datetime as dt

date = dt.date.today()
time = dt.datetime.now()
"""
%a --> Weekday abbreviated
%b --> Month name abbreiviated
%d --> Number day of the month 01-31
%Y --> Year with century
%I --> Hour
%M --> Minute
%p --> AM or PM
"""
print(f"""Today's date is {date:%a, %b %d %Y}.
The time right now is {time: %I: %M %p}.""")
