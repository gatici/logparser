#number of page visited from same ip address

class VisitedPages(object):
    def __init__(self,logfile):
        self.log = logfile
        self.store = []
        
    def parser(self):
        with open(self.log) as file:
            content = file.read()
            ip = re.findall(r'\d+\.\d+\.\d+\.\d+', content)
            url = re.findall(r'GET [/\w.]+ HTTP/1.0', content)
            self.store = list(zip(ip,url))
            count = {i:self.store.count(i) for  i  in self.store}
            sort = sorted(count.items(),key=lambda i:i[1],reverse=True)
#            sete = [set(i[0]) for  i  in  sort]
            return sort

        return 
            
    

if  __name__=='__main__':
    sol = VisitedPages('webserverlog.txt')
    print(sol.parser())
