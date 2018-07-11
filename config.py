import os

CONFIG = {
    'items' : [{'pagename':'jtbcnews', 'since':'2017-01-01', 'until':'2017-12-31'},
                {'pagename':'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}],
    'common':{
        'fetch':True,
        'result_directory':'__results__/crawling',
        'access_token':'EAACEdEose0cBAE9r95ueWfXqSmeNrKle4LXp4bO8hLcljODYwKBItR9tnS9mcoOsT9E0RFq2AcCtSENqTy7WB1k4kYZCiuZCjHx9ZA3tMD81Cw8ZBjcR1xJq9ZCMit1kG7YZClkjeI1rH9vSy0n7uW7o4PVwLyYubpXzlzCznI7AAzwoEIKLy4LWSOQheHRukSmOGBpaUuVnOMJnbiwOBzj9oqCWd0EodVrHOkGRoRqwZDZD'
    }

}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])