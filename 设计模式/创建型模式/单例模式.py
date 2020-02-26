# 单例模式概念及一般实现
# 单例模式的装饰器实现
# 简单工厂模式
# 抽象工厂模式

# 所谓单例模式，也就是说不管什么时候我们要确保只有一个对象实例存在。
# 很多情况下，整个系统中只需要存在一个对象，所有的信息都从这个对象获取，
# 比如系统的配置对象，或者是线程池。这些场景下，就非常适合使用单例模式。
# 总结起来，就是说不管我们初始化一个对象多少次，真正干活的对象只会生成一次并且在首次生成。

class singleton(object):

    _instance = None

    class _A:
        def __init__(self):
            pass

        def display(self):
            return id(self)

        def name(self):
            return "woyao"

    def __init__(self):
        if singleton._instance is None:
            singleton._instance = singleton._A()

    def __getattr__(self, item):
        return getattr(self._instance, item)

if __name__ == '__main__':
    s1 = singleton()
    s2 = singleton()
    print(s1.display())
