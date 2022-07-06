import json
import io

def read_file(file_name):
    # f = io.open(file_name, 'r', encoding='utf-8')
    f = io.open(file_name, 'r')
    ndung=f.read()
    f.close()
    return ndung

def write_file(file_name,ndung):
    f = io.open(file_name, 'w', encoding='utf-8')
    f.write(ndung)
    f.close()


data = read_file('keyword_planidea_amz.json')
# data = json.loads(read_file('keyword_planidea_amz.json'))
# data = data['data']

# data = sorted(data,key = lambda x:-x['age'])




# data = {
#     "data":[
#         {
#             "name":"nghiahsgs",
#             "age":10
#         },
#         {
#             "name":"nghiahsgs",
#             "age":20
#         },
#         {
#             "name":"nghiahsgs",
#             "age":11
#         }
#     ]
# }
# write_file("data.json",json.dumps(data))



# L_keywordPlanner = []
# for e in L_data:
#     L_keywordPlanner+=e['KeywordsPlanner']

