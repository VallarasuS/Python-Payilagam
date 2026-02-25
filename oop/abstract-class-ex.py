from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def save(self, message):
        pass


class USBStorage(Storage):

    def delete(self):
        print("USB:: delete")

    def write(self, message):
        print(message)

    def save(self, message):
        print("USB:: ", message)


class Application:

    def run(self, storage):

        print("app started")

        storage.save("app started")

        print("app processing")

        print("app completed")

        print("app exited")

        storage.save("app exited")


# fileStorage = Storage()
usbStorage = USBStorage()

app = Application()
app.run(usbStorage)
