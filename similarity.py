# import everything else
import sklearn

# At its proper place
if calling for similarity:
staticList = extract all data from list1
scaled_tempo = [float(x)/float(max(staticList[23]))for x in staticList[23]]
staticList[23]=scaled_tempo
uri = staticList[24]
newdata = [staticList[3],staticList[4],staticList[5],staticList[6],staticList[7],staticList[8],staticList[9],staticList[10],staticList[11],staticList[12],staticList[13],staticList[14],staticList[15],staticList[16],staticList[17],staticList[18],staticList[19],staticList[20],staticList[21],staticList[22],staticList[23]]
listForSim = np.transpose(newdata)
def similarity(pickedindex,listForSim):
    similarity = sklearn.metrics.pairwise.cosine_similarity(listForSim,Y=None,dense_output=True)
    score = similarity[pickedindex]
    rank = score1.argsort()
    return(rank[-2])