
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
#    print ("visited_1: ", visited_1, "visited_2: ", visited_2, "visited_3: ", visited_3, "visited_4: ", visited_4, "step: ", step, "action: ", action)


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
#    print action
#    print a_x
#    print a_y
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
    if step < len(action_stack):
       return action_stack[step]
    else:
       return 0

#with open('simulation.json') as f:
#    data = json.load(f)
def simulate(sim,data,nodes):
   collision = 0
#   with open('GOAPvsADLnE.json') as f:
#      data = json.load(f)

#   nodes = data['nodes']

#   sim = Simulation('simulation.config')

   sim.draw()
   cur_state = sim.get_state()
   current_node = nodes['0']

#   a_state_pos = (cur_state['agents'][0])
   a_state_pos = [4,11]
   o1_state_pos = (cur_state['moving_obstacles'][0])
   o2_state = (cur_state['moving_obstacles'][1])
   spatial_step = 0;
   time_step = 0;
   interrupt = 0;
   action_step = 0;
   while True:
      trans = current_node['trans']
      index = str(random.choice(trans))
      current_node = nodes[index]
      next_o1_state_pos = get_o1_state(current_node)
      next_o2_state_pos = get_o2_state(current_node)
      next_o3_state_pos = get_o3_state(current_node)
      next_a_state_pos = get_a_state(current_node)
#      action = get_action(action_step)
#      next_a_state_pos = get_a_state_goap(action,a_state_pos[0],a_state_pos[1])
      action_step = action_step+1
      if (next_a_state_pos != a_state_pos):
         if (a_state_pos == o1_state_pos):
            collision = 1
            sim.agent_move(0, next_a_state_pos)
            a_state_pos = next_a_state_pos
            spatial_step = spatial_step+1
    
         elif (next_a_state_pos == o1_state_pos):
            interrupt = interrupt+1
            action_step = action_step - 1
    
         else:
            spatial_step = spatial_step+1
            sim.agent_move(0, next_a_state_pos)
            a_state_pos = next_a_state_pos

      sim.draw()
      sleep(0.1)
      sim.obstacle_move(0, next_o1_state_pos)
      sim.obstacle_move(1, next_o2_state_pos)
      sim.obstacle_move(2, next_o3_state_pos)
      print_info(current_node)
      o1_state_pos = next_o1_state_pos
      o2_state_pos = next_o2_state_pos
      o3_state_pos = next_o3_state_pos
      sim.draw()
      sleep(0.1)
#      print step
      time_step = time_step+1
#      print ('collision: ' , collision)
#      print ('interrupt: ' , interrupt)
#      print ('a_state', a_state_pos, 'o1_state', o1_state_pos, 'o2_state', o2_state_pos, 'o3_state', o3_state_pos)
#   f.close()
#   return (time_step, spatial_step, collision, interrupt)
      if (a_state_pos == (2,1)):
         f.close()
         return (time_step, spatial_step, collision, interrupt)



collisions = 0
interrupts = 0
maximum_time_steps = 0
maximum_spatial_steps = 0
total_time_steps = 0
total_spatial_steps = 0
with open('GOAPvsADLnE.json') as f:
   data = json.load(f)
nodes = data['nodes']
sim = Simulation('simulation.config')
for i in range(1,11):
#   collisions = collisions + simulate()
   result = simulate(sim,data,nodes)
   print i
   print result
   collisions = collisions + result[2]
   interrupts = interrupts + result[3]
   total_time_steps = total_time_steps + result[0]
   total_spatial_steps = total_spatial_steps + result[1]

   if (maximum_spatial_steps < result[1]):
      maximum_spatial_steps = result[1]
       
   if (maximum_time_steps < result[0]):
      maximum_time_steps = result[0]


print ('collisions; ', collisions, 'interrupts: ', interrupts, 'maximum_time_steps: ', maximum_time_steps, 'average_time_steps: '\
, total_time_steps/1000.0, 'maximum_spatial_steps: ', maximum_spatial_steps, 'average_spatial_steps: ', total_spatial_steps/1000.0)


