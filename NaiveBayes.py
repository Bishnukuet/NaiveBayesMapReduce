from pymongo import MongoClient
import os as OS
from codecs import encode, decode
from bson.code import Code

import math
'''
'''
#read files and insert into Database



def getallPDFs(Path):
    fileList=list()
    dirList=OS.listdir(Path)
    for deep1path in dirList:
        deep2path=OS.path.join(Path,deep1path)
        if OS.path.isdir(deep2path):
            getallPDFs(deep2path)
        else:
            fileList.append(deep2path)
    return fileList




def insertItems(path,dbHandle):

    dbHandle.drop()
    files=getallPDFs(path)

    for text in files:
        doc=list()
        item={}
        C1=0
        C2=0
        if text.__contains__('fortnow'):
            C1=1
        else:
            C2=1
        lines=open(text).readlines()
        stripChars='<>?/)!=([]{};:-"\'.%,#@* \n\t'
        for line in lines:
            tokens=line.strip(stripChars).split()
            for token in tokens:
                word = decode (token.strip(stripChars) , 'latin2' ,'ignore' )
                if len(word)>=4 and word.isalpha():
                    doc.append(word.lower())
        item['content']=doc
        item['C1']=C1
        item['C2']=C2
        dbHandle.insert_one(item)


def performMapReduce(dbHandle,map,reduce,collection,):
    result=dbHandle.map_reduce(map,reduce,collection)
    #for r in result.find():
    #    print r
    return result


def trainNaiveBayes():
    N=None
    Nc1=None
    N2=None

    V=None
    pass
def testnaiveBayes(resultDb,testDb,param):
    for ex in testDb.find():
        prob={'C1':0.0,'C2':0.0}
        prob['C1']+=math.log(param['Nc1']/param['N'])
        prob['C2']+=math.log(param['Nc2']/param['N'])
        words=ex['content']
        for word in words:
            q=resultDb.find_one({'_id':word})
            if not q is None:
                Fc1=q['value']['C1']+1
                Fc2=q['value']['C2']+1
            else:
                Fc1=1
                Fc2=1
            prob['C1']+=math.log(Fc1/(param['Tc1']+param['V']))
            print Fc1/(param['Tc1']+param['V'])
            prob['C2']+=math.log(Fc2/(param['Tc2']+param['V']))
            print Fc2/(param['Tc2']+param['V'])
        testData.find_one_and_update(ex,{'$set':{'pred':{'Pc1':prob['C1'],'Pc2':prob['C2']}}})



if __name__ == '__main__':
    client=MongoClient()['NaiveBayesDB']

    trainData=client.training
    testData=client.testing


    testFiles="./TestSet"#"F:\Semester 3 UPB\Information Retrieval\Labs\session6\TestSet"
    trainFiles="./TrainSet"#"F:\Semester 3 UPB\Information Retrieval\Labs\session6\TrainSet"
    insertItems(trainFiles,trainData) #insert the training data
    insertItems(testFiles,testData)   #insert Testting Data

    #parameter={'N':60,'Nc1':30,'Nc2':30,'Tc1':0,'Tc2':0,'V':0}
    #trainNaiveBayes()
    #testnaiveBayes()
    #for item in trainData.find():
    #    print item['content']

    mapfunc=Code(open("Map.js",'r').read())
    reducefunc=Code(open("Reduce.js",'r').read())
    client.result.drop()
    result=performMapReduce(trainData,mapfunc,reducefunc,'result')

    '''
    mapfunc=Code(open('MapParameter.js','r').read())
    reducefunc=Code(open('ReduceParam.js','r').read())
    param=performMapReduce(client.result,mapfunc,reducefunc,'param1')
    print [c for c in param.find()]
    '''

    mapfunc=Code(open('Map1.js','r').read())
    reducefunc=Code(open('Reduce1.js','r').read())
    param=performMapReduce(trainData,mapfunc,reducefunc,'param2')

    p=[c for c in param.find()]
    parameters=p[0]['value']

    testnaiveBayes(client.result,testData,parameters);

    mapfunc=Code(open('MapConf.js','r').read())
    reducefunc=Code(open('ReduceConf.js','r').read())
    confusion=performMapReduce(testData,mapfunc,reducefunc,'confusion')

    print confusion.find_one()


    '''
    for f in testData.find():
        print f['pred']
    '''

