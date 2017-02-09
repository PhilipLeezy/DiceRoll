import json

p1 = json.dumps({'Int': 10, 'Str': 7}, sort_keys=True,
  indent=4, separators=(',', ': '))
