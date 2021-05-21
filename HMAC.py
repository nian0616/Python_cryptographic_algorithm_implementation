# HMAC加密,散列消息鉴别码,基于加密hash函数和共享密钥。实现原理是用公开函数和密钥产生一个固定长度的值作为认证标识
import hmac
import hashlib
# 第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数
mac = hmac.new('key','hello',hashlib.md5)
mac.digest()  # 字符串的ascii格式
mac.hexdigest()  # 加密后字符串的十六进制格式