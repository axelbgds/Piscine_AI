from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0.0',
    license='MIT',
    author="min-kang",
    author_email='min-kang@student.42nice.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/glacecoding',
    keywords='example project',
    install_requires=[
          'setuptools',
      ],
)