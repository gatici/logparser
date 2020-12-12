with open('webserverlog.txt') as file:
    
    content = file.read()
    rex1 = r"(\d+\.\d+\.\d+\.\d+)"
    rex2 = r"(GET [/\w.]+)"
    match1 = re.findall(rex1,content)
    match2 = re.findall(rex2,content)
    visit_ob = list(zip(match1,match2))
    countvisits = {i:visit_ob.count(i) for  i  in  visit_ob}
    sortedv = sorted(countvisits.items(),key=lambda x:x[1], reverse=True)
    print(sortedv)
