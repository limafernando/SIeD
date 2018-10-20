import pandas as pd
import csv
with open('MICRODADOS_ENADE_2014.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('MICRODADOS_ENADE_2014.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('title', 'intro'))
        writer.writerows(lines)

arq = pd.read_csv('MICRODADOS_ENADE_2014.csv', sep=';')

cols = [
'NU_ITEM_OFG'
,'NU_ITEM_OFG_Z'
,'NU_ITEM_OFG_X'
,'NU_ITEM_OFG_N'
,'NU_ITEM_OCE'
,'NU_ITEM_OCE_Z'
,'NU_ITEM_OCE_X'
,'NU_ITEM_OCE_N'
,'DS_VT_GAB_OFG_ORIG'
,'DS_VT_GAB_OFG_FIN'
,'DS_VT_GAB_OCE_ORIG'
,'DS_VT_GAB_OCE_FIN'
,'DS_VT_ESC_OFG'
,'DS_VT_ACE_OFG'
,'DS_VT_ESC_OCE'
,'DS_VT_ACE_OCE'
,'TP_PRES'
,'TP_PR_GER'
,'TP_PR_OB_FG'
,'TP_PR_DI_FG'
,'TP_PR_OB_CE'
,'TP_PR_DI_CE'
,'TP_SFG_D1'
,'TP_SFG_D2'
,'TP_SCE_D1'
,'TP_SCE_D2'
,'TP_SCE_D3'
,'NT_GER'
,'NT_FG'
,'NT_OBJ_FG'
,'NT_DIS_FG'
,'NT_FG_D1'
,'NT_FG_D1_PT'
,'NT_FG_D1_CT'
,'NT_FG_D2'
,'NT_FG_D2_PT'
,'NT_FG_D2_CT'
,'NT_CE'
,'NT_OBJ_CE'
,'NT_DIS_CE'
,'NT_CE_D1'
,'NT_CE_D2'
,'NT_CE_D3'
,'QE_I01'
,'QE_I02'
,'QE_I03'
,'QE_I04'
,'QE_I05'
,'QE_I06'
,'QE_I07'
,'QE_I08'
,'QE_I09'
,'QE_I10'
,'QE_I11'
,'QE_I12'
,'QE_I13'
,'QE_I14'
,'QE_I16'
,'QE_I17'
,'QE_I18'
,'QE_I19'
,'QE_I20'
,'QE_I21'
,'QE_I22'
,'QE_I23'
,'QE_I24'
,'QE_I26'
,'QE_I27'
,'QE_I28'
,'QE_I29'
,'QE_I30'
,'QE_I31'
,'QE_I32'
,'QE_I33'
,'QE_I34'
,'QE_I35'
,'QE_I36'
,'QE_I37'
,'QE_I38'
,'QE_I39'
,'QE_I40'
,'QE_I41'
,'QE_I42'
,'QE_I43'
,'QE_I44'
,'QE_I45'
,'QE_I46'
,'QE_I47'
,'QE_I48'
,'QE_I49'
,'QE_I52'
,'QE_I53'
,'QE_I54'
,'QE_I55'
,'QE_I56'
,'QE_I57'
,'QE_I58'
,'QE_I62'
,'QE_I63'
,'QE_I66'
,'QE_I67'
,'QE_I68',
'QE_I69', 'QE_I70', 'QE_I71', 'QE_I72', 'QE_I73', 'QE_I74',
'QE_I75', 'QE_I76', 'QE_I77', 'QE_I78', 'QE_I79', 'QE_I80', 'QE_I81'
]

for i in range (0, len(cols)):
	arq.drop([cols[i]], axis=1, inplace=True)

#arq.rename(columns={'Unnamed: 0':'CONT'}, inplace=True)

metade = int(len(arq)/2)

arq1 = arq[:metade]
arq2 = arq[metade:]

arq1.to_csv('MICRODADOS_ENADE_2014_NOVO1.csv', sep=';')
arq2.to_csv('MICRODADOS_ENADE_2014_NOVO2.csv', sep=';')

print(arq.columns)