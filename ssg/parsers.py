from typing import List
from pathlib import Path
import shutil
class Parser:
    extensions:List[str]=[]
    def valid_extension(self,extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(path,source,dest):
        raise NotImplementedError

    def read(path):
         # using with statement
         with open(path, 'r') as file:
	         return file.read()

    def write(path,dest,content,ext=".html"):
        full_path=dest /path.with_suffix(ext).name
        with open(path, 'w') as file:
            file.write(content)

    def copy(self,path,source,dest):
        shutil.copy2(path, dest/ path.relative_to(source))
