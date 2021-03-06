class Config:
    def __init__(self):
        pass

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:187125@localhost/school?charset=utf8mb4"
    SECRET_KEY = 'school'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    def __init__(self):
        pass

    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}

wx_config = {
    'appid': 'wx8630b25104aea1d8',
    'secret': '7156d3e922bb934d1819e5410abddd07'
}

weather_config = {
    'AppKey': 'b4f039195a3ee3eb9c16b32f95b93b5d'
}
