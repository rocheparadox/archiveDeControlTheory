#Author : Roche Christopher
#File created on 8/7/19 9:27 PM

import time
import plotly
import plotly.graph_objs as obj
from classical_pid import CLASSICAL_PID
from pid import PID

#gains

p_gain = 1
i_gain = 0
d_gain = 0

#Number of cycles to run the PID algo
cycles = 200

#problem specific variables
gas_pedal_force = 0
required_velocity = 700
show_graph=True
#show_graph=False


pidObj = CLASSICAL_PID(0.28,4.6,0)
velocity_list = []
cycle_list = []

def calculate_velocity(gas_pedal_force):
    # let us assume that the gas_pedal_force is proportional to the velocity of the vehicle
    return int(gas_pedal_force * 3)


for cycle in range(cycles):

    present_velocity = calculate_velocity(gas_pedal_force)
    print(present_velocity)
    cycle_list.append(cycle)
    velocity_list.append(present_velocity)

    gas_pedal_force = pidObj.compute_outpu(required_velocity, present_velocity)


if show_graph:
    control_siganl = obj.Scatter(
        x=cycle_list,
        y=velocity_list
    )

    target = obj.Scatter(
        x=cycle_list,
        y=[required_velocity for i in range(cycles)]
    )

    data = [control_siganl, target]
    plotly.offline.plot(data, auto_open=True)

