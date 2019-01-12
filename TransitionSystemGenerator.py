
myfile = open("file.txt","w")

N = 11;

myfile.write("\n\n")
# direction = 1, controller=0
for i in range(1,N):
  for j in range(1,N):
    myfile.write("(direction=1 & controller=0 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, i, (j+1)))


myfile.write("\n\n")
# direction = 2, controller=0
for i in range(1,N):
  for j in range(1,N):
    myfile.write("(direction=2 & controller=0 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, (i+1), j))


myfile.write("\n\n")
# direction = 3, controller=0
for i in range(1,N):
  for j in range(1,N):
    myfile.write("(direction=3 & controller=0 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, i, (j-1)))


myfile.write("\n\n")
# direction = 4, controller=0
for i in range(1,N):
  for j in range(1,N):
    myfile.write("(direction=4 & controller=0 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, (i-1), j))


myfile.write("\n\n")
# direction = 1, controller=1
for i in range(1,N):
  for j in range(1,N):
    if ((j<N-2) & (i>=1) & (i<=N-1)):
      myfile.write("(direction=1 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & ((a_x'=%d) | (a_x'=%d) | (a_x'=%d)))\n" %(i, j, (j+3), i, (i+1), (i-1)))
    else:
      myfile.write("(direction=1 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, N, i))


myfile.write("\n\n")
# direction = 2, controller=1
for i in range(1,N):
  for j in range(1,N):
    if ((i<N-2) & (j>=1) & (j<=N-1)):
      myfile.write("(direction=2 & controller=1 & a_x=%d & a_y=%d) -> ((a_x'=%d) & ((a_y'=%d) | (a_y'=%d) | (a_y'=%d)))\n" %(i, j, (i+3), j, (j+1), (j-1)))
    else:
      myfile.write("(direction=2 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, N))


myfile.write("\n\n")
# direction = 3, controller=1
for i in range(1,N):
  for j in range(1,N):
    if ((j>2) & (i>=1) & (i<=N-1)):
      myfile.write("(direction=3 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & ((a_x'=%d) | (a_x'=%d) | (a_x'=%d)))\n" %(i, j, (j-3), i, (i+1), (i-1)))
    else:
      myfile.write("(direction=3 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, 0, i))


myfile.write("\n\n")
# direction = 4, controller=1
for i in range(1,N):
  for j in range(1,N):
    if ((i>2) & (j>=1) & (j<=N-1)):
      myfile.write("(direction=4 & controller=1 & a_x=%d & a_y=%d) -> ((a_x'=%d) & ((a_y'=%d) | (a_y'=%d) | (a_y'=%d)))\n" %(i, j, (i-3), j, (j+1), (j-1)))
    else:
      myfile.write("(direction=4 & controller=1 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, 0))


myfile.write("\n\n")
# direction = 1, controller=2
for i in range(1,N):
  for j in range(1,N):
    if ((j<N-3) & (i>=2) & (i<=N-2)):
      myfile.write("(direction=1 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & ((a_x'=%d) | (a_x'=%d) | (a_x'=%d) | (a_x'=%d) | (a_x'=%d)))\n" %(i, j, (j+4), (i-2), (i-1), i, (i+1), (i+2)))
    elif(j>=N-3):
      myfile.write("(direction=1 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, N, i))
    elif(i<2):
      myfile.write("(direction=1 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, 0))
    else:
      myfile.write("(direction=1 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, N))


myfile.write("\n\n")
# direction = 2, controller=2
for i in range(1,N):
  for j in range(1,N):
    if ((i<N-3) & (j>=2) & (j<=N-2)):
      myfile.write("(direction=2 & controller=2 & a_x=%d & a_y=%d) -> ((a_x'=%d) & ((a_y'=%d) | (a_y'=%d) | (a_y'=%d) | (a_y'=%d) | (a_y'=%d)))\n" %(i, j, (i+4), (j-2), (j-1), j, (j+1), (j+2)))
    elif(i>=N-3):
      myfile.write("(direction=2 & controller=2 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, N, j))
    elif(j<2):
      myfile.write("(direction=2 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, 0, i))
    else:
      myfile.write("(direction=2 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, N, i))


myfile.write("\n\n")
# direction = 3, controller=2
for i in range(1,N):
  for j in range(1,N):
    if ((j>3) & (i>=2) & (i<=N-2)):
      myfile.write("(direction=3 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & ((a_x'=%d) | (a_x'=%d) | (a_x'=%d) | (a_x'=%d) | (a_x'=%d)))\n" %(i, j, (j-4), (i-2), (i-1), i, (i+1), (i+2)))
    elif(j<=3):
      myfile.write("(direction=3 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, 0, i))
    elif(i<2):
      myfile.write("(direction=3 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, 0))
    else:
      myfile.write("(direction=3 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, j, N))


myfile.write("\n\n")
# direction = 4, controller=2
for i in range(1,N):
  for j in range(1,N):
    if ((i>3) & (j>=2) & (j<=N-2)):
      myfile.write("(direction=4 & controller=2 & a_x=%d & a_y=%d) -> ((a_x'=%d) & ((a_y'=%d) | (a_y'=%d) | (a_y'=%d) | (a_y'=%d) | (a_y'=%d)))\n" %(i, j, (i-4), (j-2), (j-1), j, (j+1), (j+2)))
    elif(i<=3):
      myfile.write("(direction=4 & controller=2 & a_x=%d & a_y=%d) -> ((a_x'=%d) & (a_y'=%d))\n" %(i, j, 0, j))
    elif(j<2):
      myfile.write("(direction=4 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, 0, i))
    else:
      myfile.write("(direction=4 & controller=2 & a_x=%d & a_y=%d) -> ((a_y'=%d) & (a_x'=%d))\n" %(i, j, N, i))

 
myfile.close()

