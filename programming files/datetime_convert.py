# Pulling in datetime library
from datetime import datetime

# Sample time as a string
date_str = "2022-03-17 10:45:30"

# Read in string to create a datetime object
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

# Reformat date style
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print newly formatted date toString
print(formatted_date)
