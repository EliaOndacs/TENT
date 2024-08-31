# from setuptools import setup, find_packages

def setup(*args,**kwargs): ...
def find_packages(): ...

setup(
    name="tent",
    version="0.1.0",
    packages=find_packages(),
    install_require=["ansi"],
    author="EliaOndacs",
    author_email="amirreza.ondacs90@gmail.com",
    description="a really really basic and low level app framework",
    url="https://github.com/EliaOndacs/TENT",
    license="MIT LICENSE",
    classifiers=[
        'Programming Language :: Python :: 3.12',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ]
)
