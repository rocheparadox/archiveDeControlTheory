#Author : Roche Christopher
#File created on 8/7/19 9:27 PM

import time
import plotly
import plotly.graph_objs as obj

from pid import PID

#gains

p_gain = 1
i_gain = 0
d_gain = 0

#Number of cycles to run the PID algo
cycles = 30

#problem specific variables
gas_pedal_force = 0
required_velocity = 400


pidObj = PID(0.1,0.3,0.0)
velocity_list = []
cycle_list = []

def calculate_velocity(gas_pedal_force):
    # let us assume that the gas_pedal_force is propotional to the velocity of the vehicle
    return int(gas_pedal_force * 3)


for cycle in range(cycles):

    present_velocity = calculate_velocity(gas_pedal_force)
    #print(present_velocity)
    cycle_list.append(cycle)
    velocity_list.append(present_velocity)

    gas_pedal_force = pidObj.compute(required_velocity, present_velocity)



trace = obj.Scatter(
    x=cycle_list,
    y=velocity_list
)

data = [trace]
plotly.offline.plot(data, auto_open=True)

