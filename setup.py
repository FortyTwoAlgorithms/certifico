from setuptools import setup

setup(
    name='certifico',
    version='0.0.1',
    packages=['certifico'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-PyMongo',
        'Flask-SendGrid',
        'sendgrid==3.6.5',
        'rq',
        'gunicorn'
    ],
)

