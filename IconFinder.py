class IconPositions:
    def __init__(self):
            self.y = 300
            self.width = 28
            self.height = 28
            self.position_one_x = 74
            self.position_two_x = 134
            self.position_three_x = 194
            self.position_four_x = 254
            self.position_five_x = 314
            self.position_six_x = 374
            self.position_seven_x = 434
            self.position_eight_x = 494
            self.position_nine_x = 554
            self.position_ten_x = 614

    def position_one_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_one_x:self.position_one_x+self.width]
    
    def position_two_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_two_x:self.position_two_x+self.width]

    def position_three_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_three_x:self.position_three_x+self.width]
    
    def position_four_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_four_x:self.position_four_x+self.width]
    
    def position_five_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_five_x:self.position_five_x+self.width]
    
    def position_six_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_six_x:self.position_six_x+self.width]
    
    def position_seven_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_seven_x:self.position_seven_x+self.width]
    
    def position_eight_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_eight_x:self.position_eight_x+self.width]
    
    def position_nine_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_nine_x:self.position_nine_x+self.width]
    
    def position_ten_output(self, frame):
        return frame[self.y:self.y+self.height, self.position_ten_x:self.position_ten_x+self.width]