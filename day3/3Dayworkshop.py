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
