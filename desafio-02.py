import rpa as r

r.init(visual_automation = True)
r.url("https://www.4devs.com.br/gerador_de_pessoas")

def click(times, element):
  for i in range(1, times+1):
    r.click(element) 


r.hover('images/arrow-down.png')
click(6, 'images/arrow-down.png')

r.hover('images/select-number-of-persons.png')
click(1, 'images/select-number-of-persons.png')
r.type('6. Gerar quantas pessoas? (Máx.: 30)', '0')

r.hover('images/generate-person.png')
click(1, 'images/generate-person.png')

r.hover('images/download-button.png')
click(1,'images/download-button.png')

r.wait(5)

r.close()