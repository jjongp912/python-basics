
dic = {'오뎅':'300','순대':'400','만두':'500'}

menu = input('메뉴: ')

if menu in dic:

    print(menu,dic[menu])
else:
    price = 0
    print('가격: 0')
