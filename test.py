import redis
import json
import string
r = redis.StrictRedis()
pubsub = r.pubsub()
pubsub.psubscribe('__keyevent@0__:expired')
for msg in pubsub.listen():
  print msg['data']
