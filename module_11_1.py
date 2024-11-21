import requests

url = 'https://2tcontrol.ru/'

r = requests.get(url) # HTTP запрос
print(r.status_code)          # 200 - запрос успешно выполнен
print(r.headers['content-type'])
print(r.text)
# методы HTTP
print(requests.head('https://httpbin.org/get'))
#requests.patch('https://httpbin.org/patch', data={'key':'value'})
# requests.post('https://httpbin.org/post', data={'key':'value'})
# requests.put('https://httpbin.org/put', data={'key':'value'})
# requests.delete('https://httpbin.org/delete')
# requests.options('https://httpbin.org/get')


# Скачать картинку с сайта
url = 'https://i.novgorod.ru/imho/photos/8/0/9/img-5908.jpg'

r = requests.get(url) # HTTP запрос
print(r.status_code)
with open('image.png', 'wb') as image:
    for i in r.iter_content(chunk_size=1024):
        image.write(r.content)
    print('Картинка сохранена')


'''
numpy - создать массив чисел, выполнить математические операции с массивом
 и вывести результаты в консоль
'''
import numpy as n


list1 = [67, 6, 8, 6, 4, 5, 6, 7, 8, 9, 1, 2, 3, 99, 30]

arr = n.array(list1)
print(arr.shape)       # размер массива
copy1 = arr.copy()     # копия массива
print(arr[1:4])        # срез массива
new_arr = n.array_split(arr, 5) # array_split - разделение массива
print(new_arr)
new_arr1 = arr.reshape(3, 5)   # reshape изменение формы массива
print(new_arr1)

for i in n.nditer(arr):  #  nditer итерация массива по элементам
    print(i)
for i in new_arr:
    n.nditer(i)
    print(i)

arr2 = n.stack(new_arr, axis = 1) # stack объединяет несколько массивов в один
print(arr2)

# where поиск значения в массиве, выявление совпадений, выводит индексы
x = n.where(arr == 6)
print(x)
x2 = n.where(arr % 2 == 0)
print(x2)
