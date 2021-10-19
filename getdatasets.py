#"http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/nama_10_gdp?geo=EU28&precision=1&na_item=B1GQ&unit=CP_MEUR&time=2010&time=2011"

from urllib.request import urlopen
import json

url = "https://servicios.ine.es/wstempus/jsstat/ES/DATASET/24387?nult=4"

#Early leavers from education and training by sex and labour status
# edat_lfse_14?filterNonGeo=1&precision=1&sex=T&unit=PC&wstatus=POP&age=Y18-24 

#Pupils and students enrolled by education level, sex, type of institution and intensity of participation
# educ_uoe_enra01?filterNonGeo=1&precision=1&sex=T&unit=NR&worktime=TOTAL 

#Employment rates of young people not in education and training by sex, educational attainment level and years since completion of highest level of education
# edat_lfse_24?filterNonGeo=1&precision=1&sex=T&duration=TOTAL&unit=PC&isced11=TOTAL&time=2014&time=2015&time=2016&time=2017&time=2018&time=2019&age=Y15-34&age=Y18-34&age=Y20-34 



response = urlopen(url)

#data = response.read()
data = json.loads(response.read())

#print(json.dumps(data, indent=4))

f = open("pruebaINE.json", "a") #wb unicode
f.write(json.dumps(data, indent=4))
f.close()