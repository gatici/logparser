class  LogParser(object):
    
    def __init__(self,logfile):
        self.logfile = logfile
        self.final_store = []
        self.content = []
    
    def _clear_log(self):
        with  open(self.logfile,'r') as  file:
            self.content = file.readlines()
            for  line in self.content:
                info_wout_time = line.split('"',1)[1]
                self.final_store.append(info_wout_time)
        return self.final_store
    
    def __str__(self):
        text = '\n'.join(self._clear_log())
        return text
    
 

if  __name__=='__main__':
    log = LogParser('webserverlog2.txt')
    print(log)
        
