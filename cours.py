els = {'numero': ('id', 'numeroVoie'),
       'voie': ('name', "nomVoie"),
       'ville': ('id', "ville"),
       'code_postal': ('id', "codePostal")}

tuple_test = ('id', 'numeroVoieCELUILA')

list_test = ["id", "numVoie", "toto", "on s'en fous", tuple_test]
liste2 = ["un autre test"]

print(els["numero"])
print(els.keys())

els["numero"] = "toto"
for key, value in els.items():
       print(key, value)

x = 12
print(x, type(x))
x = float(x)
print(x, type(x))

if type(x) == float:
       x = int(x)
       x = str(x)
else:
       x = str(x)
print(x, type(x))

"""el_info[2] = str(el_info[2])
print(el_info[2], type(el_info[2]))
el_info[2] = float(el_info[2])
print(el_info[2], type(el_info[2]))

if type(el_info[2]) == float:
       el_info[2] = int(el_info[2])
       el_info[2] = str(el_info[2])
else:
    el_info[2] = str(el_info[2])
print(el_info[2], type(el_info[2])"""
