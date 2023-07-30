from IconFinder import IconPositions
from IconMatch import IconMatch

pos = IconPositions()
match = IconMatch()

class InputBuilder:
    def __init__(self, resolution):
            # Reference images
            self.referenceImages = match.define_reference(resolution)
            self.neutral = 'NEUTRAL'

    def position_ten_input(self, frame):
        position = pos.position_ten_output(frame)
        input_ten = match.find_match(position, self.referenceImages)
        return input_ten
    
    def position_nine_input(self, frame):
        position = pos.position_nine_output(frame)
        input_nine = match.find_match(position, self.referenceImages)

        if input_nine == self.neutral:
            return self.neutral, self.neutral
        else:
            input_ten = self.position_ten_input(frame)
            return input_nine, input_ten

    def position_eight_input(self, frame):
        position = pos.position_eight_output(frame)
        input_eight = match.find_match(position, self.referenceImages)

        if input_eight == self.neutral:
            return self.neutral, self.neutral, self.neutral
        else:
            input_nine, input_ten = self.position_nine_input(frame)
            return input_eight, input_nine, input_ten

    def position_seven_input(self, frame):
        position = pos.position_seven_output(frame)
        input_seven = match.find_match(position, self.referenceImages)

        if input_seven == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_eight, input_nine, input_ten = self.position_eight_input(frame)
            return input_seven, input_eight, input_nine, input_ten

    def position_six_input(self, frame):
        position = pos.position_six_output(frame)
        input_six = match.find_match(position, self.referenceImages)
        
        if input_six == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_seven, input_eight, input_nine, input_ten = self.position_seven_input(frame)
            return input_six, input_seven, input_eight, input_nine, input_ten
        
    def position_five_input(self, frame):
        position = pos.position_five_output(frame)
        input_five = match.find_match(position, self.referenceImages)

        if input_five == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_six, input_seven, input_eight, input_nine, input_ten = self.position_six_input(frame)
            return input_five, input_six, input_seven, input_eight, input_nine, input_ten
        
    def position_four_input(self, frame):
        position = pos.position_four_output(frame)
        input_four = match.find_match(position, self.referenceImages)
        
        if input_four == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_five, input_six, input_seven, input_eight, input_nine, input_ten = self.position_five_input(frame)
            return input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten
        
    def position_three_input(self, frame):
        position = pos.position_three_output(frame)
        input_three = match.find_match(position, self.referenceImages)
        
        if input_three == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten = self.position_four_input(frame)
            return input_three, input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten
        
    def position_two_input(self, frame):
        position = pos.position_two_output(frame)
        input_two = match.find_match(position, self.referenceImages)
        
        if input_two == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_three, input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten = self.position_three_input(frame)
            return input_two, input_three, input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten
        
    def position_one_input(self, frame):
        position = pos.position_one_output(frame)
        input_one = match.find_match(position, self.referenceImages)
        
        if input_one == self.neutral:
            return self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral, self.neutral
        else:
            input_two, input_three, input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten = self.position_two_input(frame)
            return input_one, input_two, input_three, input_four, input_five, input_six, input_seven, input_eight, input_nine, input_ten
    
    
    
    
    

    
    
    
    
