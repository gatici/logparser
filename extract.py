
class Extract(object):
    def __init__(self,logfile):
        self.log = logfile
        self.store = []
        
    def  parser(self):
        import re
        with  open(self.log,'r') as file:
            content = file.readlines()
            for  line  in content:
                if  "BIOS-" in  line:
                    part = line.split(" ")[10:]
                    self.store.append(part)
        return self.store

if __name__=='__main__':
    sol = Extract('syslog3')
    for  line  in  sol.parser():
        print(line, sep="\n")
