import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
    name='gxm-guestbook',  # 程序包名称
    version='1.0.1',  # 版本号
    description='A guestbook web application.',
    long_description=read_file('README.rst'),
    author='gxm',
    author_email='gxm@tests.com',
    url='https://guestbook@git.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11'
    ],
    packages=find_packages(),  # 指定所有捆绑的Python程序包
    include_package_data=True,  # 设置用来是否安装Python包中所含的程序包资源
    keywords=['web', 'guestbook'],
    install_requires=[  # 列表指定安装依赖包
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        guestbook=guestbook:main
    """
)