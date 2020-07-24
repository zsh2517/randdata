from OutputMgr import OutputMgr
from Generator import Generator
from generators import gen


class DataSet:
    """
    数据集
    最终生成的一张表
    """
    order: list = []
    gen: dict = {}
    data: list = []

    def set(self, name: str, generator: Generator, arg: dict) -> bool:
        """
        添加一个生成器
        :param name: 字段名称
        :param generator: 生成器
        :param arg: 生成器所需要的参数
        :return:
        """
        if name in self.order:
            return False
        else:
            self.order.append(name)
            self.gen[name] = {}
            self.gen[name]["generator"] = generator
            self.gen[name]["arg"] = arg
            return True

    def remove(self, name: str) -> None:
        """
        删除指定的生成器
        :param name: 生成器字段名
        :return:
        """
        return

    def setorder(self):
        pass

    def gen_one(self):
        s = {}
        for k in self.order:
            s[k] = self.gen[k]["generator"].generate(self.gen[k]["arg"])
        self.data = [s]
        return s

    def gen_multi(self, length):
        total = []
        tempdict = {}
        for k in self.order:
            tempdict[k] = []
            if self.gen[k]["generator"].special_multi():
                tempdict[k] = self.gen[k]["generator"].generate_multi(length, self.gen[k]["arg"])
            else:
                tempdict[k] = [self.gen[k]["generator"].generate(self.gen[k]["arg"]) for i in range(length)]
        for i in range(length):
            d = {}
            for k in self.order:
                d[k] = tempdict[k][i]
            total.append(dict(d))
        self.data = total
        return total

    def output(self, mgr: OutputMgr):
        mgr.setData(self.order, self.data)
        mgr.output()
        pass