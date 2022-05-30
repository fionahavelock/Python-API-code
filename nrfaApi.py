import requests
import json
import pandas as pd
###################################
#Task of River Flow Api
#get time series data only by id 
#get meta data for each station underneath the - display this underneath a time series graph




base_url = "https://nrfaapps.ceh.ac.uk/nrfa/ws/"
dataObject = "format=json-object"
timeSeries = "time-series?"
metaData = "station-info?"

#region help (Query API)

#  Query API #
def queryAPI(query):
    response = requests.get(query)
    response = response.json()
    return response

#endregion 

#https://nrfaapps.ceh.ac.uk/nrfa/ws/time-series?format=json-object&data-type=cmr&station=45001

#You can only access time series data by station ID. This means we need to allow the user to choose a station ID (location)
def getTimeSeries(flowType, stationNumber):
    jsonData = queryAPI(base_url + timeSeries + dataObject + "&data-type=" + flowType + "&station=" + stationNumber)
    #make every even number a column and every odd number a column
    index = 0
    dataList = []
    #create empty dictionary
    tempDictionary = {}
    for i in jsonData['data-stream']:
        if index % 2 == 0:
            #spilt string to make the time series graph 
            date = i.split("-")
            tempDictionary['Year'] = int(date[0])
            tempDictionary['Month'] = int(date[1])

        else:
            tempDictionary['Value'] = i
            dataList.append(tempDictionary.copy())
        index +=1
    return dataList
    
    
#https://nrfaapps.ceh.ac.uk/nrfa/ws/station-info?station=43009&format=json-object&fields=id,name,grid-reference,lat-long,river
def getMetaData(stationNumber):
    jsonMetaData = queryAPI(base_url + metaData + "station=" + stationNumber + "&" + dataObject + "&fields=id,name,river,location,easting,northing,geology,elevation,urban-extent")
    metaDatafromJson = jsonMetaData['data'][0]
    dataList = []
    tempDictionary ={}
    for key,value in metaDatafromJson.items():
        tempDictionary['Key'] = key
        if value == None:
            value = 'N/A'
        tempDictionary['Value'] = value
        dataList.append(tempDictionary.copy())
    metadataframe = pd.DataFrame(dataList)
    return metadataframe


#return metaDatafromJson 



getTimeSeries('pot-flow', '45001')

#getMetaData("45001")

