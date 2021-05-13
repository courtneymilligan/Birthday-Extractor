# Birthday-Extractor
Used with Google Chrome's 'Birthday Calendar Extractor for Facebook' to create calendar for specified list of friends

Instructions:
1. Install Chrome's 'Birthday Calendar Extractor for Facebook' url=https://chrome.google.com/webstore/detail/birthday-calendar-extract/imielmggcccenhgncmpjlehemlinhjjo
2. Open Facebook, click the 'Birthday Calendar Extractor for Facebook' extension, and select 'Generate Google Calendar - ICS'
3. Save 'import_birthdays.py' and 'birthday-calendar.ics' (generated by extension) in the same folder
4. Run the following in the command line:
    python <extract_birthdays file path>
5. Follow prompts
6. Import new friend_birthdays.ics file into your calendar
    a. For Outlook: File>Open & Export>Open Calendar>friend_birthdays.ics
    b. For Google Calendar: Settings>Import & export>Select file from your computer>friend_birthdays.ics
Notes:
- You must use a computer with Python installed on it
- If using Google Calendar, can add reminders following these steps:
    Settings>[your calendar name]>All-day event notifications>+ Add Notifications
