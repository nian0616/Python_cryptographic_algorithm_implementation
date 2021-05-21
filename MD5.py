#MD5 消息摘要算法，密码散列函数，产生出128位的散列值
import hashlib
m = hashlib.md5()
m.update(str.encode("utf8"))
print(m.hexdigest())