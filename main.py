import string

def main():
    with open("log.txt") as f:
        content = f.readlines()
        for x in content:
            filterMsg(x)


def filterMsg(x):
    if x.startswith('SUCCESS'):
        # TODO: Turn this into a class that tostring method outputs this:
        content= x.split()
        # print
        ProduceLog(content[2],string.join(content[5:], " "),"PASSED")

        #print  x.split()


def ProduceLog(time, cmd_exec, status):
    print(" level=INFO " +
    
           " openshiftVersion=3.7 " +
           " project=oshinko-cli " +
           " action="+ cmd_exec +
           " status=START  " )
    print(" level=INFO  " +
           " openshiftVersion=3.7 " +
           " project=oshinko-cli " +
           " action="+ cmd_exec +
           " time=" + time +
           " status="+ status)



main()