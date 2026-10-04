import time
timestamp = (time.strftime('%H:%M:%S'))
# strftime ->> Convert a time tuple to a string according to a format specification.
# strftime() means format the current time into a string according to the format you provide.
print(timestamp)

timestamp = int(time.strftime('%H'))
print(timestamp)# withoit using int it will return string therefore to convert string into int i have used int
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

