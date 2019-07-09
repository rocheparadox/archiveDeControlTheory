#Author : Roche Christopher
#File created on 9/7/19 6:47 AM

# classic pid equation is fetched from the below file
# https://www.cds.caltech.edu/~murray/courses/cds101/fa02/caltech/astrom-ch6.pdf
# equation 6.1


class CLASSICAL_PID:

    def __init__(self, proportional_gain, intergral_time, differential_time):
        self.proportional_gain=proportional_gain
        self.intergral_time=intergral_time
        self.differential_time=differential_time
        self.previous_error=0
        self.integral_error_sum=0

    def compute_output(self, set_point, measured_value):

        present_error = set_point - measured_value

        proportional_term=present_error
        differential_term=(present_error - self.previous_error)*self.differential_time
        if self.intergral_time == 0:
            integral_term = 0
        else:
            # update self.integral_error_sum
            self.integral_error_sum = self.integral_error_sum + present_error
            integral_term=self.integral_error_sum/self.intergral_time


        #update the previous error
        self.previous_error = present_error

        pid_output = (proportional_term + integral_term + differential_term) * self.proportional_gain

        return pid_output
