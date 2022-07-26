"""
Class Attribute (物件屬性) vs. Instance Attribute (實例屬性):
1. Instance Attribute (實例屬性):
    - is an instance attribute defined inside the constructor.
    - is accessible as both a property of the class and as a property of objects, as it is shared between all of them.
2. Class Attribute (物件屬性):
    - is a class attribute defined outside the constructor.

[Note] Class Attributes Mutate to Be Instance Attributes.

Reference:
    - https://dzone.com/articles/python-class-attributes-vs-instance-attributes
    - https://medium.com/georges-note-idea/python-class-attribute-vs-instance-attribute-%E8%A7%80%E5%BF%B5%E5%92%8C%E5%B7%AE%E7%95%B0-3e1bcbb3ec68
"""


class ExampleClass(object):
    # class attribute. (定義在外面的稱為物件屬性)
    class_attr = 0

    def __init__(self, instance_attr):
        # instance attribute. (定義在__init__()內的稱為實例屬性)
        self.instance_attr = instance_attr


if __name__ == '__main__':
    foo = ExampleClass(1)
    bar = ExampleClass(2)

    print('foo\'s instance attr: ', foo.instance_attr, '; class attr: ', foo.class_attr) # foo's instance attr:  1 ; class attr:  0
    print('bar\'s instance attr: ', bar.instance_attr, '; class attr: ', bar.class_attr) # bar's instance attr:  2 ; class attr:  0
    print(ExampleClass.class_attr)
    print(foo.class_attr)
    print(bar.class_attr)
    # print(ExampleClass.instance_attr) # 此需要被實體化才會有instance_attr值

    # Class Attributes Mutate to Be Instance Attributes
    foo.class_attr = 3
    print('foo\'s instance attr: ', foo.instance_attr, '; class attr: ', foo.class_attr) # foo's instance attr:  1 ; class attr:  3
    print('bar\'s instance attr: ', bar.instance_attr, '; class attr: ', bar.class_attr) # bar's instance attr:  2 ; class attr:  0

    print(ExampleClass.__dict__) # {'__module__': '__main__', 'class_attr': 0, '__init__': <function ExampleClass.__init__ at 0x0000026E85555488>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
    print(foo.__dict__) # {'instance_attr': 1, 'class_attr': 3}
    print(bar.__dict__) # {'instance_attr': 2}
