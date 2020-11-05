import json
import csv

# abrir arquivo para leitura
def read_json():
  with open('reference.json', 'r', encoding='utf-8') as file:
    return json.load(file)

# salvar arquivo csv
def save_csv(persons):
  with open('persons.csv', 'w', newline='') as file:
    output= csv.writer(file)
    output.writerow(['nome', 'signo', 'email', 'endereco', 'numero', 'bairro', 
    'celular', 'cor']);
    for person in persons: 
      person = [person['nome'], person['signo'],
        person['email'], person['endereco'],
        person['numero'], person['bairro'],
        person['celular'], person['cor']]
      output.writerow(person) 

# ler arquivo
persons = read_json()

# pessoas com mais de 30 anos:
print("\n===> Pessoas com mais de 30 anos:\n")
for person in persons:
  if(person['idade'] > 30):
    print("\t %s" %(person['nome']))

# homens que gostam de vermelho:
print("\n===> Homens que gostam de vermelho:\n")
for person in persons:
  if(person['sexo'] == "Masculino" and person['cor'] == "vermelho"):
    print( "\tnome: %s" %(person['nome']), "| idade: %s anos!" %(person['idade']))

# salvar csv:
save_csv(persons)