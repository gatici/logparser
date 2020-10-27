def parser(logfile):
    res = dict()
    count = 1
    with open(logfile,"r") as file:
        for  line  in  file:
            ipaddr = line.split('-')[0].strip()
            page_visited = line.split('"')[1]
            if ipaddr not  in res:
                res[ipaddr] = [[page_visited],[count]]
            else:
                if page_visited in res[ipaddr][0]:
                    ind = res[ipaddr][0].index(page_visited)
                    res[ipaddr][1][ind] += 1
                else:
                    res[ipaddr][0].append(page_visited)
                    res[ipaddr][1].append(count)
                
    with open("analsis.log","w") as output:
        for  ip in  res:
            pages = res[ip][0]
            visited_num = res[ip][1]
            zipped = zip(pages,visited_num)
            qued = list(zipped)
            qued.sort(key=lambda x:x[1])
            output.write(f"{ip} {qued[0]} {qued[-1]} \n")
    return
            
if __name__=='__main__':
    parser("webserverlog.txt")  
    with  open("analsis.log",'r') as output:
        for  line  in output:
            print(line)
            
