class Clearlog(object):
    def __init__(self,logfile):
        self.log = logfile
        self.store = []
    def parser(self):
        import re
        with  open(self.log,'r') as file:
            content = file.readlines()
            for  line in content:
                regex = r'[[\d/\w/\d:\d:\d]+ -\d+]'
                #new = re.findall(regex,content,re.IGNORECASE)
                new = re.sub(regex,r"",line,re.IGNORECASE)
                print(new)
                self.store.append(new)
              
        return self.store



if  __name__=='__main__':
    sol = Clearlog('webserverlog2.txt')
    print(sol.parser())
    
