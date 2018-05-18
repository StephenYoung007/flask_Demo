import json

from utils import log


def save(data, path):
    s= json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', data, s, path)
        f.write(s)


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s= f.read()
        log('load', s)
        return json.loads(s)



class Model(object):

    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = 'db/{}.txt'.format(classname)
        return path


    @classmethod
    def new(cls, form):
        m = cls(form)
        return m


    @classmethod
    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [cls.new(m) for m in models]
        return ms


    def save(self):
        models = save.all()
        models.append(self)
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)


    def __repr__(self):
        """
        这是一个 魔法函数
        不明白就看书或者 搜
        当你调用 str(o) 的时候
        实际上调用了 o.__str__()
        当没有 __str__ 的时候
        就调用 __repr__
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)


