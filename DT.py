
from math import log
import numpy as np

def createDataset():
    dataset= [
        [1, 1,'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']]
    labels = ['no sufer','flipers']
    return  dataset, labels

#计算香农熵
def CalcShannonEnt(dataset):
     #进到矩阵的元素个素,也可以np.array(dataset).shape[0])
     numberEntries = len(dataset)
     labelCounts = {}
     #遍历每个一行元素
     for featvec in dataset:
        #得到每一行的最后一个数据，也就是标签值
        currentLabel=featvec[-1]
        #对每个标签的数量进行计数
        if currentLabel not in labelCounts.keys():
             labelCounts[currentLabel] = 0
        else:
            labelCounts[currentLabel] =  labelCounts[currentLabel] +1
     shannonEnt = 0.0
     for key in labelCounts:
        # 1/5
        prob = float(labelCounts[key])/numberEntries
        shannonEnt -=  prob*log(prob,2)
     return  shannonEnt


#根据特症划分数据
def splitDataSet(dataset,aixs,value):
    retDateset = []
    for featVeac in dataset:
         if featVeac[aixs] == value:
            reduceFeat=  featVeac[:aixs]
            #截断
            reduceFeat.extend(featVeac[aixs+1:])
            retDateset.append(reduceFeat)
    return  retDateset


#选择最好的特症
def chooseBestFeatureToSplit(dataset):
    #第一行的数据长度减-
    numFeatuers = len(dataset[0])
    #计算熵
    baseEntropy = CalcShannonEnt(dataset)
    baseInfo = 0.0
    beseFeautre= -1
    for i in range(numFeatuers):
         #行列转换
         fealist=[examples[i] for examples in dataset]
         #得到唯一值
         uniqueVals = set(fealist)
         newEntropy = 0.0
         for value in uniqueVals:
              subDataSet = splitDataSet(dataset,i,value)
              prob=len(subDataSet)/float(len(dataset))
              print(subDataSet)
              newEntropy += prob*CalcShannonEnt(subDataSet)
         newInfo = baseEntropy -newEntropy
         if newInfo>baseInfo:
              baseInfo=newInfo
              beseFeautre=i

    return beseFeautre

def main():
    dataset,labels=createDataset()
    chooseBestFeatureToSplit(dataset)

##[[1, 'no'], [1, 'no']]
#[[1, 'yes'], [1, 'yes'], [0, 'no']]


if __name__ == '__main__':
    main()