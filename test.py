import struct

def write_bin_file(filename, filter, *args):
   with open(filename, 'wb') as F:
        data = struct.pack(filter, *args)
        F.write(data)
   return

def main():
    filter='<i4shih45s'
    filename = 'data.bin'
    write_bin_file(filename, filter,  7, 'spam', 8, 9, 10, 'niall')
  
    #data = r'\x07\x00spam\x08\x00'
    F = open(filename, 'rb')
    data = F.read()
    data
    print data
    values = struct.unpack(filter, data)
    print values
    return
 
if __name__ == '__main__':
    main()
