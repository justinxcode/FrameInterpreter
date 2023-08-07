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
            self.direction_inputs = ref.get_direction_references()
            self.neutral = 'NEUTRAL'
            self.all_neutral = [self.neutral] * 10
            self.results = [self.neutral] * 3
            self.old_result_one = self.all_neutral
            self.old_result_two = self.all_neutral
            self.old_result_three = self.all_neutral
            self.old_result_four = self.all_neutral

    # Row one functions
    def row_one_position_ten_input(self, frame):
        position = pos.row_one_position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs.items())
        return [input_ten]
    
    def row_one_position_nine_input(self, frame):
        position = pos.row_one_position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs.items())

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.row_one_position_ten_input(frame)

    def row_one_position_eight_input(self, frame):
        position = pos.row_one_position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs.items())

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.row_one_position_nine_input(frame)

    def row_one_position_seven_input(self, frame):
        position = pos.row_one_position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs.items())

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.row_one_position_eight_input(frame)

    def row_one_position_six_input(self, frame):
        position = pos.row_one_position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs.items())
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.row_one_position_seven_input(frame)
        
    def row_one_position_five_input(self, frame):
        position = pos.row_one_position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs.items())

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.row_one_position_six_input(frame)
        
    def row_one_position_four_input(self, frame):
        position = pos.row_one_position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs.items())
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.row_one_position_five_input(frame)
        
    def row_one_position_three_input(self, frame):
        position = pos.row_one_position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs.items())
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.row_one_position_four_input(frame)
        
    def row_one_position_two_input(self, frame):
        position = pos.row_one_position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs.items())
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.row_one_position_three_input(frame)
        
    def row_one_position_one_input(self, frame):
        position = pos.row_one_position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs.items())
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.row_one_position_two_input(frame)
        
    # Row two functions
    def row_two_position_ten_input(self, frame):
        position = pos.row_two_position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs.items())
        return [input_ten]
    
    def row_two_position_nine_input(self, frame):
        position = pos.row_two_position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs.items())

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.row_two_position_ten_input(frame)

    def row_two_position_eight_input(self, frame):
        position = pos.row_two_position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs.items())

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.row_two_position_nine_input(frame)

    def row_two_position_seven_input(self, frame):
        position = pos.row_two_position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs.items())

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.row_two_position_eight_input(frame)

    def row_two_position_six_input(self, frame):
        position = pos.row_two_position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs.items())
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.row_two_position_seven_input(frame)
        
    def row_two_position_five_input(self, frame):
        position = pos.row_two_position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs.items())

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.row_two_position_six_input(frame)
        
    def row_two_position_four_input(self, frame):
        position = pos.row_two_position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs.items())
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.row_two_position_five_input(frame)
        
    def row_two_position_three_input(self, frame):
        position = pos.row_two_position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs.items())
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.row_two_position_four_input(frame)
        
    def row_two_position_two_input(self, frame):
        position = pos.row_two_position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs.items())
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.row_two_position_three_input(frame)
        
    def row_two_position_one_input(self, frame):
        position = pos.row_two_position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs.items())
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.row_two_position_two_input(frame)
        
    # Row three functions
    def row_three_position_ten_input(self, frame):
        position = pos.row_three_position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs.items())
        return [input_ten]
    
    def row_three_position_nine_input(self, frame):
        position = pos.row_three_position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs.items())

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.row_three_position_ten_input(frame)

    def row_three_position_eight_input(self, frame):
        position = pos.row_three_position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs.items())

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.row_three_position_nine_input(frame)

    def row_three_position_seven_input(self, frame):
        position = pos.row_three_position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs.items())

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.row_three_position_eight_input(frame)

    def row_three_position_six_input(self, frame):
        position = pos.row_three_position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs.items())
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.row_three_position_seven_input(frame)
        
    def row_three_position_five_input(self, frame):
        position = pos.row_three_position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs.items())

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.row_three_position_six_input(frame)
        
    def row_three_position_four_input(self, frame):
        position = pos.row_three_position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs.items())
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.row_three_position_five_input(frame)
        
    def row_three_position_three_input(self, frame):
        position = pos.row_three_position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs.items())
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.row_three_position_four_input(frame)
        
    def row_three_position_two_input(self, frame):
        position = pos.row_three_position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs.items())
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.row_three_position_three_input(frame)
        
    def row_three_position_one_input(self, frame):
        position = pos.row_three_position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs.items())
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.row_three_position_two_input(frame)
        
    # Row four functions
    def row_four_position_ten_input(self, frame):
        position = pos.row_four_position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs.items())
        return [input_ten]
    
    def row_four_position_nine_input(self, frame):
        position = pos.row_four_position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs.items())

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.row_four_position_ten_input(frame)

    def row_four_position_eight_input(self, frame):
        position = pos.row_four_position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs.items())

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.row_four_position_nine_input(frame)

    def row_four_position_seven_input(self, frame):
        position = pos.row_four_position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs.items())

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.row_four_position_eight_input(frame)

    def row_four_position_six_input(self, frame):
        position = pos.row_four_position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs.items())
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.row_four_position_seven_input(frame)
        
    def row_four_position_five_input(self, frame):
        position = pos.row_four_position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs.items())

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.row_four_position_six_input(frame)
        
    def row_four_position_four_input(self, frame):
        position = pos.row_four_position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs.items())
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.row_four_position_five_input(frame)
        
    def row_four_position_three_input(self, frame):
        position = pos.row_four_position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs.items())
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.row_four_position_four_input(frame)
        
    def row_four_position_two_input(self, frame):
        position = pos.row_four_position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs.items())
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.row_four_position_three_input(frame)
        
    def row_four_position_one_input(self, frame):
        position = pos.row_four_position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs.items())
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.row_four_position_two_input(frame)
        
    # Row five functions
    def row_five_position_ten_input(self, frame):
        position = pos.row_five_position_ten_output(frame)
        input_ten = match.find_match(position, self.button_inputs.items())
        return [input_ten]
    
    def row_five_position_nine_input(self, frame):
        position = pos.row_five_position_nine_output(frame)
        input_nine = match.find_match(position, self.button_inputs.items())

        if input_nine == self.neutral:
            return [self.neutral] * 2
        else:
            return [input_nine] + self.row_five_position_ten_input(frame)

    def row_five_position_eight_input(self, frame):
        position = pos.row_five_position_eight_output(frame)
        input_eight = match.find_match(position, self.button_inputs.items())

        if input_eight == self.neutral:
            return [self.neutral] * 3
        else:
            return [input_eight] + self.row_five_position_nine_input(frame)

    def row_five_position_seven_input(self, frame):
        position = pos.row_five_position_seven_output(frame)
        input_seven = match.find_match(position, self.button_inputs.items())

        if input_seven == self.neutral:
            return [self.neutral] * 4
        else:

            return [input_seven] + self.row_five_position_eight_input(frame)

    def row_five_position_six_input(self, frame):
        position = pos.row_five_position_six_output(frame)
        input_six = match.find_match(position, self.button_inputs.items())
        
        if input_six == self.neutral:
            return [self.neutral] * 5
        else:
            return [input_six] + self.row_five_position_seven_input(frame)
        
    def row_five_position_five_input(self, frame):
        position = pos.row_five_position_five_output(frame)
        input_five = match.find_match(position, self.button_inputs.items())

        if input_five == self.neutral:
            return [self.neutral] * 6
        else:
            return [input_five] + self.row_five_position_six_input(frame)
        
    def row_five_position_four_input(self, frame):
        position = pos.row_five_position_four_output(frame)
        input_four = match.find_match(position, self.button_inputs.items())
        
        if input_four == self.neutral:
            return [self.neutral] * 7
        else:
            return [input_four] + self.row_five_position_five_input(frame)
        
    def row_five_position_three_input(self, frame):
        position = pos.row_five_position_three_output(frame)
        input_three = match.find_match(position, self.button_inputs.items())
        
        if input_three == self.neutral:
            return [self.neutral] * 8
        else:
            return [input_three] + self.row_five_position_four_input(frame)
        
    def row_five_position_two_input(self, frame):
        position = pos.row_five_position_two_output(frame)
        input_two = match.find_match(position, self.button_inputs.items())
        
        if input_two == self.neutral:
            return [self.neutral] * 9
        else:
            return [input_two] + self.row_five_position_three_input(frame)
        
    def row_five_position_one_input(self, frame):
        position = pos.row_five_position_one_output(frame)
        input_one = match.find_match(position, self.all_inputs.items())
        
        if input_one == self.neutral:
            return [self.neutral] * 10
        else:
            return [input_one] + self.row_five_position_two_input(frame)
        
    def majority_true(slef, list):
        number_true = list.count(True)
        return number_true >= len(list) * 0.5
        
    # Get newest inputs
    def get_input(self, frame):
        
        # Store current results
        row_one_result = self.row_one_position_one_input(frame)
        row_two_result = self.row_two_position_one_input(frame)
        row_three_result = self.row_three_position_one_input(frame)
        row_four_result = self.row_four_position_one_input(frame)
        row_five_result = self.row_five_position_one_input(frame)

        bool_list = []
        bool_list.append(self.old_result_one == row_two_result)
        bool_list.append(self.old_result_two == row_three_result)
        bool_list.append(self.old_result_three == row_four_result)
        bool_list.append(self.old_result_four == row_five_result)

        row_changed = self.majority_true(bool_list)

        if row_changed:
            output = row_one_result
        else:
            output = self.all_neutral

        # Set old results with current ones
        self.old_result_one = row_one_result
        self.old_result_two = row_two_result
        self.old_result_three = row_three_result
        self.old_result_four = row_four_result

        return output, bool_list