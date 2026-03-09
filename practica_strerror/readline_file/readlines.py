from os import strerror

try:
    count = line_count = 0
    for line in open('practica_strerror/Simple_Text.txt', 'rt'):
        line_count += 1
        for character in line:
            print(character, end = '')
            count += 1

        print("\n\n Caracteres del archivo:   ", count)
        print("Lineas en el archivo:   ", line_count)
except IOError as e:
    print("Se produjo un error inesperado en: ", strerror(e.errno))
<<<<<<< HEAD:practica_strerror/readlines.py
=======





>>>>>>> 5ac250e9fbb914c40a5b0061ecdbaab6b585765a:practica_strerror/readline_file/readlines.py
