import hashlib
import time
import random
import string
from urllib.parse import quote


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # 将得到的MD5值所以字符转换成大写
    return m.hexdigest().upper()


def get_params(group_id):
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    # 应用标志，这里修改成自己的 id 和 key
    app_id = '2117292455'
    app_key = 'VjOCJEchO0wGwuis'

    params = {'app_id': app_id,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'group_id': group_id,
              }
    sign_before = ''
    # 要对 key 排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以 app_key 为键名，拼接到字符串 sign_before 末尾
    sign_before += 'app_key={}'.format(app_key)


    # 对字符串sign_before进行MD5运算，得到接口请求
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params
