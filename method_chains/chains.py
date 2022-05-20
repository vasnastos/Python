import json
import pathlib

poke_dict = json.loads(pathlib.Path("pokemon.json").read_text(encoding='utf8'))

class Clumper:
    def __init__(self,blob):
        self.blob=blob
    
    def keep(self,func):
        return Clumper([d for d in self.blob if func(d)])


if __name__=='__main__':
    print(Clumper(poke_dict).keep(
        lambda d: 'Grass' in d['type']).keep(
        lambda x: x['base']['HP']<60).blob)

