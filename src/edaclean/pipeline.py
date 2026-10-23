class Pipeline:
    def __init__(self, source):
        self.source = source
    def run(self):
        print(f"EdaClean is processing:{self.source}")