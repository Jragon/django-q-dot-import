
from importlib import import_module
import logging
logger = logging.getLogger('django-q')

class DotImport():
    def __init__(self, path, **kwargs):
        try:
            module_path, class_name = path.rsplit(".", 1)
            module = import_module(module_path)
            Reporter = getattr(module, class_name)
            self.Reporter = Reporter(**kwargs)
        except Exception as e:
            logger.exception(e, exc_info=True)


    def report(self):
        self.Reporter.report()
