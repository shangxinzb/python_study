import redis


r = redis.Redis('localhost', 6379)
r.set('name', 'cmps')
print(r.get('name'))




