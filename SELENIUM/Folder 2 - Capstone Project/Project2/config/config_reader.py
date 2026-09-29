import configparser
import os

class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls, config_path=None):
        if cls._config is None:
            if config_path is None:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                config_path = os.path.join(base_dir, "config", "config.ini")
            
            cls._config = configparser.ConfigParser()
            cls._config.read(config_path)
        return cls._config

    @classmethod
    def get(cls, section, key, fallback=None):
        config = cls.load_config()
        return config.get(section, key, fallback=fallback)

    @classmethod
    def get_boolean(cls, section, key, fallback=False):
        config = cls.load_config()
        return config.getboolean(section, key, fallback=fallback)

    @classmethod
    def get_int(cls, section, key, fallback=0):
        config = cls.load_config()
        return config.getint(section, key, fallback=fallback)

    @classmethod
    def get_base_url(cls):
        return cls.get("DEFAULT", "base_url")

    @classmethod
    def get_browser(cls):
        return cls.get("DEFAULT", "browser", "chrome")

    @classmethod
    def is_headless(cls):
        return cls.get_boolean("DEFAULT", "headless", False)

    @classmethod
    def get_implicit_wait(cls):
        return cls.get_int("DEFAULT", "implicit_wait", 10)

    @classmethod
    def get_explicit_wait(cls):
        return cls.get_int("DEFAULT", "explicit_wait", 15)
