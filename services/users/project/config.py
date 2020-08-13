# services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False


class DevelopmentConfig:
    """Developement configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""
    pass
