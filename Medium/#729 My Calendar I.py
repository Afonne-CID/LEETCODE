class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        self.bookings[start] = 1 + self.bookings.get(start, 0)
        self.bookings[end] = -1 + self.bookings.get(end, 0)

        cnt = 0
        for i in sorted(self.bookings.keys()):
            cnt += self.bookings[i]
            if cnt > 1:
                self.bookings[start] -= 1
                self.bookings[end] += 1
                return False
        return True
        
    # def book(self, start: int, end: int) -> bool:       
    #     for booking in self.bookings:
    #         if (not start >= booking[1]) and (not end <= booking[0]):
    #             return False
    #     self.bookings.append([start, end])
    #     return True
