import datetime, portion


startdate = input("Enter datetime1 in YY/MM/DD HH:MM :")
enddate = input("Enter datetime1 in YY/MM/DD HH:MM :")

datetime1 = datetime.datetime.strptime(startdate, "%Y/%m/%d %H:%M")
datetime2 = datetime.datetime.strptime(enddate, "%Y/%m/%d %H:%M")

datetime_diff = (
    datetime2 - datetime1
)  # this is normal difference in this night time is included
print("Before Removing Nights :", datetime_diff)
m = 0

# hours = [0, 1, 2, 3, 4, 5]
hours = portion.open(
    datetime.time(00, 00, 00), datetime.time(5, 59, 59)
)  # this is interval to check time is in this interval or not

if (datetime_diff.days == 0) and (
    datetime1.time() in hours and datetime2.time() in hours
):  # this condition work when both date are same, both time are nigth time and number of days between dates are 0
    print("After Removing Nights :", "00:00:00")
else:
    dt1_diff = datetime.datetime.strptime(
        "00:00:00", "%H:%M:%S"
    )  # this is used to calculate difference between 6:00AM - starttime  default 00:00:00
    dt2_diff = datetime.datetime.strptime(
        "00:00:00", "%H:%M:%S"
    )  # this is used to calculate difference between 00:00AM - endtime   default 00:00:00
    if datetime1.time() in hours:
        d1 = datetime.datetime(
            datetime1.year, datetime1.month, datetime1.day, 6, 0
        )  # creating datetime object with same date as startdate but time will be of 6:00AM
        dt1_diff = datetime.datetime.strptime(
            str(d1 - datetime1), "%H:%M:%S"
        )  # calculating difference between 6:00AM - starttime

    if datetime2.time() in hours:
        d2 = datetime.datetime(
            datetime2.year, datetime2.month, datetime2.day, 0, 0
        )  # creating datetime object with same date as enddate but time will be of 00:00AM
        dt2_diff = datetime.datetime.strptime(
            str(datetime2 - d2), "%H:%M:%S"
        )  # calculating difference between endtime - 00:00:00
    # m = total minutes of night(12AM - 6AM) can be calculate by adding dt1_diff, dt2_diff and (60 * 6hour * number of day between days)
    m = (
        (dt2_diff.hour + dt1_diff.hour) * 60
        + (dt2_diff.minute + dt1_diff.minute)
        + datetime_diff.days * 6 * 60
    )
    if (
        datetime_diff.days >= 1
        and datetime1.time() in hours
        and datetime2.time() in hours
    ):
        m -= 6 * 60
    print(
        "After Removing Nights :", datetime_diff - datetime.timedelta(minutes=m)
    )  # this is actual difference in this nigth time is subtracted
