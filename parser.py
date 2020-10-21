
def log_parser(log):
    parsed_data= []
    with open(log,"r") as file:
        prev_time=""
        data = {}
        for  line in file:
            time= line.split("[")[1].split("]")[0].split(" ")[0]
            status_code = line.split('"')[2].split(" ")[1]
            
            if prev_time != "":
                if time == prev_time:
                    data[time]["count"] = data[time]["count"] +1
                    if status_code in data[time]:
                        data[time][status_code] = data[time][status_code] +1
                        
                    else:
                        data[time][status_code] = 1
                else:
                    prev_time= time
                    parsed_data.append(data)
                    data = {}
                    data[time] = {"count":1, status_code: 1}
            else:
                prev_time = time
                data[time] = {"count":1, status_code:1}
    
    return parsed_data
  
for _ in  log_parser("/var/log/apache2/access.log"):
    print(_)
