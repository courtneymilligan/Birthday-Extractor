import re, os, sys

friends = []
add_friends = True
minutes = 0


# inputs for desired reminder time
def get_time():
    global minutes
    try:
        minutes = int(input("How many hours before the event do you want your reminder?: ")) * (-60)
    except TypeError:
        print("Not a number. Try again.")
        get_time()


outlook = input("Do you use outlook? (y/n): ")
if outlook == 'y':
    get_time()

print("Ready to create friend list.")
while add_friends:
    new_friend = input("Add a friend's name, or type 'done' and hit enter when list is complete: ")
    if new_friend.lower() == 'done':
        add_friends = False
    else:
        friends.append(new_friend)

try:
    file = open(os.path.join(sys.path[0], "birthday-calendar.ics")).read()
except FileNotFoundError:
    print('ERROR: Could not open file. Check file name and location')

start_pattern = 'BEGIN:VEVENT'
end_pattern = 'END:VCALENDAR'
start = re.search(start_pattern, file).span()[0]
end = re.search(end_pattern, file).span()[0]
header = file[:start].strip()
footer = '\n' + file[end:]
file = file[start:end]

file = file.replace('END:VEVENT', 'END:VEVENT&sep')
file = file.replace('TRANSP:TRANSPARENT',
                    f'TRANSP:TRANSPARENT\nBEGIN:VALARM\nTRIGGER:PT{minutes}M\nACTION:DISPLAY\nDESCRIPTION:Reminder\nEND:VALARM')
data = file.split('&sep')

new_list = []
for element in data:
    if element == '\n':
        continue
    name = element.split('SUMMARY:ðŸŽ‚ ')[1].split("\nTRANSP")[0]
    if name in friends:
        friends.remove(name)
        description = element.split('DESCRIPTION:')[1].split('\nSEQUENCE:')[0]
        element = element.replace(description, f"Today is {name}'s birthday!")
        new_list.append(element)

return_cal = '\n'.join(new_list)
return_cal = return_cal.replace('END:VEVENT\n', 'END:VEVENT')

return_cal = header + return_cal + footer

with open(os.path.join(sys.path[0], 'friend_birthdays.ics'), 'w') as f:
    f.write(return_cal)

print('Success, new cal generated: friend_birthdays.ics.')
if len(friends) > 0:
    print(f'Note: could not find birthdays for the following friends: {friends}')
