class LineSequence:
    def __init__(self, x, y) -> None:

        self.x_center = x/2
        self.y_center = y/2
        self.CONSTANT = 145.243282498

        self.point_mapping = dict()
        self.points = []
        # self.occurrences = []
        self.last = None
        self.lines = []

    def add(self, z : list, new_sequence):
        t = z.copy()

        t[1] = -1 * (t[1] - self.y_center)/self.CONSTANT
        t[0] = (t[0] - self.x_center)/self.CONSTANT

        t.append(0)

        t = tuple(t)
        
        if (next := self.point_mapping.get(t)) == None:
            self.points.append(t)
            self.point_mapping[t] = len(self.points) - 1
            next = len(self.points) - 1
            
        if self.last != None and self.last != next and not new_sequence:
            self.lines.append((self.last, next))
        
        self.last = next

    def remove_last(self):
        if len(self.points) == 0: return

        v = [None, None]
        if len(self.lines) > 0:
            v = self.lines.pop(len(self.lines) - 1)
        self.last = v[0]

        print(v)

        if v[1] != None and v[1] == len(self.points) - 1:
            print(p := self.points.pop(len(self.points) - 1))
            del self.point_mapping[p]


    def get_vals(self):
        return (self.points, self.lines)