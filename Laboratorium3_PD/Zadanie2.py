def fun(word,lenght):
    print('{:*>{size}}'.format("", size=lenght))
    print('*'+'{:{size}}'.format("", size=lenght-2)+'*')
    print('*'+'{:^{size}}'.format(word, size=lenght-2)+'*')
    print('*'+'{:{size}}'.format("", size=lenght-2)+'*')
    print('{:*>{size}}'.format("", size=lenght))

fun("Hello",11)


word = input("Please insert string")
lenght = int(input("Please insert lenght of box where string will be stored"))

fun(word, lenght)