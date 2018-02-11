# in python 3-6 there is order-preserving,
# but should not be relied upon (this may change in the future)
# https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-compactdict

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
