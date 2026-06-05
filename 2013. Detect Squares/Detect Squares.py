class DetectSquares:

    def __init__(self):
        self.map=defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.map[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        sqr_c=0
        x1,y1=point

        for (x2,y2),n in self.map.items():
            x_dist, y_dist= abs(x1-x2), abs(y1-y2)
            if x_dist==y_dist and x_dist>0:
                corner1=(x1,y2)
                corner2=(x2,y1)
                if corner1 in self.map and corner2 in self.map:
                    sqr_c += n * self.map[corner1] * self.map[corner2]
        return sqr_c


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)