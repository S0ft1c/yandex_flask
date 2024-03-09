# from requests import get, post, delete
#
# print(get('http://127.0.0.1:5000/api/news').json())
# print(get('http://127.0.0.1:5000/api/news/1').json())
#
# print(get('http://127.0.0.1:5000/api/news/999').json())
# print(post('http://127.0.0.1:5000/api/news', json={}).json())
#
# print(post('http://127.0.0.1:5000/api/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://127.0.0.1:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())
#
# print(delete('http://127.0.0.1:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://127.0.0.1:5000/api/news/1').json())


from requests import get, post, delete

print(get('http://localhost:8080/api/v2/news').json())
print(get('http://localhost:8080/api/v2/news/1').json())

print(get('http://localhost:8080/api/v2/news/999').json())
print(post('http://localhost:8080/api/v2/news', json={}).json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:8080/api/v2/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

print(delete('http://localhost:8080/api/v2/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:8080/api/v2/news/1').json())