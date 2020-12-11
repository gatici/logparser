class Parser(object):
    def __init__(self,filename):
        self.store = []
        self.input = filename
    def parser(self):
        import re
        with open(self.input,"r") as file:
            while True:
                content = file.readline()
                a = re.findall(r"Starting \w+ \w+", content)
                if a:
                    for  i  in a:
                        self.store.append(i)
                if not content:
                    break
        return self.store
        
 
            
                
if __name__=='__main__':
    sol = Parser("syslog")
    res = sol.parser()
    for  i in  res:
        print(i,end="\n")
