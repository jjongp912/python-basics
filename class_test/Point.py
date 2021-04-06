class Point:
    count_of_instance = 0  # Class 변수


    def  __init__(self, x, y):
        Point.count_of_instance += 1
        self.x = x  # 객체 변수
        self.y = y

    def draw(self):
        print(f'x={self.x}, y={self.y} 에 점을 그렸습니다.')