l1=list(input("enter email addresses fo day1:").split(" "))
l2=list(input("enter email addresses fo day2:").split(" "))
l3=list(input("enter email addresses fo day3:").split(" "))
def CleanLists(l1,l2,l3):
    s1=set(l1)
    s2=set(l2)
    s3=set(l3)
    s1={i.lower() for i in s1}
    s2={i.lower() for i in s2}
    s3={i.lower() for i in s3}
    return s1,s2,s3
s1,s2,s3=CleanLists(l1,l2,l3)
def uniqueAttendees(s1,s2,s3):
    return s1|s2|s3
def AttendedAllDays(s1,s2,s3):
    return s1&s2&s3
def AttendedOnlyOneDay(s1,s2,s3):
    return (s1-(s2|s3))|(s2-(s1|s3))|(s3-(s1|s2))
def pairwiseOverlaps(s1,s2,s3):
    return (s1&s2)|(s2&s3)|(s3&s1)
print("unique attendees:",uniqueAttendees(s1,s2,s3))
print("attended all days:",AttendedAllDays(s1,s2,s3))
print("attended only one day:",AttendedOnlyOneDay(s1,s2,s3))
print("pairwise overlaps:",pairwiseOverlaps(s1,s2,s3))

'''
A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
Write a Python program that:
Cleans each day's list (normalizes case, removes duplicates).
Prints the total number of unique attendees across all days.
Prints the list of attendees who attended all three days.
Prints the list of attendees who attended exactly one day.
Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
Produces a final report with counts and sorted lists for each of the above outputs.
'''