class Expense(object):
    def __init__(self,inputfile):
        self.store = []
        self.file = inputfile
        self.total = 0.0
    def parser(self):
        with open(self.file) as file:
            self.store = re.findall(r'[\d\.]+',file.read())
    def calculate(self):
        for  i  in  self.store:
            #print(i)
            self.total += float(i)
  
    def __str__(self):
        return str(self.total)


            
if  __name__=='__main__':
    sol = Expense('expenses.txt')
    sol.parser()
    sol.calculate()
    print(sol)
