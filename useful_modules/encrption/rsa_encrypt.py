from Crypto.PublicKey import RSA
from Crypto import Random


INPUT_SIZE = 1024


# RSA私钥和公钥的生成
def rsa_generate_keypair():
    random_func = Random.new().read                   # 产生随机的函数
    key_pair = RSA.generate(INPUT_SIZE, random_func)  # 生成密钥对
    private_pem = key_pair.exportKey()                # 获取PEM格式的私钥
    public_pem = key_pair.publickey().exportKey()                 # 获取PEM格式的公钥
    print("私钥：%s" % private_pem)                                # 输出私钥
    print("公钥：%s" % public_pem)                                 # 输出公钥
    return public_pem, private_pem


PUBLIC_KEY_PEM, PRIVATE_KEY_PEM = rsa_generate_keypair()
DATA = b"Hello, world!"


# 用公钥加密
def rsa_encrypt():
    random_func = Random.new().read
    public_key = RSA.importKey(PUBLIC_KEY_PEM)         # 输入PEM格式的公钥并获取RSA对象
    encrypted = public_key.encrypt(DATA, random_func)  # 加密数据
    print("加密后的数据：%s" % encrypted)                 # 输出加密后的数据
    return encrypted


ENCRYPT_DATA = rsa_encrypt()


def decrypt():
    private_key = RSA.importKey(PRIVATE_KEY_PEM)
    decrypted = private_key.decrypt(ENCRYPT_DATA)
    print("解密后的数据：%s" % decrypted.decode("utf-8", errors="ignore"))


decrypt()
