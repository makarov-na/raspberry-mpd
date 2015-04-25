from bottle import route, run


@route('/<man>')
def hello(man):
    return "Hello "+man+"!"


def fetcher(obj, index):
    return obj[index]

x = "spam"

print(x)


class User:
    def __init__(self, name):
        self.id = 111
        self.name = name

user1 = User("John Doe")

print(str(user1.id)+":"+user1.name)


try:
    fetcher(x, 66)
except IndexError as err:
    xw = 5
    print(err.args)


#run(host='0.0.0.0', port=8080,reloader=True)