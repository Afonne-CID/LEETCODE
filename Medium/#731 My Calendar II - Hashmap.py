class MyCalendarTwo:

    def __init__(self):
        self.bookings = {}

    def book(self, start: int, end: int) -> bool:
        cnt = 0
        if start in self.bookings:
            self.bookings[start] += 1
        else:
            self.bookings[start] = 1
        if end in self.bookings:
            self.bookings[end] += -1
        else:
            self.bookings[end] = -1

        for b in sorted(self.bookings.keys()):
            cnt += self.bookings[b]
            if cnt > 2:
                self.bookings[start] -= 1
                self.bookings[end] += 1
                return False
        return True