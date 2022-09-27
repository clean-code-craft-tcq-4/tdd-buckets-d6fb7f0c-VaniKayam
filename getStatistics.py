import numpy as np


def convertCurrentsamplesToArrayInput( currentSample):
    currentSampleArr = np.array(currentSample)
    return currentSampleArr
    
def getInputTypeOfCurrentSamples( currentSampleArr): 
    for x in currentSampleArr:
        if  type(x) == np.int32:
            pass
        else:
            return False                
    return True  

def getCurrentSampleReadingsAsConsecutiveNumbers( currentSampleArr):
    currentSampleArr.sort()
    return currentSampleArr        
   
def getConsecutiveGroupsWithNumberOfReadings( currentSampleArr):
    ReadingCount=0
    index=0
    start = end = None
    data = " "
    
    while(index < len(currentSampleArr)-1):
        
        value = getRangeWithValue(currentSampleArr, start, end, ReadingCount, index)
        start = value[0]
        end = value[1]
        ReadingCount = value[2]
                  
        if(end!=None):
            data = getFormattedRangeAndReadingsCountOfCurrentSampleArr(currentSampleArr, start, end, ReadingCount, data, index)             
            ReadingCount=0
            start = end = None        
        index+=1   
    
    return data

def getStartValueOfCurrentSampleRange( currentSampleArr,start,end,ReadingCount,index):       
    
    ReadingCount+=1
    if(start == None ):
        start = currentSampleArr[index]        

    if(index == len(currentSampleArr)-2):
        end=currentSampleArr[index+1]
        ReadingCount+=1         
    return start,end,ReadingCount


def getEndValueOfCurrentSampleRange( currentSampleArr,start,end,ReadingCount,index):
    if(start != None):
        end = currentSampleArr[index]
        ReadingCount+=1    
    return start,end,ReadingCount
        
def getFormattedRangeAndReadingsCountOfCurrentSampleArr( currentSampleArr,start,end,ReadingCount,data,index):
   readingsFormat = f' [{start}-{end}, {ReadingCount}] '
   data+=readingsFormat
   return data
         

def getRangeWithValue( currentSampleArr,start,end,ReadingCount,index):
    if((currentSampleArr[index]==currentSampleArr[index+1]) or (((currentSampleArr[index])+1) == currentSampleArr[index+1])):
        value = getStartValueOfCurrentSampleRange(currentSampleArr,start,end,ReadingCount,index)
        start = value[0]
        end = value[1]
        ReadingCount = value[2]
       
    else:
        value = getEndValueOfCurrentSampleRange(currentSampleArr,start,end,ReadingCount,index)
        start = value[0]
        end = value[1]
        ReadingCount = value[2]         
    return start,end,ReadingCount
        
   
def print_on_console(message):
    print(message)
