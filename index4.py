import io
from functools import partial, wraps
from typing import TextIO, Callable

def write_file(file_name,ndung):
    f = io.open(file_name, 'w', encoding='utf-8')
    f.write(ndung)
    f.close()


def chunked_file_reader(fp, block_size = 1024 * 1024*1024*2):
    for chunk in iter(partial(fp.read, block_size), ''):
        yield chunk


def read_file(file_path):
    data = ''
    count: int = 0
    with open(file_path,encoding="utf8") as f_read:
        for chunk in chunked_file_reader(f_read):
            count += 1
            print(count)
            # print(chunk)
            data+=chunk
    # return count
    return data

# data = read_file('keyword_planidea_law.json')
data = read_file('keyword_planidea_amz.json')

import json
L_data = json.loads(data)
L_keywordPlanner = []
for e in L_data:
    L_keywordPlanner+=e['KeywordsPlanner']

L_keywordPlanner = list(map(lambda x:{
    "Text": x['Text'],
    "AvgMonthlySearches": x['AvgMonthlySearches'],
},L_keywordPlanner))



L_keywordPlanner = sorted(L_keywordPlanner,key = lambda x:x['AvgMonthlySearches'])

L_keywordPlanner = [
    {
        "Text":e["Text"],
        "AvgMonthlySearches":e["AvgMonthlySearches"],
        "_id":index+9801
    }
    for (index,e) in enumerate(L_keywordPlanner)
]


write_file("file_name.json",json.dumps(L_keywordPlanner))