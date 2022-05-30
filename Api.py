import requests
import json
import pandas as pd

base = 'http://environment.data.gov.uk/water-quality'

#region help (Query API)

#  Query API #
def queryAPI(query):
    response = requests.get(query)
    response = response.json()
    return response['items']

#endregion 

#region help (check dictionary and build parameter search)  
def buildSearchParameters(userInputDictionary, entireDictionary):
    if userInputDictionary == None:
        return ''
    elif userInputDictionary.keys() <= entireDictionary.keys():
        parameterString = '?' 
        for key,value in userInputDictionary.items():
            parameterString += key + '=' + value + '&'
        parameterString = parameterString[:-1]
        return parameterString
    else:
        raise('error, item not searchable')
 
#endregion



##########################################################
#Sampling Points
#region help (sampling points)
#userInputDictionary = The key values the user inputs 

#  Get list of Sampling Points #
def getSamplingPoint(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = { 'search': '', 'lat': '', 'long': '', 'easting': '', 'northing': '', 'dist': '', 'area': '', 'subArea': '', 'samplingPointType': '', 'samplingPointStatus': '', '_limit': '' }
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/id/sampling-point' + parameterString)
    
#Samples taken from a sampling point
def getSamplesTakenFromASamplingPoint(SampleID, userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'startDate': '', 'endDate': '', 'year': '', 'purpose': '', 'isComplianceSample': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/id/sampling-point/' + SampleID + '/samples' + parameterString)

#Measurements on samples from a sampling point
def getMeasurementsOnSamplesFromSamplingPoint(SampleID, userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'startDate': '', 'endDate': '', 'year': '', 'purpose': '', 'isComplianceSample': '', 'determinand': '', 'determinandGroup': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/id/sampling-point/' + SampleID + '/measurements' + parameterString)
    
#endregion
##########################################################
#Samples
#region help (samples)
#  Get List of Samples #
def getSamples(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = { 'search': '', 'lat': '', 'long': '', 'easting': '', 'northing': '', 'dist': '', 'area': '', 'subArea': '','startDate': '', 'endDate': '', 'year': '', 'purpose': '', 'isComplianceSample': '', 'samplingPoint': '',  'samplingPointType': '', 'sampledMaterialType': '', '_limit': '' }
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/data/sample' + parameterString)

# Get measurements from a particular sample
def getMeasurementBySampleID(SampleID, userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'determinand': '', 'determinandGroup': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/data/sample/' + SampleID + '/measurements' + parameterString)
#endregion
##########################################################



##########################################################
#Measurements
# region help (measurements) 
#  Get List of Measurements #
def getMeasurements(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'lat': '', 'long': '', 'dist': '', 'easting': '', 'northing': '', 'dist': '', 'area': '', 'subArea': '', 'startDate': '', 'endDate': '', 'year': '', 'purpose': '', 'isComplianceSample': '', 'samplingPoint': '', 'samplingPointType': '', 'sampledMaterialType': '', 'determinand': '',  'determinandGroup': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/data/measurement' + parameterString)
#endregion

##########################################################
#Reference Data
#region help (referenence data)

#  Get List of Determinands #
def getDeterminands(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', 'unit': '', 'unit.label': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/determinands' + parameterString)


#  Get List of Determinand Units #
def getDeterminandsUnits(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/units' + parameterString)

#  Get List of Determinand Groups #
def getDeterminandsGroups(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/determinand-groups' + parameterString)

#  Get list of purposes for which samples can be taken #
def getListPurposes(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/purposes' + parameterString)

#  Get list of Environment Agency areas #
def getEnvironmentAgencyAreas(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/id/ea-area' + parameterString)

#  Get list of Environment Agency sub-areas #
def getEnvironmentAgencySubAreas(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/id/ea-subarea' + parameterString)

#  Get list of types of material that can be sampled #
def getMaterialTypes(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/sampled-material-types' + parameterString)

#  Get list types of sampling point #
def getSamplingPointTypes(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/sampling-point-types' + parameterString)

#  Get list groups of types of sampling point #
def getSamplingPointGroups(userInputDictionary=None):
    #Create new variable to hold entire dictionary of parameters
    entireDictionary = {'search': '', '_limit': ''}
    parameterString = buildSearchParameters(userInputDictionary, entireDictionary)
    return queryAPI(base + '/def/sampling-point-type-groups' + parameterString)
#endregion

#Call Functions and build dataframe 

#getSamplingPoint()

#list1 = getSamplingPoint({'area': '3-35', 'samplingPointType': 'F6'})
#list2= getSamplingPoint({'area': '3-35', 'samplingPointType': 'FA'})

#df1 = pd.DataFrame(data=list1)
#df2 = pd.DataFrame(data=list2)

#frames = [df1, df2]

#result = pd.concat(frames)
#print(result)

#getSamplesTakenFromASamplingPoint('NW-88016299')
#getMeasurementsOnSamplesFromSamplingPoint('NW-88016299')
#getSamples()
#getMeasurementBySampleID('AN-01M02-20150119-1785064')
