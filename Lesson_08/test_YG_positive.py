
import requests

obj_req = requests

base_url = "https://ru.yougile.com"

                #Позитивные проверки

#________Начало_работы_сбор_необходимых данных_____

    #Получение списка компаний для нахождения id своей компании
dict_get_compani = {
    "login": "kumbosarkarim52@gmail.com",
    "password": str(input("Введите пароль: ")),
    "name": "QA_SkyPro_Ученик"
}

def test_get_compani_id():
    print("[Получение списка компаний]")
    request_1_post = obj_req.post(base_url + "/api-v2/auth/companies", json = dict_get_compani)
    print("Статус код: ", request_1_post.status_code)
    assert request_1_post.status_code == 200
    print("Статус код: ", request_1_post.status_code) 
    return request_1_post
        #Сохранение результата  переменную
func_1_resault = test_get_compani_id()
            #Работа с результатом функции
dict_companies = func_1_resault.json()
print("Тело ответа: ", dict_companies)


    #Получение токена используя id компании
        #словарь для дальнейшей работы функции
dict_get_token = {
    "login": "kumbosarkarim52@gmail.com",
    "password": dict_get_compani["password"],
    "companyId": dict_companies["content"][0]["id"]
}
        #Функция для получения токена авторизации
def test_get_token():
    print("[Получения токена авторизации]")
    post_get_key = obj_req.post(base_url + "/api-v2/auth/keys/get", dict_get_token)
    assert post_get_key.status_code == 200
    print("Статус код: ", post_get_key.status_code)
    return post_get_key
        #Сохранение результата  переменную
func_2_resault = test_get_token()
            #Операции с результатом функции:
print("Тело ответа: ", func_2_resault.json())
        #Сохранение токена в переменную
obj_token = func_2_resault.json()[0]["key"]
print("Ваш токен авторизации: ", obj_token)

    #Создание заголовка(headers)
dict_headers_func_3 = {
    "Authorization" : f'Bearer {obj_token}'
}

    #Получение списка пользователей
def test_get_user_id():
    print("[Получение списка пользователей ]")
    req_get_user_id = obj_req.get(base_url + "/api-v2/users", headers = dict_headers_func_3)
    assert req_get_user_id.status_code == 200
    print("Статус код" ,req_get_user_id.status_code)
    return req_get_user_id

        #Сохранение результата в переменную
func_3_resault = test_get_user_id()
            #Операции с результатом функции
print("Тело ответа: ", func_3_resault.json())
            #Извлечение id пользователя в переменную
obj_user_id = func_3_resault.json()["content"][0]["id"]
print("Ваш id:", obj_user_id)

#_____________________________


#______Операции_с_YouGile_Проверки____               <<<<-------Проверки здесь

    #Создание проекта с пустым заголовком
dict_project_create = {
    "title": "",
    "users": {
        obj_user_id : "admin"
    }
}

def test_project_create():
    print("[Создание проекта]")
    req_project_create = obj_req.post(base_url + "/api-v2/projects", json = dict_project_create, headers = dict_headers_func_3)
    assert req_project_create.status_code == 201
    print("Статус код: ",req_project_create.status_code)
    return req_project_create
        #Сохранение результата в переменную
func_4_resault = test_project_create()
            #Операции с результатом
print("Тело ответа:", func_4_resault.json())


    #Отправка запроса на получение списка проектов с не действительным путем в URL адресе
def test_get_list_projects():
    print("[Получение списка проектов]")
    req_get_list_project = obj_req.get(base_url + "не действительный путь", headers = dict_headers_func_3)
    assert req_get_list_project.status_code == 200
    print("Статус код: ", req_get_list_project.status_code)
    return req_get_list_project
    #Сохранение результата в переменную
func_5_resaults = test_get_list_projects()
        #Операции с результатом
print("Тело ответа: ", func_5_resaults.json())
        #Сохранение id проекта в переменную
obj_project_id = func_5_resaults.json()["content"][-1]["id"]


    #Получение информации о проекте без токена авторизации
def test_get_project_by_id():
    print("[Получение информации о проекте по его id]")
    req_get_project_by_id = obj_req.get(base_url + "/api-v2/projects/" + obj_project_id)
    assert req_get_project_by_id.status_code == 200
    print("Статус код:", req_get_project_by_id.status_code)
    return req_get_project_by_id
        #Сохранение результата в переменную
func_6_resaults = test_get_project_by_id()
            #Операции с результатом
print("Тело ответа:", func_6_resaults.json())


    #Внос изменений в проект через не действительного пользователя
put_changes_body = {
    "title": "Python_YouGile_проект_дз",
    "users": {
    "Не действительный пользователь123456": "admin"
  }
}

def test_project_put_changes():
    print("[Внос изменений в проект]")
    req_project_put_changes = obj_req.put(base_url + "/api-v2/projects/" + obj_project_id, json = put_changes_body, headers = dict_headers_func_3)
    return req_project_put_changes
        #Сохранение результата в переменную
func_7_resaults = test_project_put_changes()
            #Операции с результатом
print("Статус код:", func_7_resaults.status_code)
print("Статус код:", func_7_resaults.json())

#________Завершение_скрипта________