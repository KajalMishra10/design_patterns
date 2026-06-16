from AsyncLogProcessor import InfoLogProcessor, ErrorLogProcessor, DebugLogProcessor
from LogHandler import fileHandler, consoleHandler, Handler
from LogSubject import LogSubject

class LogManager:
    def create_chain_of_loggers(self):
        # Create the chain of loggers (e.g., ConsoleLogger, FileLogger, etc.)
        info_processor = InfoLogProcessor(level=1)
        error_processor = ErrorLogProcessor(level=2)
        debug_processor = DebugLogProcessor(level=3)
        info_processor.set_next(error_processor)
        error_processor.set_next(debug_processor)

        return info_processor
    
    def create_log_subject(self):
        logSubject = LogSubject()
        file_handler = fileHandler()
        console_handler = consoleHandler()
        logSubject.add_handler(1, file_handler)
        logSubject.add_handler(1, console_handler)
        logSubject.add_handler(2, file_handler)
        logSubject.add_handler(3, console_handler)
        return logSubject