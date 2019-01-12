
[INPUT]
o1_y:8...8
o1_x:1...3
o2_y:6...6
o2_x:6...8
o3_y:3...3
o3_x:5...7

a_x: 0...9
a_y: 0...12

visited_1:0...1
visited_2:0...1
visited_3:0...1
visited_4:0...1

cost:0...70

#batteryAction:0...1
#battery:0...31

[OUTPUT]

#0 = no motion, 1 = North, 2 = East, 3 = South, 4 = West
action:0...4



[SYS_INIT]

#direction = 0

[ENV_INIT]
o1_x = 1
o2_x = 8
o3_x = 5

a_x = 4
a_y = 11

visited_1 = 0
visited_2 = 0
visited_3 = 0
visited_4 = 0

[SYS_TRANS]

a_x' != 0
a_y' != 0
a_x' != 9 
a_y' != 12
#battery' >= 8

!(a_x' = 1 & a_y' = 2)
!(a_x' = 2 & a_y' = 2)
!(a_x' = 3 & a_y' = 2)
!(a_x' = 4 & a_y' = 2)

!(a_x' = 4 & a_y' = 3)
!(a_x' = 4 & a_y' = 4)
!(a_x' = 4 & a_y' = 5)
!(a_x' = 4 & a_y' = 6)
!(a_x' = 4 & a_y' = 7)

!(a_x' = o1_x & a_y' = o1_y)
!(a_x' = o1_x' & a_y' = o1_y')
#!(a_x = o1_x' & a_y = o1_y')

!(a_x' = o2_x & a_y' = o2_y)
!(a_x' = o2_x' & a_y' = o2_y')
#!(a_x = o2_x' & a_y = o2_y')

!(a_x' = o3_x & a_y' = o3_y)
!(a_x' = o3_x' & a_y' = o3_y')
#!(a_x = o3_x' & a_y = o3_y')



[SYS_LIVENESS]
#a_x' = 3 & a_y' = 3
#a_x' = 2 & a_y' = 1
#a_x' = 6 & a_y' = 5
#a_x' = 7 & a_y' = 9

(visited_1 = 1) & (visited_2 = 1) & (visited_3 = 1) & (visited_4 = 1)
#cost' <= 30
[ENV_TRANS]

(action = 0) -> ((a_x' = a_x) & (a_y' = a_y))

(action = 1) -> ((a_y' = a_y + 1) & (a_x' = a_x) & (cost' = cost + 1)) 
(action = 2) -> ((a_x' = a_x + 1) & (a_y' = a_y) & (cost' = cost + 1))
(action = 3) -> ((a_y' + 1 = a_y) & (a_x' = a_x) & (cost' = cost + 1))
(action = 4) -> ((a_x' + 1 = a_x) & (a_y' = a_y) & (cost' = cost + 1))

((a_x = 4) & (a_y = 11) -> (cost' = 0))

(a_x = 2 & a_y = 1) <-> (visited_1' = 1)
(a_x = 3 & a_y = 3) <-> (visited_2' = 1)
(a_x = 6 & a_y = 5) <-> (visited_3' = 1)
(a_x = 7 & a_y = 9) <-> (visited_4' = 1)

(visited_1 = 1) -> (visited_1' = 1)
(visited_2 = 1) -> (visited_2' = 1)
(visited_3 = 1) -> (visited_3' = 1)
(visited_4 = 1) -> (visited_4' = 1)

(o1_x = 2) -> (o1_x' != 2)
(o1_x != 2) -> (o1_x' = 2)

#(o1_x' = 1)


[ENV_LIVENESS]

(o1_x = 1)


