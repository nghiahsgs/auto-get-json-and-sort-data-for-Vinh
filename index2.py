# import module
import fileinput
import time
  
#time at the start of program is noted
start = time.time()
  
#keeps a track of number of lines in the file
count = 0
data = ""
for lines in fileinput.input(['data.json']):
    # print(lines)
    data+=lines
    count = count + 1


    