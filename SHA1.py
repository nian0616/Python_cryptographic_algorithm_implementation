# SHA1加密,安全哈希算法,对于长度小于2^ 64位的消息，SHA1会产生一个160位的消息摘要
import hashlib
sha1 = hashlib.sha1()
data = '2333333'
sha1.update(data.encode('utf-8'))
sha1_data = sha1.hexdigest()
print(sha1_data)