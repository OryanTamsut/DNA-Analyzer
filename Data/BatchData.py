class BatchData:
    _instance = None
    _was_init = False

    def __new__(cls, *args, **kwargs):
        if not BatchData._instance:
            BatchData._instance = object.__new__(cls)
        return BatchData._instance

    def __init__(self):
        if not BatchData._was_init:
            self.__batches = {}
            BatchData._was_init = True

    def add_batch(self, name, batch):
        if name[0] == "@":
            name = name[1:]
        self.__batches[name] = batch
        return batch

    def get_batch(self, name):
        if name[0] == "@":
            name = name[1:]
            return self.__batches.get(name)
        raise Exception("error, name need to start with @")

    def get_all_batches(self):
        return self.__batches
