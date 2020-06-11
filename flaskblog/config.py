import os


class Config:
    SECRET_KEY = 'b87b27ded93869ad0b42f700e20b2b8e'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://xgfqwybykoawbx:9ab838021cede9ded21e3d3cb3ebbbde4ae5bb5fd58fb21ba0582f3045539811@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/ddbnuj4mfb4h0e'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

