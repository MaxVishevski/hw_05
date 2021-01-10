# 1. Написать генератор песенки «TEN green bottles
# hanging on the wall».
# В песенке вместо цифр должны быть именно слова,
# обозначающие цифры, т.е. TEN, NINE, EIGHT, etc.
# 2понедельник, 28 декабря 2020 г.
# Песенка состоит из серии куплетов вот таких:
# <количество> green bottles hanging on the wall,
# <количество> green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There‛ll be...
# <пустая строка>
# <количество - 1> green bottles hanging on the wall...
# И так до тех пор, пока не закончатся бутылки. Когда
# они закончились, то песенка должна закончится
# фразой: NO green bottles hanging on the wall!

d = {1: 'one',
     2: 'two',
     3: 'three',
     4: 'four',
     5: 'five',
     6: 'six',
     7: 'seven',
     8: 'eight',
     9: 'nine',
     10: 'ten',
     }




i = len(d)
while 1 <= i:
    if i == 1:
        string = "And if one green bottle should accidentally fall,\nThere‛ll be...\n"

    else:
        string = f'{d[i]} {"green bottles hanging on the wall"}'
    i -= 1
    print(string)
else:
    print("NO green bottles hanging on the wall!")
