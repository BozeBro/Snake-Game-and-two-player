class Test:
    COLOR = "RED"
    def color(self):
        print("color")
        def print_color(self):
            print(COLOR)
        return self.print_color()

m = Test()
m.color()