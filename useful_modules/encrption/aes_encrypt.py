from Crypto.Cipher import AES


KEY = "testtesttesttest"   # 加密和解密时使用的通用密码
DATA = "0123456789012345"  # 数据长度为16的倍数


def rsa_generate_keypair():
    aes = AES.new(KEY)                        # 生成AES类的实例
    encrypt_data = aes.encrypt(DATA)          # 加密
    print(repr(encrypt_data))                 # 输出加密状态的数据
    decrypt_data = aes.decrypt(encrypt_data)  # 解密
    print(repr(decrypt_data))                 # 输出二进制串解密后还原的数据


main()
