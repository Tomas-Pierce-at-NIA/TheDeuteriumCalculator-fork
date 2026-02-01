
from xml.etree.ElementTree import ElementTree
from pathlib import Path
from collections.abc import Mapping

class UniMod(Mapping):
    "lookup table for UniMod-labeled modifications"
    namespaces = {'unimod': 'http://www.unimod.org/xmlns/schema/unimod_tables_1'}
    
    __default = None
    
    def __init__(self, filepath :Path):
        self.path = filepath
        self.tree = ElementTree()
        self.tree.parse(self.path)
        self.__mod_lookup = self.get_mod_lookup()
    
    def __len__(self):
        return self.__mod_lookup.__len__()
    
    def __getitem__(self, key):
        return self.__mod_lookup.__getitem__(key)
    
    def __contains__(self, key):
        return self.__mod_lookup.__contains__(key)
    
    def __iter__(self):
        return self.__mod_lookup.__iter__()
    
    @classmethod
    def default(cls):
        if cls.__default is None:
            unimod = Path(__file__).parent / "unimod"
            table_filename = unimod / "unimod_tables.xml"
            cls.__default = cls(table_filename)
        return cls.__default
    
    def get_mod_rows(self):
        root = self.tree.getroot()
        mods = root.find("unimod:modifications", self.namespaces)
        rows = mods.findall("unimod:modifications_row", self.namespaces)
        return rows
    
    def get_mod_lookup(self):
        rows = self.get_mod_rows()
        lookup = {}
        for row in rows:
            record_id = row.attrib['record_id']
            lookup[record_id] = row.attrib
        return lookup
     

