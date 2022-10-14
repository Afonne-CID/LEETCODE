class MyCalendarThree:

    def __init__(self):
        self.bookings = {}

    def book(self, start: int, end: int) -> int:
        
        self.bookings[start] = 1 + self.bookings.get(start, 0)
        self.bookings[end] = -1 + self.bookings.get(end, 0)

        cnt, res = 0, 0

        for b in sorted(self.bookings.keys()):
            cnt += self.bookings[b]
            res = max(cnt, res)
        return res