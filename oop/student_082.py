class Student:
    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        if modlist is None:
            self.modlist = []
        else:
            self.modlist = list(modlist)

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def __str__(self):
        sorted_mods = sorted(self.modlist)
        return 'ID: {}\nName: {}\nModules: {}'.format(
            self.sid,
            self.name,
            ', '.join(sorted_mods)
        )
