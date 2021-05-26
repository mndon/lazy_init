# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 16:21
# @Author  : LinMD
# @File    : lazy_init.py
# @Descip  :
class LazyProxy:
    def __init__(self, cls, *args, **kwargs):
        print("INIT PROXY")
        self.__dict__['_cls'] = cls
        self.__dict__['_params'] = args
        self.__dict__['_kwargs'] = kwargs
        self.__dict__['_obj'] = None

    def __getattr__(self, item):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        return getattr(self.__dict__['_obj'], item)

    def __setattr__(self, key, value):
        if self.__dict__['_obj'] is None:
            self._init_obj()
        setattr(self.__dict__['_obj'], key, value)

    def _init_obj(self):
        self.__dict__['_obj'] = object.__new__(self.__dict__['_cls'])
        self.__dict__['_obj'].__init__(*self.__dict__['_params'], **self.__dict__['_kwargs'])


class LazyInit:
    """需要实现懒加载的类，继承该类"""

    def __new__(cls, *args, **kwargs):
        return LazyProxy(cls, *args, **kwargs)
