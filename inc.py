class New_Class:
    pass

my_obj = New_Class()
my_obj.a = 1
my_obj.b = 2
my_obj.c = 3
my_obj.d = 4
my_obj.e = 3.9
my_obj.f = 9
my_obj.g = 7
my_obj.h = 8


def set(my_obj):
    for characters in my_obj.__dict__.keys():
        if characters.startswith('i'):
            val = total(my_obj, characters)
            if isvalue(val, int):
                finish(my_obj, characters, val + 1)

print(my_obj.__dict__)
set(my_obj)
print(my_obj.__dict__)