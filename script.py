import re
print("starting filter!")
def open_file_as_lines(path):
    lines=[]
    with open(path,"r",encoding="utf-8") as f:
        lines=f.readlines()
    return lines

def rm_all_lines_contains_key(path,savepath,filterpath):
    text="" # filtered text
    keys=open_file_as_lines(filterpath)
    lines=open_file_as_lines(path)
    for line in lines:
        ok=True
        for key in keys:
            key=key.rstrip()
            if str(line).find(key) is not -1:
                ok=False
        if ok:
            text=text.__add__(line)    

        
    with open(savepath,"w",encoding="utf-8") as tf:
        tf.write(text)
        tf.close()
    print("keys filtered successfully!")
    pass

rm_all_lines_contains_key("asl","psites_fd","psites")