import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run


def hello(name='world'):
    print('hello %s!' % name)

# def prepare_deploy():
#     local("./manage.py test uploadapp")
#     local("git init")
#     local("git add")
#     local('git commit -m "first commit" ', capture=False)
    # local("git remote add origin https://github.com/sprashan069/demo.git ")
    # local("git push -u origin master ")

def clone():
    local("git clone https://github.com/sprashan069/Angular-5.git")

def test():
    local("./manage.py test uploadapp")

def commit():
    local("git add -A")
    # local("git commit")
    local('git commit -a -m  "first commit" ', capture=False)
    local("git remote add origin https://github.com/sprashan069/Fabric_test.git ")

def push():
    local("git push -u origin master")

def prepare_deploy():
    # test()
    commit()
    push()
