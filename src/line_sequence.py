class LineSequence:
    def __init__(self, x, y) -> None:

        self.x_center = x/2
        self.y_center = y/2
        self.CONSTANT = 145.243282498

        self.point_mapping = dict()
        self.points = []
        self.last = None
        self.lines = []

    def add(self, z : list, new_sequence):
        t = z.copy()

        t[1] = -1 * (t[1] - self.y_center)/self.CONSTANT
        t[0] = (t[0] - self.x_center)/self.CONSTANT

        t = tuple(t)
        
        if (next := self.point_mapping.get(t)) == None:
            self.points.append((t[0], t[1], -2))
            self.points.append((t[0], t[1], 0))
            self.point_mapping[t] = int(len(self.points)/2 - 1)
            next = int(len(self.points)/2 - 1)
            
        if self.last != None and not new_sequence:
            self.lines.append((self.last*2, next*2))
            self.lines.append((self.last*2 + 1, next*2 + 1))
        
        self.last = next

    def get_vals(self):
        return (self.points, self.lines)