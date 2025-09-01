
'''
function base_generate:
    given list: lst, path: str
    returns nothing
    creates M3U file at given file path
'''

def base_generate(list,path):

    #create empty list for lines to generate
    lines_to_write = []

    #m3u header line
    with open(path,"w")as file:
        file.write("#EXTM3U")

    #for each stream append info in format of #EXTINF:-1 group-title="live", title (time | sport)
    for i in range(0,len(list)):
        lines_to_write.append(f'\n#EXTINF:-1 group-title="live",{list[i]["title"]} ({list[i]["time"]})\n{list[i]["m3u8"]}')

    #write all lines to m3u file
    with open(path,"a")as file:
        file.writelines(lines_to_write)

