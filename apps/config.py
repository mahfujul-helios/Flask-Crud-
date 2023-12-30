class Config(object):
    pass

class ProductionConfig(Config):
    DEBUG = False

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}