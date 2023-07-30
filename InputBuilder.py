from References import References
from IconFinder import IconPositions
from IconMatch import IconMatch

ref = References()
pos = IconPositions()
match = IconMatch()

class InputBuilder:
    def __init__(self):
            self.all_inputs = ref.get_all_references()
            self.button_inputs = ref.get_button_references()
            self.neutral = 'NEUTRAL'

    def position_ten_input(self, frame):
        position = pos.position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs)
        return [input_ten]
    
    def position_nine_input(self, frame):
        position = pos.position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs)

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.position_ten_input(frame)

    def position_eight_input(self, frame):
        position = pos.position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs)

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.position_nine_input(frame)

    def position_seven_input(self, frame):
        position = pos.position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs)

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.position_eight_input(frame)

    def position_six_input(self, frame):
        position = pos.position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs)
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.position_seven_input(frame)
        
    def position_five_input(self, frame):
        position = pos.position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs)

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.position_six_input(frame)
        
    def position_four_input(self, frame):
        position = pos.position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs)
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.position_five_input(frame)
        
    def position_three_input(self, frame):
        position = pos.position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs)
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.position_four_input(frame)
        
    def position_two_input(self, frame):
        position = pos.position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs)
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.position_three_input(frame)
        
    def position_one_input(self, frame):
        position = pos.position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs)
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.position_two_input(frame)
    
    
    
    
    

    
    
    
    
