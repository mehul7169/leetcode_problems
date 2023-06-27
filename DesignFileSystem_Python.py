class FileSystem:

    def __init__(self):
        self.paths = dict()

    def createPath(self, path: str, value: int) -> bool:
        if len(path) < 2:
            return False
        split = path.split('/')
        parentPath = '/'.join(split[:-1])
        if parentPath and parentPath not in self.paths or path in self.paths:
            return False
        else: self.paths[path] = value
        return True
    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        return -1