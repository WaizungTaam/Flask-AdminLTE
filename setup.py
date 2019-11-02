import setuptools


with open('README.md', 'rb') as f:
    long_description = f.read().decode()

setuptools.setup(
    name='Flask-AdminLTE',
    version='0.0.1',
    author='waizungtaam',
    author_email='waizungtaam@gmail.com',
    description='Integration of Flask-Admin and AdminLTE template.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab-inet.zkyouxi.com/tanweizhong/zhangkun.oalogin',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'flask-admin'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
