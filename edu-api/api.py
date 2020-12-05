import requests
from bs4 import BeautifulSoup
import json


def day_info(login, password, day):
    url = "https://edu.tatar.ru/logon"
    payload = f'main_login={login}&main_password={password}'
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except:
        return json.loads('''{"error" : true, "error_text" : "Неопознанная ошибка"}''')
    if 'Неверный логин или пароль.' in response.text:
        return json.loads('''{"error" : true, "error_text" : "Неверный логин или пароль."}''')
    session = response.cookies['DNSID']
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
        'Cookie': f'DNSID={session}'
    }
    res2 = requests.request('GET', f"https://edu.tatar.ru/user/diary/day?for={day}", headers=headers)
    soup = BeautifulSoup(res2.text, 'lxml')
    list = soup.find_all('tr')
    ans = []
    try:
        for i in range(2, len(list)):
            temp = []
            for j in list[i].text.split("\n"):
                if j != '':
                    temp.append(j)
            if len(temp) > 1:
                ans.append(temp)
        json_ans = '{"error" : false, "lessons" : ['
        for i in ans:
            s = "{"
            try:
                s += f'"lesson_time" : "{i[0]}", "lesson_name":"{i[1]}", "homework" : "{i[2]}"'
            except:
                s += f'"lesson_time" : "{i[0]}", "lesson_name" : "{i[1]}", "homework" : null'
            if len(i) > 3:
                marks = ''
                for j in range(3, len(i)):
                    marks += i[j]
                    marks += " "
                s += ", "
                s += f'"marks" : "{marks.rstrip()}"'
            s += "}, "
            json_ans += s
        json_ans = json.loads(json_ans[:-2] + ']}')
        return json_ans
    except:
        return json.loads('''{"error" : true, "error_text" : "Неопознанная ошибка"}''')


def all_marks(login, password, period):
    url = "https://edu.tatar.ru/logon"
    payload = f'main_login={login}&main_password={password}'
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except:
        return json.loads('''{"error" : true, "error_text" : "Неопознанная ошибка"}''')
    if 'Неверный логин или пароль.' in response.text:
        return json.loads('''{"error" : true, "error_text" : "Неверный логин или пароль."}''')
    session = response.cookies['DNSID']
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
        'Cookie': f'DNSID={session}'
    }
    res2 = requests.request('GET', f"https://edu.tatar.ru/user/diary/term?term={period}", headers=headers)
    soup = BeautifulSoup(res2.text, 'lxml')
    list = soup.find_all('tr')
    marks = []
    for i in range(1, len(list) - 1):
        temp = []
        for j in list[i].text.split("\n"):
            if j != '' and j != 'просмотр':
                temp.append(j.lstrip())
        marks.append(temp)
    json_ans = ''
    json_ans += '{ "marks" : ['
    for i in marks:
        json_ans += '{' + f'"lesson" : "{i[0]}",'
        if len("".join(i[1:-1])) == 0:
            json_ans += '"marks" : null, "middle" : null, "final" : null},'
        else:
            if len(i[-1]) > 1:
                json_ans += '"marks"' +':'+ f'"{"".join(i[1:-1])}",'
                json_ans += f'"middle" : "{i[-1]}",'
                json_ans += f'"final" : null'
                json_ans += '},'
            else:
                json_ans += '"marks"' + ':' + f'"{"".join(i[1:-2])}",'
                json_ans += f'"middle" : "{i[-2]}",'
                json_ans += f'"final" : "{i[-1]}"'
                json_ans += '},'
    json_ans = json_ans[:-1]
    json_ans += ']}'
    return json.loads(json_ans)
def about_me(login, password):
    url = "https://edu.tatar.ru/logon"
    payload = f'main_login={login}&main_password={password}'
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except:
        return json.loads('''{"error" : true, "error_text" : "Неопознанная ошибка"}''')
    if 'Неверный логин или пароль.' in response.text:
        return json.loads('''{"error" : true, "error_text" : "Неверный логин или пароль."}''')
    session = response.cookies['DNSID']
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://edu.tatar.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://edu.tatar.ru/logon',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
        'Cookie': f'DNSID={session}'
    }
    res2 = requests.request('GET', f"https://edu.tatar.ru/user/anketa", headers=headers)
    soup = BeautifulSoup(res2.text, 'lxml')
    list = soup.find_all('table')
    ans = []
    for i in list[0].find_all('tr'):
        temp = []
        for j in i.text.split('\n'):
            if j != "":
                temp.append(j.strip())
        if len(temp) == 1:
            temp.append('null')
        ans.append(temp)
    a = '"'
    b = "'"
    json_ans = '{' + f'"name" : "{ans[0][1]}", "login" : "{ans[1][1]}", "school" : "{ans[2][1].replace(a,b)}", "birthday" : "{ans[4][1]}", "sex" :" {ans[5][1]}", "hobbies":"{ans[6][1]}",' \
                     f'"favorite_subjects" : "{ans[7][1]}", "dop_info":"{ans[8][1]}", "certificate" : "{ans[9][1]}"' + '}'
    print(json.loads(json_ans))
    return json.loads(json_ans)
