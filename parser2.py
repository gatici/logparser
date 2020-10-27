class Solution:
    def visitedsites(self,page):
        store = {}
        count = 1
        res = []
        with open(page,"r") as file:
            for  line  in  file:
                ipaddr = line.split("-")[0].strip()
                link = line.split('"')[1].split(" ")[1]
                if  ipaddr in  store:
                    if link  in  store[ipaddr][0]:
                        ind = store[ipaddr][0].index(link)
                        store[ipaddr][1][ind] += 1
                    else:
                        store[ipaddr][0].append(link)
                        store[ipaddr][1].append(count)
                else:
                    store[ipaddr] = [[link],[count]]
        for  ip in store:
            visited = store[ip][0]
            quantity = store[ip][1]
            temp = list(zip(visited,quantity))
            temp.sort(key=lambda x:x[1])
            res.append(f"[{ip} {temp[0]} {temp[-1]}]")
        return res
            
s = Solution()
print(s.visitedsites("webserverlog.txt"))
