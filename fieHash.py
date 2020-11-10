"""
计算(大)文件的哈希值 +md5 +sha1
"""
import hashlib
import time


def sha1Value(file, buffer_size=1024):
    sha1 = hashlib.sha1()
    with open(r'%s' % file, 'rb') as f:
        data_buffer = f.read(buffer_size)
        while data_buffer:
            sha1.update(data_buffer)
            data_buffer = f.read(buffer_size)
    return sha1.hexdigest()


def md5Value(file, buffer_size=1024):
    md5 = hashlib.md5()
    time = 0
    with open(r'%s' % file, 'rb') as f:
        data_buffer = f.read(buffer_size)
        while data_buffer:
            md5.update(data_buffer)
            time += 1
            data_buffer = f.read(buffer_size)
    print('md5 time: %s' % time)
    return md5.hexdigest()


if __name__ == '__main__':
    file_path = input('please input your file path')
    begin = time.clock()
    sha1_str = sha1Value(file_path)
    print(sha1_str)
    time1 = time.clock()
    sha1_time = time1 - begin
    print(sha1_time)
    md5_str = md5Value(file_path)
    print(md5_str)
    md5_time = time.clock() - time1
    print(md5_time)



