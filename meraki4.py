import imp


import json
a={"4":5,
   "6":7,
   "1":3,
   "2":4
   }
x=json.dumps(a, indent=4, sort_keys=True)
print(x)



