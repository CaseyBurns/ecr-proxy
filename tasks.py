# http://docs.pyinvoke.org/en/stable/

from invoke import task, Context

@task(help={'detached': 'start detacted docker-compose'})
def start(c, detached=False):
    """start test environment"""

    options = "-f docker-compose.yml -f docker-compose.dev.yml up"
    if detached:
        options += ' -d '

    c.run(f'docker-compose {options}')

@task
def stop(c):
    """stop test environment"""
    c.run('docker-compose -f docker-compose.yml -f docker-compose.dev.yml down')

@task
def restore(c):
    """restore packages required by tests"""
    c.run('pip install -r tests/requirements.txt')

@task
def tests(c):
    """run tests"""
    c.run('pytest --color=yes')

@task
def build(c):
    """build container"""
    c.run('docker build . -t ecr-proxy:dev')
