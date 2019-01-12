
myfile = open("file.txt","w")

N = 9;
M = 12


myfile.write("\n\n")
# South
for i in range(1,N):
  for j in range(1,M):
#    myfile.write("  planner.addAction(\"moveSouth_x_%d_y_%d()\", \n\t\t {\"At(x_%d,y_%d)\"}, \n\t\t {\"At(x_%d,y_%d)\", \"~At(x_%d,y_%d)\"});\n" %(i, j, i, j, i, (j-1), i, j))
    myfile.write("  planner.setActionCost(\"moveSouth_x_%d_y_%d()\", 1);\n" %(i, j))


myfile.write("\n\n")
# North
for i in range(1,N):
  for j in range(1,M):
#    myfile.write("  planner.addAction(\"moveNorth_x_%d_y_%d()\", \n\t\t {\"At(x_%d,y_%d)\"}, \n\t\t {\"At(x_%d,y_%d)\", \"~At(x_%d,y_%d)\"});\n" %(i, j, i, j, i, (j+1), i, j))
    myfile.write("  planner.setActionCost(\"moveNorth_x_%d_y_%d()\", 1);\n" %(i, j))

myfile.write("\n\n")
# East
for i in range(1,N):
  for j in range(1,M):
#    myfile.write("  planner.addAction(\"moveEast_x_%d_y_%d()\", \n\t\t {\"At(x_%d,y_%d)\"}, \n\t\t {\"At(x_%d,y_%d)\", \"~At(x_%d,y_%d)\"});\n" %(i, j, i, j, (i+1), j, i, j))
    myfile.write("  planner.setActionCost(\"moveEast_x_%d_y_%d()\", 1);\n" %(i, j))

myfile.write("\n\n")
# West
for i in range(1,N):
  for j in range(1,M):
#    myfile.write("  planner.addAction(\"moveWest_x_%d_y_%d()\", \n\t\t {\"At(x_%d,y_%d)\"}, \n\t\t {\"At(x_%d,y_%d)\", \"~At(x_%d,y_%d)\"});\n" %(i, j, i, j, (i-1), j, i, j))
    myfile.write("  planner.setActionCost(\"moveWest_x_%d_y_%d()\", 1);\n" %(i, j))




 
myfile.close()

