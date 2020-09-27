from pathlib import Path
class Site:
    def __init__(self,source,dest):
        self_source=Path(source)
        self_dest=Path(dest)

    def create_dir(self,Path):

        directory=self_dest  / Path.relative_to(self_source)
        return directory.mkdir(parents=True, exist_ok=True)¶

    def build():
        dir= self_dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                create_dir(path)

        return dir
