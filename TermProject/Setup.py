from distutils.core import setup, Extension

module_spam = Extension('cstr', sources = ['returnstr.c'])

setup(
    name='HealthHero', 
    version='1.0',
    py_modules=['Hospital', 'Email', 'Graph', 'InfoClass', 'locationDict', 'Server', 'telegram'], 
    packages=['Resource'], 
    package_data = {'Resource': ['*.png']},
    ext_modules=[module_spam]
    )
