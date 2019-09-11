'''
Reference:
    - https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
    - https://docs.python-guide.org/scenarios/serialization/
'''
import pickle

def object_to_bytes_to_file():
    # let the object -> bytes -> write into the file. (把變數從記憶體轉變成可儲存或傳輸的過程，稱之序列化。)
    d = dict(name='george', age=20, score=88)

    # object -> bytes.
    res = pickle.dumps(d)
    print(res) # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00georgeq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'

    # bytes -> write into the file.
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()

def improve():
    ''' improve the function of object_to_bytes_to_file.'''
    d = dict(name='george', age=20, score=88)

    improved_f = open('dump1.txt', 'wb')
    pickle.dump(d, improved_f)
    improved_f.close()


def file_to_bytes_to_object():
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print(d) # {'name': 'george', 'age': 20, 'score': 88}  # 這變數跟原來的變數是完全不相干的object，只是內容相同而已。


def main():
    object_to_bytes_to_file()
    file_to_bytes_to_object()

if __name__ == '__main__':
    main()
