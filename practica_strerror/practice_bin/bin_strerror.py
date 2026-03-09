from os import strerror

try:
    """with open('file.bin', 'wb') as f:
         f.write(b'ABCDE12345') # 10 bytes de datos"""
    
    """with open('file.bin', 'wb') as f_crear:
        f_crear.write(b'\x41\x42\x43\x44')"""
    
    binary_file = open('practica_strerror/practice_bin/file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))