import time
import json

  
start = time.time()
count = 0
data = ''
with open("keyword_planidea_law.json") as file:
    for line in file:
        print(count)
        data+=line
        count = count + 1
end =  time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)


L_data = json.loads(data)

L_keywordPlanner = []
for e in L_data:
    L_keywordPlanner+=e['KeywordsPlanner']

