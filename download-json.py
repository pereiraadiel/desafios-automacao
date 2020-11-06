import rpa as r

r.init(visual_automation = True)
r.url("https://www.4devs.com.br/gerador_de_pessoas")

def click(times, element):
  for i in range(1, times+1):
    r.click(element) 


r.hover('arrow-down.png')
click(6, 'arrow-down.png')

r.hover('select-number-of-persons.png')
click(1, 'select-number-of-persons.png')
r.type('6. Gerar quantas pessoas? (Máx.: 30)', '0')

r.hover('generate-person.png')
click(1, 'generate-person.png')

r.hover('download-button.png')
click(1,'download-button.png')

r.wait(5)

r.close()