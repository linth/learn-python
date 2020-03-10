MISSING = object()


class Base(object):
    """ The base class that all of the object model classes inherit from. """

    def __init__(self, cls, fields):
        """
        every object has a class.
        :param cls:
        :param fields:
        """
        self.cls = cls
        self._fields = fields

    def read_attr(self, field_name):
        """
        read field: field_name out of the object.
        :param field_name:
        :return:
        """
        return self._read_dict(field_name)

    def write_attr(self, field_name, value):
        """
        write field: field_name into the object.
        :param field_name:
        :param value:
        :return:
        """
        self._write_dict(field_name, value)

    def isinstance(self, cls):
        """
        return true if the object is an instance of class cls.
        :param cls:
        :return:
        """
        return self.cls.issubclass(cls)

    def callmethod(self, method_name, *args):
        """
        call method: 'method_name' with arguments 'args' on object.
        :param method_name:
        :param args:
        :return:
        """
        meth = self.cls_read_from_class(method_name)
        return meth(self, *args)

    def _read_dict(self, field_name):
        """
        read an field: field_name out of object's dict.
        :param field_name:
        :return:
        """
        return self._fields.get(field_name, MISSING)

    def _write_dict(self, field_name, value):
        """
        write a field: field_name into the object's dict.
        :param field_name:
        :param value:
        :return:
        """
        self._fields[field_name] = value


class Instance(Base):
    """ Instance of a user-defined class. """

    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, {})


class Class(Base):
    """ A User-defined class. """

    def __init__(self, name, base_class, fields, metaclass):
        Base.__init__(self, metaclass, fields)
        self.name = name
        self.base_class = base_class

    def method_resolution_order(self):
        """
        compute the method resolution order of the class.
        :return:
        """
        if self.base_class is None:
            return [self]
        else:
            return [self] + self.base_class.method_resolution_order()

    def issubclass(self, cls):
        """
        is self a subclass of cls?
        :param cls:
        :return:
        """
        return cls in self.method_resolution_order()

    def _read_from_class(self, method_name):
        """
        :param method_name:
        :return:
        """
        for cls in self.method_resolution_order():
            if method_name in cls._fields:
                return cls._fields[method_name]
        return MISSING


OBJECT = Class(name='object', base_class=None, fields={}, metaclass=None)
TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)


if __name__ == '__main__':
    # set up the base hierarchy like in Python (the ObjVLisp model)
    OBJECT = Class(name='object', base_class=None, fields={}, metaclass=None)

    TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)

    # TYPE is an instance of itself
    TYPE.cls = TYPE
    # OBJECT is an instance of TYPE
    OBJECT.cls = TYPE

    print(TYPE.cls, TYPE.base_class) # <__main__.Class object at 0x00000174790870F0> <__main__.Class object at 0x00000174790870B8>
    print(OBJECT.cls, OBJECT.base_class) # <__main__.Class object at 0x00000174790870F0> None