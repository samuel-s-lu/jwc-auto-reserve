# jwc-auto-reserve

Python script that automatically reserves slots for activities in JWC (e.g. rock climbing, badminton).

To automate the process of "signing-in" without command line input, create a Python file "userInfo.py" and create a dictonary in the form:
    credentials = {"username": userString, "password": passString, "activity": desiredActivity}
    desired_events = [['Wednesday', '5:10 PM - 6:30 PM'],...] as an example.