class OutputMgr:
    """
    输出管理器
    """
    order = []
    data = []

    def get_help(self):
        """
        nothing
        :return:
        """
        return "以表格的形式输出内容"

    def setData(self, order, data):
        self.data = data
        self.order = order
        return

    def output(self):
        def sumwhite(total, string):
            return total - len(string.encode("gbk")) + 1

        max_len = [len(item.encode("gbk")) for item in self.order]
        temp: int = 0
        for item in self.data:
            for i in range(len(self.order)):
                name = self.order[i]
                max_len[i] = max(max_len[i], len(str(item[name]).encode("gbk")))
        print("|", end="")
        for i in range(len(self.order)):
            print(" " * sumwhite(max_len[i], self.order[i]) + self.order[i] + " |", end="")
        print("")
        print("|", end="")
        for i in range(len(self.order)):
            print(" " + "-" * (max_len[i]) + " |", end="")
        print("")
        for item in self.data:
            print("|", end="")
            for i in range(len(self.order)):
                print(" " * sumwhite(max_len[i], item[self.order[i]]) + item[self.order[i]] + " |", end="")
            print("")
