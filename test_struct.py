import struct


def write_bin_file(filename, filter, args):
   with open(filename, 'wb') as F:
        data = struct.pack(filter, *args)
        F.write(data)
        
def main():

    filter='<i4shih16s' # Little End
    filename = 'data.bin'
    # python3.x need precede string with b' to make byte arrray
    args = 7, b'spam', 8, 9, 10, b'niall' 
    write_bin_file(filename, filter, args)

  
    data = r'\x07\x00spam\x08\x00'
    F = open(filename, 'rb')
    data = F.read()
    values = struct.unpack(filter, data)
    print(values)
    return
 
if __name__ == '__main__':
    main()
