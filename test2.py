import pandas as pd
from cadastre import CadastreAPI
import pdb

# exemple de biens
xl = "source/Exemples Biens - SCI SA.csv"


# réécriture : factorisation du code
def liste_biens(csv_file=None):
    if csv_file is None:
        csv_file = xl
    biens = pd.read_csv(filepath_or_buffer=csv_file, sep=";", encoding_errors='ignore')
    return biens[biens.columns[:4]]


def process_num(address):
    out = pd.DataFrame(columns=['NO', 'VOIE'], index=address.index)
    for j, a in address.iterrows():
        num = str(a[0]).strip().split(" ")[0]
        adr = str(a[0]).replace(str(num) + " ", "")
        out['NO'].at[j] = num
        out['VOIE'].at[j] = str(adr).replace("\n", " ").strip()
        # print(num, adr)
    return out


def process_ville(v_cp):
    for j, d in v_cp.iterrows():
        if d['CODE POSTAL'] is not None:
            d['CODE POSTAL'] = str(int(d['CODE POSTAL']))
            v_cp['CODE POSTAL'].at[j] = d['CODE POSTAL']
            if str(d['VILLE']).lower() == 'paris':
                # pdb.set_trace()
                try:
                    v_cp['VILLE'].at[j] = d['VILLE'] + " " + str(d['CODE POSTAL'])[-2:]
                    print(d, ': ', v_cp['VILLE'].at[j])
                except:
                    pass
    return v_cp


def retraitement_adresse(df_info):
    pdf = process_num(pd.DataFrame(data=df_info['ADRESSE']))
    for c in df_info.columns:
        if not (c in pdf.columns):
            pdf[c] = df_info[c]
    return pdf


info = liste_biens()
info = retraitement_adresse(info)
info = process_ville(info)
print(info.head())

# api = CadastreAPI()
# info_3 = api.scraping_all(info_2, cols=['NO', 'VOIE', 'VILLE', 'CODE POSTAL'])
# print(info_3)