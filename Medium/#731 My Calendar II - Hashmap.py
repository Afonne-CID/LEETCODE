class MyCalendarTwo:

    def __init__(self):
        self.bookings = {}

    def book(self, start: int, end: int) -> bool:
        cnt = 0
        self.bookings[start] = 1 + self.bookings.get(start, 0)
        self.bookings[end] = -1 + self.bookings.get(end, 0)

        for b in sorted(self.bookings.keys()):
            cnt += self.bookings[b]
            if cnt > 2:
                self.bookings[start] -= 1
                self.bookings[end] += 1
                return False
        return True