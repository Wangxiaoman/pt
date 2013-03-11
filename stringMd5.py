'''
Created on 2013-3-8

@author: wang_xm


import hashlib   

src = 'teststring'
print (hashlib.md5(src).hexdigest().upper())
'''

import redis
redis_ip = "123.58.176.61"
redis_port =6379
redis_db = 0
rcon = redis.StrictRedis(host=redis_ip, port=redis_port, db=redis_db)
key = 'm_install_QFy4DsD65K_507b5afad008bbbc8cf07eff58377d52'

print(key)
print(rcon)
print(rcon.hmget(key, "mac")[0])