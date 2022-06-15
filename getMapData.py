from nrfaApi import *
import pandas as pd

indexCol = []
Bywell = getMapData('23001')
Bywelldf= pd.DataFrame(data=Bywell)
for value in Bywelldf["Value"]:
    indexCol.append(1)
Bywelldf["Index"] = indexCol
Bywelldf = Bywelldf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
East_Linton = getMapData('20001')
East_Lintondf= pd.DataFrame(data=East_Linton)
for value in East_Lintondf["Value"]:
    indexCol.append(1)
East_Lintondf["Index"] = indexCol
East_Lintondf = East_Lintondf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Spilmersford = getMapData('20003')
Spilmersforddf= pd.DataFrame(data=Spilmersford)
for value in Spilmersforddf["Value"]:
    indexCol.append(1)
Spilmersforddf["Index"] = indexCol
Spilmersforddf = Spilmersforddf.pivot(index="Index", columns="Key", values="Value")


indexCol = []
Haydon_Bridge = getMapData('23004')
Haydon_Bridgedf= pd.DataFrame(data=Haydon_Bridge)
for value in Haydon_Bridgedf["Value"]:
    indexCol.append(1)
Haydon_Bridgedf["Index"] = indexCol
Haydon_Bridgedf = Haydon_Bridgedf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Featherstone = getMapData('23006')
Featherstonedf= pd.DataFrame(data=Featherstone)
for value in Featherstonedf["Value"]:
    indexCol.append(1)
Featherstonedf["Index"] = indexCol
Featherstonedf = Featherstonedf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Alston = getMapData('23009')
Alstondf= pd.DataFrame(data=Alston)
for value in Alstondf["Value"]:
    indexCol.append(1)
Alstondf["Index"] = indexCol
Alstondf = Alstondf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Reaverhill = getMapData('23003')
Reaverhilldf= pd.DataFrame(data=Reaverhill)
for value in Reaverhilldf["Value"]:
    indexCol.append(1)
Reaverhilldf["Index"] = indexCol
Reaverhilldf = Reaverhilldf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Tarset = getMapData('23005')
Tarsetdf= pd.DataFrame(data=Tarset)
for value in Tarsetdf["Value"]:
    indexCol.append(1)
Tarsetdf["Index"] = indexCol
Tarsetdf = Tarsetdf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Kielder_temporary = getMapData('23014')
Kielder_temporarydf= pd.DataFrame(data=Kielder_temporary)
for value in Kielder_temporarydf["Value"]:
    indexCol.append(1)
Kielder_temporarydf["Index"] = indexCol
Kielder_temporarydf = Kielder_temporarydf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Barrasford = getMapData('23014')
Barrasforddf= pd.DataFrame(data=Barrasford)
for value in Barrasforddf["Value"]:
    indexCol.append(1)
Barrasforddf["Index"] = indexCol
Barrasforddf = Barrasforddf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Uglydub = getMapData('23014')
Uglydubdf= pd.DataFrame(data=Uglydub)
for value in Uglydubdf["Value"]:
    indexCol.append(1)
Uglydubdf["Index"] = indexCol
Uglydubdf = Uglydubdf.pivot(index="Index", columns="Key", values="Value")


indexCol = []
Chester_le_Street = getMapData('24009')
Chester_le_Streetdf= pd.DataFrame(data=Chester_le_Street)
for value in Chester_le_Streetdf["Value"]:
    indexCol.append(1)
Chester_le_Streetdf["Index"] = indexCol
Chester_le_Streetdf = Chester_le_Streetdf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Darlington_Broken_Scar = getMapData('25001')
Darlington_Broken_Scardf= pd.DataFrame(data=Darlington_Broken_Scar)
for value in Darlington_Broken_Scardf["Value"]:
    indexCol.append(1)
Darlington_Broken_Scardf["Index"] = indexCol
Darlington_Broken_Scardf = Darlington_Broken_Scardf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Dent_Bank = getMapData('25002')
Dent_Bankdf= pd.DataFrame(data=Dent_Bank)
for value in Dent_Bankdf["Value"]:
    indexCol.append(1)
Dent_Bankdf["Index"] = indexCol
Dent_Bankdf = Dent_Bankdf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Barnard_Castle = getMapData('25008')
Barnard_Castledf= pd.DataFrame(data=Barnard_Castle)
for value in Barnard_Castledf["Value"]:
    indexCol.append(1)
Barnard_Castledf["Index"] = indexCol
Barnard_Castledf = Barnard_Castledf.pivot(index="Index", columns="Key", values="Value")

indexCol = []
Low_Moor = getMapData('25009')
Low_Moordf= pd.DataFrame(data=Low_Moor)
for value in Low_Moordf["Value"]:
    indexCol.append(1)
Low_Moordf["Index"] = indexCol
Low_Moordf = Low_Moordf.pivot(index="Index", columns="Key", values="Value")


indexCol = []
Middleton_Teesdale = getMapData('25018')
Middleton_Teesdaledf= pd.DataFrame(data=Middleton_Teesdale)
for value in Middleton_Teesdaledf["Value"]:
    indexCol.append(1)
Middleton_Teesdaledf["Index"] = indexCol
Middleton_Teesdaledf = Middleton_Teesdaledf.pivot(index="Index", columns="Key", values="Value")


indexCol = []
Cow_Green_Reservoir = getMapData('25023')
Cow_Green_Reservoirdf= pd.DataFrame(data=Cow_Green_Reservoir)
for value in Cow_Green_Reservoirdf["Value"]:
    indexCol.append(1)
Cow_Green_Reservoirdf["Index"] = indexCol
Cow_Green_Reservoirdf = Cow_Green_Reservoirdf.pivot(index="Index", columns="Key", values="Value")

frames = [Bywelldf, East_Lintondf, Spilmersforddf, Chester_le_Streetdf, Darlington_Broken_Scardf, Dent_Bankdf, 
Barnard_Castledf, Low_Moordf, Middleton_Teesdaledf, Cow_Green_Reservoirdf, 
Haydon_Bridgedf, Featherstonedf , Alstondf, Reaverhilldf, Tarsetdf, Kielder_temporarydf, Barrasforddf, Uglydubdf]
MapData = pd.concat(frames)
print(MapData)