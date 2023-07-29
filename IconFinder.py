class IconPositions:
    def __init__(self):
            self.y = 296
            self.width = 36
            self.height = 36
            self.position_one_x = 70    #CERTAIN - 60.78
            self.position_two_x = 129   #CERTAIN - 483.36
            self.position_three_x = 190 #CERTAIN - 485.93
            self.position_four_x = 250  #CERTAIN - 295.78
            self.position_five_x = 310  #CERTAIN - 566.12
            self.position_six_x = 369   #CERTAIN - 979.64
            self.position_seven_x = 430 #CERTAIN - 990.56
            self.position_eight_x = 489 #CERTAIN - 536.03
            self.position_nine_x = 550 
            self.position_ten_x = 610 

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