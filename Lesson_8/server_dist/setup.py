from setuptools import setup, find_packages

setup(name="my_mess_server",
      version="0.0.1",
      description="mess_server",
      author="Anton Kulikov",
      author_email="kulikoff.ab@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
