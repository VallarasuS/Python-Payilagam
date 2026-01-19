from abc import ABC, abstractmethod


# Abstract class
class Logger(ABC):

    def info(self, message):
        pass


class FileLogger(Logger):

    def info(self, message):
        print("File ::", message)


class DBLogger(Logger):
    def info(self, message):
        print("DB ::", message)


# Single logger example
class MyApplication:

    def register(self, logger):
        self.logger = logger

    def run(self):
        self.logger.info("Application Running")

    def stop(self):
        self.logger.info("Application Stopping")


app1 = MyApplication()  # initialize / construct
app1.register(DBLogger())
app1.run()

app2 = MyApplication()  # initialize / construct
app2.register(DBLogger())
app2.register(FileLogger())
app2.run()


# App with multi loggers
class AppMultiLoggers:

    def __init__(self):
        self.loggers = []

    def register(self, logger):
        self.loggers.append(logger)

    def run(self):
        for logger in self.loggers:
            logger.info("Application Running")


app = AppMultiLoggers()  # initialize / construct
app.register(DBLogger())
app.register(FileLogger())
app.run()
