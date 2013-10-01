import sys
from collections import defaultdict
from sets import Set
import operator

class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx
    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())
    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)
    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)

mt = defaultdict(float)
#nt = [[None for _ in range(36955)] for _ in range(5573)]
#nt = [defaultdict(float) for _ in range(5573)]
nt = defaultlist(lambda: defaultdict(float))
movieidset = Set()

def readdata(input_file):
    l = input_file.readline()
    while l:
        line = l.strip()
        if line:
            fields = line.split(",")
            #mt[int(fields[0])][int(fields[1])] = float(fields[2])
            #mt[(int(fields[0]),int(fields[1]))] = float(fields[2])
            nt[int(fields[0])][int(fields[1])] = float(fields[2])
            movieidset.add(int(fields[1]))
            
        l = input_file.readline()
        
    

def count(mid):
    mid_count = 0;
    with_mid = defaultdict(int)
    not_with_mid = defaultdict(int)
    counts = defaultdict(int)
    
    for movieid in movieidset:
        counts[movieid] = 0
        
    for user_ratings in nt:
        if mid in user_ratings.keys():
            mid_count+=1
            for movieid in user_ratings.keys():
                counts[movieid]+=1
                if movieid != mid:
                    if movieid in with_mid:
                        with_mid[movieid]+=1;
                    else:
                        with_mid[movieid]=1;
        else:
            for movieid in user_ratings.keys():
                counts[movieid]+=1
                if movieid != mid:
                    if movieid in not_with_mid:
                        not_with_mid[movieid]+=1;
                    else:
                        not_with_mid[movieid]=1;
                        
    ratings1 = defaultdict(float)
    ratings2 = defaultdict(float)
    
    user_num = 5564 #len(nt)
    
    for movieid in movieidset:
        if movieid == mid:
            continue
        ratings1[movieid] = float(with_mid[movieid])/float(mid_count)
        try:
            ratings2[movieid] = (float(with_mid[movieid])/float(mid_count))/(float(not_with_mid[movieid])/(float(user_num-mid_count)))
            '''
            if movieid==1891:
                print "id =",movieid
                print "id & mid =",with_mid[movieid]
                print "mid_count =",mid_count
                print "rating1 =",ratings1[movieid]
                print "id & !mid =",not_with_mid[movieid]
                print "!mid_count =",len(nt)-mid_count
                print "id & !mid / !mid_count = ",(float(not_with_mid[movieid])/(float(len(nt)-mid_count)))
                print "rating2 =",ratings2[movieid]
                '''
        except Exception as inst:
            print type(inst)
            print inst.args
            print inst
            print movieid,with_mid[movieid],mid_count,not_with_mid[movieid],user_num,counts[movieid]
            return
            
    sorted1 = sorted(ratings1.iteritems(), key=lambda (k,v): v,reverse=True)
    sorted2 = sorted(ratings2.iteritems(), key=lambda (k,v): v,reverse=True)
    
    #print mid,sorted1[0],sorted1[1],sorted1[2],sorted1[3],sorted1[4]
    '''
    print mid,
    for i in range(0,5):
        print (",{0},{1:.2f}".format(sorted1[i][0],sorted1[i][1])),
    print
    '''
    print mid,
    for i in range(0,5):
        print (",{0},{1:.2f}".format(sorted2[i][0],sorted2[i][1])),
    print

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: recsys1.py imput_file\n")
        sys.exit(2)
    try:
        input_file = file(sys.argv[1],"r")
    except IOError:
        sys.stderr.write("Error read input file %s.\n" % arg)
        sys.exit(1)

    readdata(input_file)
    #count(11)
    count(786)
    count(36955)
    count(1894)
