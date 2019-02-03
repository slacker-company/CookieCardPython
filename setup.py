import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CookieCard",
    version="0.0.1",
    author="SlackerCompany",
    author_email="slackercompany@cookiemail.ml",
    description="API implementation of https://slackercompany.ml/CarteCookie/ in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slacker-company/CookieCardPython",
    packages=setuptools.find_packages()
)