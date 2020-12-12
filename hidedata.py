class Hidedate(object):
    def __init__(self,filename):
        self.log = filename
        self.store = []
    def parser(self):
        import re
        with  open(self.log) as file:
            content = file.readlines()
            for  line in content:
                ext = r'\w+ \d+ \d+:\d+:\d+ '
                new = re.sub(ext,r"",line,re.IGNORECASE)
                #find = r'Started[\s+\w+]+'
                #match = re.findall(find,new,re.IGNORECASE)
                self.store.append(new)
        return self.store


if  __name__=='__main__':
    sol = Hidedate('syslog3')
    print(sol.parser())
