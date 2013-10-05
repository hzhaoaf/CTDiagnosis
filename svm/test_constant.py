
var1 = 1

class Constant:
    var1 = 1

if __name__ == '__main__':
    config = Constant()
    print config.var1, config.var2
    config.var1 = 3
    print config.var1, config.var2



