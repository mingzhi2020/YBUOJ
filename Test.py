import hashlib

md5 = hashlib.md5()
md5.update('Hsy123456'.encode('utf-8'))
print(md5.hexdigest())
md5 = hashlib.md5()
md5.update('Hsy123456'.encode('utf-8'))
print(md5.hexdigest())
