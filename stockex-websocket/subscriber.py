import redis
# connect with redis server as Bob
r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
# subscribe to classical music
p.subscribe('classical_music')

print(p.get_message()['data'])