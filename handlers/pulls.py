import requests


def get_pulls(state):
    if state == "open" or state == "closed":
        return get_list_res(state)
    elif state == "accepted" or state == "needs work":
        return get_list_label(state)
    else:
        return get_list_all(state)


def get_list_res(state):
    lmy = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&per_page=100'
    response = requests.get(lmy)
    res = response.json()
    list_res = []
    for i in res:
        if i["state"] == state:
            dict = {"num": i['number'], "title": i['title'], "link": i['url']}
            list_res.append(dict)
    return(list_res)


def get_list_label(state):
    if state == "accepted" or state == "needs work":
        lmy = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&per_page=100'
        response = requests.get(lmy)
        res = response.json()
        list_res = []
        for i in res:
            if i["labels"] and i["labels"][0]["name"] == state:
                dict = {"num": i['number'], "title": i['title'], "link": i['url']}
                list_res.append(dict)
                print(list_res)
    return (list_res)


def get_list_all(state):
    lmy = 'https://api.github.com/repos/alenaPy/devops_lab/pulls?state=all&per_page=100'
    response = requests.get(lmy)
    res = response.json()
    list_res = []
    for i in res:
        dict = {"num": i['number'], "title": i['title'], "link": i['url']}
        list_res.append(dict)
    return(list_res)
