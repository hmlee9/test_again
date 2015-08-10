# -*- coding:utf-8 -*-
from qiniu import Auth, put_file

access_key = 'kzy0EaJo3HeR8eMyaNNGTRs00-9McxP2Mm2djRXO'
secret_key = 'Zzd20NkqreFqfHZIq7dZsapeik8WO4PzbHQlnYD-'
bucket_name = 'xiaohua'


q = Auth(access_key, secret_key)

localfile = '/root/workspace/test/fanbb.jpg'
key = '_fanbb.jpg'
mime_type = "image/jpeg"

token = q.upload_token(bucket_name, key)
ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
print(info)
