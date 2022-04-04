class clockTime:
    def __init__(self):
        self.hours = ""
        self.minutes = ""
        self.seconds = ""
        self.time = ""
    def setHours(self, hours):
        self.hours = hours
    def setMinutes(self, minutes):
        self.minutes = minutes
    def setSeconds(self, seconds):
        self.seconds = seconds
    def setTime(self):
        self.time = self.hours + ":" + self.minutes + ":" + self.seconds
    def showTime(self):
        print("Time is: " + self.time)

hours = input("Enter hours: ")
minutes = input("Enter minutes: ")
seconds = input("Enter seconds: ")
clock = clockTime()
clock.setHours(hours)
clock.setMinutes(minutes)
clock.setSeconds(seconds)
clock.setTime()
clock.showTime()