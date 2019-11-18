import setuptools
from setuptools import setup

setup(
    name="hanzi_char_lookup_feature",
    version="0.1",
    packages=setuptools.find_packages(),
    url="https://github.com/howl-anderson/hanzi_char_lookup_feature",
    license="MIT",
    author="Xiaoquan Kong",
    author_email="u1mail2me@gmail.com",
    description="Dictionary Feature extractor for Deep learning",
    install_requires=["pygtrie", "tokenizer_tools", "numpy"],
)
