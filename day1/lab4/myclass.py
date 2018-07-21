class polygon():

    def __init__(self):
        self.points = []

    def addPoint(self, x, y):
        self.points.append([x, y])

    def disform(self, x1, x2, y1, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

    def perimeter(self):
        answer = 0
        x1 = abs(self.points[0][0])
        x2 = abs(self.points[len(self.points)-1][0])
        y1 = abs(self.points[len(self.points)-1][1])
        y2 = abs(self.points[0][1])
        answer += self.disform(x1, x2, y1, y2)
        if len(self.points) <= 2:
            print("you have not added enough points")
        else:
            for i in range(len(self.points)-1):
                x1 = abs(self.points[i][0])
                x2 = abs(self.points[i+1][0])
                y1 = abs(self.points[i][1])
                y2 = abs(self.points[i+1][1])
                answer += self.disform(x1, x2, y1, y2)
            return answer

    def area(self):
        points = self.points
        x = 0
        answer = 0
        points.append(points[0])
        while x < len(points) - 1:
            answer1 = points[x][0]*points[x+1][1] - points[x-1][0]*points[x][1]
            x += 1
            answer += answer1
        return abs(answer) / 2

banana = polygon()
banana.addPoint(1000, 200)
banana.addPoint(200, 400)
banana.addPoint(100, 300)
print(banana.perimeter())
print(banana.area())
