import json
import pathlib

class Clumper:
    def __init__(self,blob):
        self.blob=blob
    
    def keep(self,*funcs):
        data=self.blob
        for func in funcs:
            data=[d for d in data if func(d)]
        return Clumper(data)

if __name__=='__main__':
    poke_dict = json.loads(pathlib.Path("pokemon.json").read_text(encoding='utf8'))
    print(Clumper(poke_dict).keep(lambda d:'Grass' in d['type'],
                                  lambda d:d['base']['HP']<60)
                                  .blob)