from re import U
import mysql.connector
import time, pandas
import apiPI

mydb = mysql.connector.connect(
  host="34.236.250.118",
  user="root",
  password="Smart",
  database="MeshliumDB"
)
cursor = mydb.cursor()

query = ("SELECT sensor, value, timestamp, id_wasp FROM sensorParser")

cursor.execute(query)

content = pandas.DataFrame(cursor, columns=["sensor","valor","data","nome"])

LUX = content[(content.nome == "Horta-C") & (content.sensor == "LUX")]["valor"].tolist()
PRES = content[(content.nome == "Horta-C") & (content.sensor == "PRES")]["valor"].tolist()
HUM = content[(content.nome == "Horta-C") & (content.sensor == "HUM")]["valor"].tolist()
UMDB = content[(content.nome == "Horta-C") & (content.sensor == "HUMB")]["valor"].tolist()
TC = content[(content.nome == "Horta-C") & (content.sensor == "TC")]["valor"].tolist()
ANE = content[(content.nome == "Horta-C") & (content.sensor == "ANE")]["valor"].tolist()
SOIL_C = content[(content.nome == "Horta-C") & (content.sensor == "SOIL_C")]["valor"].tolist()
LW = content[(content.nome == "Horta-C") & (content.sensor == "LW")]["valor"].tolist()
PLV1 = content[(content.nome == "Horta-C") & (content.sensor == "PLV1")]["valor"].tolist()
PLV2 = content[(content.nome == "Horta-C") & (content.sensor == "PLV2")]["valor"].tolist()
PLV3 = content[(content.nome == "Horta-C") & (content.sensor == "PLV3")]["valor"].tolist()
STR = content[(content.nome == "Horta-C") & (content.sensor == "STR")]["valor"].tolist()
BAT = content[(content.nome == "Horta-C") & (content.sensor == "BAT")]["valor"].tolist()

LUX_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "LUX")]["valor"].tolist()
PRES_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "PRES")]["valor"].tolist()
HUM_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "HUM")]["valor"].tolist()
UMDB_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "HUMB")]["valor"].tolist()
TC_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "TC")]["valor"].tolist()
LW_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "LW")]["valor"].tolist()
BAT_T = content[(content.nome == "Telhado-Intelige") & (content.sensor == "BAT")]["valor"].tolist()

BaT =BAT[-1]
Lumi = LUX[-1]
Pres = PRES[-1]
Umi = HUM[-1]
Umi_soil_b = UMDB[-1]
TempC = TC[-1]
Ane = ANE[-1]
SoloC = SOIL_C[-1]
Lw = LW[-1]
PlvHA = PLV1[-1]
PlvPH = PLV2[-1]
PlvD = PLV3[-1]
StR = STR[-1]

LuX_T = LUX_T[-1]
Pres_T = PRES_T[-1]
HuM_T = HUM_T[-1]
HuMB_T = UMDB_T[-1]
Tc_T = TC_T[-1]
Lw_T = LW_T[-1]
BaT_T = BAT_T[-1]

############################################################################################

# #print(Umi_soil_b)
ptm_soil_umi_T = apiPI.getPiPoints('Telhado_Inteligente_soil_umi')[0]
print(apiPI.setValue(ptm_soil_umi_T['WebId'], HuMB_T))

# #print(BaT)
ptM_BAT_T = apiPI.getPiPoints('Telhado_Inteligente_BaT')[0]
print(apiPI.setValue(ptM_BAT_T['WebId'], BaT_T))

# #print(LUX)
ptM_LUX_T = apiPI.getPiPoints('Telhado_Inteligente_LuX')[0]
print(apiPI.setValue(ptM_LUX_T['WebId'], LuX_T))

# # print(PRES)
ptM_PRES_T = apiPI.getPiPoints('Telhado_Inteligente_Pres')[0]
print(apiPI.setValue(ptM_PRES_T['WebId'], Pres_T))

# # print(HUM)
ptM_HUM_T = apiPI.getPiPoints('Telhado_Inteligente_Hum')[0]
print(apiPI.setValue(ptM_HUM_T['WebId'], HuM_T))

#print(TC)
ptM_TC_T = apiPI.getPiPoints('Telhado_Inteligente_TC')[0]
print(apiPI.setValue(ptM_TC_T['WebId'], Tc_T))

# # print(LW)
ptM_LW_T = apiPI.getPiPoints('Telhado_Inteligente_Lw')[0]
print(apiPI.setValue(ptM_LW_T['WebId'], Lw_T))



############################################################################################
# #print(Umi_soil_b)
ptm_soil_umi = apiPI.getPiPoints('Horta_Inteligente_Umi_soil_b')[0]
print(apiPI.setValue(ptm_soil_umi['WebId'], Umi_soil_b))

# #print(BaT)
ptM_BAT = apiPI.getPiPoints('Horta_Inteligente_BaT')[0]
print(apiPI.setValue(ptM_BAT['WebId'], BaT))

# #print(LUX)
ptM_LUX = apiPI.getPiPoints('Horta_Inteligente_Lux')[0]
print(apiPI.setValue(ptM_LUX['WebId'], Lumi))

# # print(PRES)
ptM_PRES = apiPI.getPiPoints('Horta_Inteligente_Pres')[0]
print(apiPI.setValue(ptM_PRES['WebId'], Pres))

# # print(HUM)
ptM_HUM = apiPI.getPiPoints('Horta_Inteligente_Hum')[0]
print(apiPI.setValue(ptM_HUM['WebId'], Umi))

#print(TC)
ptM_TC = apiPI.getPiPoints('Horta_Inteligente_TC')[0]
print(apiPI.setValue(ptM_TC['WebId'], TempC))

# # print(ANE)
ptM_ANE = apiPI.getPiPoints('Horta_Inteligente_Ane')[0]
print(apiPI.setValue(ptM_ANE['WebId'], Ane))

# # print(SoloC)
ptM_SOIL_C = apiPI.getPiPoints('Horta_Inteligente_Soil')[0]
print(apiPI.setValue(ptM_SOIL_C['WebId'], SoloC))

# # print(LW)
ptM_LW = apiPI.getPiPoints('Horta_Inteligente_Lw')[0]
print(apiPI.setValue(ptM_LW['WebId'], Lw))

# # print(PLV1)
ptM_PLV1 = apiPI.getPiPoints('Horta_Inteligente_PlvHA')[0]
print(apiPI.setValue(ptM_PLV1['WebId'], PlvHA))

# # print(PLV2)
ptM_PLV2 = apiPI.getPiPoints('Horta_Inteligente_PlvPH')[0]
print(apiPI.setValue(ptM_PLV2['WebId'], PlvPH))

# # print(PLV3)
ptM_PLV3 = apiPI.getPiPoints('Horta_Inteligente_PlvD')[0]
print(apiPI.setValue(ptM_PLV3['WebId'], PlvD))


# # print(StR)
ptM_StR = apiPI.getPiPoints('Horta_Inteligente_StR')[0]
print(apiPI.setValue(ptM_StR['WebId'], StR))