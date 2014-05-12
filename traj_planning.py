import quadrotor.command as cmd
from math import sqrt

# Create a list of motion commands using the following functions defined in the quadrotor.command package.

# forward(x) - move x meters forward
# backward(x) - move x meters backward
# left(x) - move x meters to the left
# right(x) - move x meters to the right
# up(x) - move x meters up
# down(x) - move x meters down
# turn_left(x) - turn x degrees to the left
# turn_right(x) - turn x degrees to the right

def plan_mission(mission):

    # this is an example illustrating the different motion commands,
    # replace them with your own commands and activate all beacons
    commands  = [
        cmd.up(1),
        cmd.forward(5),
        cmd.right(2),
        cmd.backward(4),
        cmd.left(4),
        cmd.forward(5),
        
        # cmd.turn_left(45),
        # cmd.forward(sqrt(2)),
        # cmd.turn_right(45),
        # cmd.right(1),
        # cmd.turn_left(45),
        # cmd.forward(sqrt(0.5)),
        # cmd.turn_left(90),
        # cmd.forward(sqrt(0.5)),
        # cmd.turn_left(45),
        # cmd.forward(1),
        # cmd.turn_right(45),
        # cmd.backward(sqrt(2)),
        # cmd.turn_left(45),
        # cmd.forward(1),
    ]

    mission.add_commands(commands)
