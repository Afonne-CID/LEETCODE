class MyCalendarThree:

    def __init__(self):
        self.bookings = {}

    def book(self, start: int, end: int) -> int:
        if start in self.bookings:
            self.bookings[start] += 1
        else:
            self.bookings[start] = 1
        if end in self.bookings:
            self.bookings[end] += -1
        else:
            self.bookings[end] = -1

        cnt = 0
        res = 0
        for b in sorted(self.bookings.keys()):
            cnt += self.bookings[b]
            res = max(cnt, res)
        return res