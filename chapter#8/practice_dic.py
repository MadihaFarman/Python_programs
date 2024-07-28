my_dic = {'madiha':'03338336248','farman':'03359737865','maria':'03329038808'}
if 'mariaa' in my_dic:
    # print('not found')
    del my_dic['maria']

# my_dic['papa'] = '03464128408'
# print(my_dic)
# del my_dic['farman']
# print(my_dic)
# the following wil raise an error
# del my_dic['farmannn']
# print(my_dic)
print(len(my_dic))
test_scores = {'Madiha':[20,25,23],'Fariha':[29,30,24],'Faryal':[87,34,21]}
print(test_scores)
print(test_scores['Fariha'])
print(test_scores['Madiha'])
my_phonebook = {}
my_phonebook['ali']='4356'
my_phonebook['akram']= '814092'
print(my_phonebook)
print(type(my_phonebook))
for key in my_dic:
    print(key)
for key in my_dic:
    print(my_dic[key])
# print(type(my_phonebook))
# for key in my_dic:
#     print(key,':',my_dic[key])
#my_dic.clear()
print(my_dic)
val = my_dic.get('madihaaa','madiha not found')
print(val)
print(my_dic.items())
for key,value in my_dic.items():
    print(key,value)
print(my_dic.keys())
for keys in my_dic.keys():
    print(keys)
my_dic.pop('madiha','not found')
print(my_dic)
my_dic['madiha'] = '03338336248'
print(my_dic)
k ,v = my_dic.popitem()
print(k,v)
print(my_dic)
print(my_dic.values())
print(my_dic.items())