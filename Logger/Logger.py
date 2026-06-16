from LogManager import LogManager
from LogSubject import LogSubject
class Logger:
    _instance = None
    chainOfLoggers = None
    logSubject=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def get_logger(self):
        if self.chainOfLoggers is None:
            log_manager = LogManager()
            self.chainOfLoggers = log_manager.create_chain_of_loggers()
            self.logSubject = log_manager.create_log_subject()

        return self._instance
    
    def createLog(self, level, message):
         return self.chainOfLoggers.log(level, message, self.logSubject)
      
    def info(self, level,message):
        self.createLog(level,message)

    def error(self, level,message):
        self.createLog(level,message)

    def debug(self, level,message):
        self.createLog(level,message)
    