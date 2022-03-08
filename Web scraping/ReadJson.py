
# this is my json
stringOfJsonData = '{"name" : "Sneha Mathadawar","details" : "csjgfusgdfuy"  }'

import json
jsonObj = json.loads(stringOfJsonData)
print(jsonObj)

# TO READ JSON WITH LOADS() METHOD
# 1] consider variable which holds the json data
# 2] import json module
# 3] create json object
# 4] reading json data