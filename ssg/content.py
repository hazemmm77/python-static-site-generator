import re
from yaml import load,FullLoader
from collections.abc import Mapping
class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(self,cls,string):
        _, fm, content=self.__regex.split(string,2)
        base.load(fm,Loader= FullLoader)
        return cls(metadata,content)
