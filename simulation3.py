
import json
import random
import time
from environment import Simulation
from time import sleep

def print_info(node):
#    time = node['state'][19]*2**4 + node['state'][18]*2**3\
#          + node['state'][17]*2**2 + node['state'][16]*2**1 + node['state'][15]*2**0
##    controller = node['state'][20]*2**1 + node['state'][19]*2**0
##    direction = node['state'][23]*2**2 + node['state'][22]*2**1 + node['state'][21]*2**0
#    action = node['state'][23]*2**3 + node['state'][22]*2**2 + node['state'][21]*2**1 + node['state'][20]*2**0
##    print ('time: ', time, "direction ", direction, "controller:", controller)
#    print ('time: ', time, "action", action)

    visited_1 = node['state'][14]
    visited_2 = node['state'][15]
    visited_3 = node['state'][16]
    visited_4 = node['state'][17]
    step = node['state'][23]*2**5 + node['state'][22]*2**4 + node['state'][21]*2**3\
    + node['state'][20]*2**2 + node['state'][19]*2**1 + node['state'][18]*2**0 
    action = node['state'][27]*2**3 + node['state'][26]*2**2 + node['state'][25]*2**1 + node['state'][24]*2**0
    print ("visited_1: ", visited_1, "visited_2: ", visited_2, "visited_3: ", visited_3, "visited_4: ", visited_4, "step: ", step, "action: ", action)


def get_o1_state(node):
    return (1 + node['state'][1]*(2**1) + node['state'][0]*(2**0), 8)

def get_o2_state(node):
    return (6 + node['state'][3]*(2**1) + node['state'][2]*(2**0), 6)

def get_o3_state(node):
    return (5 + node['state'][5]*(2**1) + node['state'][4]*(2**0), 3)

def get_a_state(node):
    a_x = node['state'][9]*2**3 + node['state'][8]*2**2 + node['state'][7]*2**1\
           + node['state'][6]*2**0
    a_y = node['state'][13]*2**3 + node['state'][12]*2**2 + node['state'][11]*2**1\
           + node['state'][10]*2**0
    return (a_x, a_y)

def get_a_state_goap(action,a_x,a_y):
    print action
    print a_x
    print a_y
    if action == 1:
       a_y = a_y+1
    elif action == 2:
       a_x = a_x+1  
    elif action == 3:
       a_x = a_x-1  
    elif action == 4:
       a_y = a_y-1  
    return (a_x, a_y)

def get_action(step):
#    action_stack = [4,4,4,3,4,4,4,4,4,6,1,1,1,1,1,1,2,2,2,2,8,4,4,4,4,3,7,4,4,4,4,3,3,3,3,5]
    action_stack = [4,4,2,2,2,8,4,3,3,3,3,4,4,4,4,4,6,1,1,1,1,1,2,2,4,4,4,2,7,4,2,2,4,4,4,3,3,3,3,3,3,5]
#    action_stack = [4,4,2,2,2,8,4,4,3,3,4,4,2,7,4,2,2,4,4,4,3,3,3,3,3,3,5]
#    if step < len(action_stack):
    return action_stack[step]
#    else:
#       return 0

#with open('simulation.json') as f:
#    data = json.load(f)

with open('GOAPvsADLnE.json') as f:
    data = json.load(f)

nodes = data['nodes']

sim = Simulation('simulation.config')
sim.draw()
cur_state = sim.get_state()
current_node = nodes['0']

a_state_pos = (cur_state['agents'][0])
o1_state_pos = (cur_state['moving_obstacles'][0])
o2_state = (cur_state['moving_obstacles'][1])
step = 0;
while True:
    trans = current_node['trans']
    index = str(random.choice(trans))
    current_node = nodes[index]
    next_o1_state_pos = get_o1_state(current_node)
    next_o2_state_pos = get_o2_state(current_node)
    next_o3_state_pos = get_o3_state(current_node)
    next_a_state_pos = get_a_state(current_node)
#    action = get_action(step)
#    next_a_state_pos = get_a_state_goap(action,a_state_pos[0],a_state_pos[1])
    print ((a_state_pos == o1_state_pos) | (next_a_state_pos == o1_state_pos))
    sim.agent_move(0, next_a_state_pos)
    sim.draw()
    sleep(0.5)
    sim.obstacle_move(0, next_o1_state_pos)
    sim.obstacle_move(1, next_o2_state_pos)
    sim.obstacle_move(2, next_o3_state_pos)
    print_info(current_node)
    a_state_pos = next_a_state_pos
    o1_state_pos = next_o1_state_pos
    o2_state_pos = next_o2_state_pos
    o3_state_pos = next_o3_state_pos
    sim.draw()
    sleep(0.5)
    print step
    step = step+1
