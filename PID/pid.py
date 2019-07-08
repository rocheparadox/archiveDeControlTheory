#Author : Roche Christopher
#File created on 8/7/19 9:00 PM

class PID:

    def __init__(self, proportional_gain_constant, integral_gain_constant, differential_gain_constant):
        self.proportional_gain_constant = proportional_gain_constant
        self.integral_gain_constant = integral_gain_constant
        self.differential_gain_constant = differential_gain_constant
        self.previous_error = 0
        self.integral_error = 0

    def compute(self, set_point, present_value):

        #calculate errors
        present_error = set_point - present_value
        proportional_error = present_error
        self.integral_error = (self.integral_error + present_error)
        differential_error = (present_error - self.previous_error)
        self.previous_error = present_error

        #calculate PID algo output
        pid_output = (proportional_error * self.proportional_gain_constant) + \
                     (self.integral_error * self.integral_gain_constant) + \
                     (differential_error * self.differential_gain_constant)

        return pid_output
