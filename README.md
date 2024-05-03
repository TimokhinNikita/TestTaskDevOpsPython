## Первым делом нам необходимо проверить/установить Docker:
https://i.imgur.com/KpNlIfw.png


## Далее поднимаем Docker:
https://i.imgur.com/RYhWhzW.png
https://i.imgur.com/sPU97eK.png

## Создаем три тестовых файла для проверки запросов:
changingApi.py
createApi.py
readApi.py

## И теперь проверяем:
https://i.imgur.com/gLaKPbj.png

## Проверяем, что приложение правильно обрабатывает запросы:
```bash
curl http://localhost:8080/keyvalue/my_key
```
https://i.imgur.com/AXJoXeW.png
