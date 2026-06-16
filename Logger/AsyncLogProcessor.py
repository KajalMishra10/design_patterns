class AsyncLogProcessor:
    def __init__(self, level):
        self.level = level
        self.next_processor=None
    def log(self, level, message, log_subject):
        # Simulate asynchronous log processing
        pass
    def set_next(self, next_processor):
        self.next_processor = next_processor

class InfoLogProcessor(AsyncLogProcessor):
    
    def log(self, level, message, log_subject):
        # Process info level logs
        if level>=self.level:
            print(f"INFO: {message}")
            log_subject.notify_handlers(level, message)
            if self.next_processor:
                self.next_processor.log(level, message, log_subject)

class ErrorLogProcessor(AsyncLogProcessor):

    def log(self, level, message, log_subject):
        # Process error level logs
        if level>=self.level:
            print(f"ERROR: {message}")
            log_subject.notify_handlers(level, message)
            if self.next_processor:
                self.next_processor.log(level, message, log_subject)

class DebugLogProcessor(AsyncLogProcessor):

    def log(self, level, message, log_subject):
        # Process debug level logs
        if level>=self.level:
            print(f"DEBUG: {message}")
            log_subject.notify_handlers(level, message)
            if self.next_processor:
                self.next_processor.log(level, message, log_subject)