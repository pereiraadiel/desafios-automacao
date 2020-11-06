import rpa as r
import csv

r.init(visual_automation = True)

# use url('your_url') to go to web page, url() returns current URL
r.url('http://rpachallenge.com/')
r.wait(5.1)

r.hover('imagesstart.png') # mover mouse para o botao start
r.click('images/start.png') # clicar no botao start


def scroll_down():
  r.hover('imagesarrow-down.png')
  r.click('images/arrow-down.png')
  r.click('images/arrow-down.png')
  r.click('images/arrow-down.png')

def scroll_up():
  r.hover('imagesarrow-up.png')
  r.click('images/arrow-up.png')
  r.click('images/arrow-up.png')
  r.click('images/arrow-up.png')


def read_and_iterate_csv():
  with open('persons.csv', 'r') as file:
    inputfile = csv.reader(file)
    next(inputfile) # pular cabecalhos ['nome','signo','email','endereco',
    # 'numero','bairro', 'celular', 'cor']
    for line in inputfile:
      # print (line)
      name = line[0].split(' ')[0]
      lastname = line[0].split(name + ' ')[1]
      signo = line[1]
      email = line[2]
      endereco = line[3]
      numero = line[4]
      bairro = line[5]
      celular = line[6]
      cor = line[7]
    
      if(not r.hover('imagesaddress.png')):
        scroll_down()
        if(not r.hover('imagesaddress.png')):
          scroll_up()
          r.hover('imagesaddress.png')
      r.click('images/address.png') # selecionar address
      r.type('Address', endereco + ", " + numero + " - " +bairro) # inserir texto do address

      if(not r.hover('imagesemail.png')):
        scroll_down()
        if(not r.hover('imagesemail.png')):
          scroll_up()
          r.hover('imagesemail.png')
      r.click('images/email.png') # selecionar email
      r.type('email', email) # inserir texto do email
      
      if(not r.hover('imagesphone-number.png')):
        scroll_down()
        if(not r.hover('imagesphone-number.png')):
          scroll_up()
          r.hover('imagesphone-number.png')
      r.click('images/phone-number.png') # selecionar phone-number
      r.type('Phone Number', celular) # inserir texto do phone-number

      if(not r.hover('imagescompany-name.png')):
        scroll_down()
        if(not r.hover('imagescompany-name.png')):
          scroll_up()
          r.hover('imagescompany-name.png')
      r.click('images/company-name.png') # selecionar company-name
      r.type('Company Name', signo + " " + cor) # inserir texto do company-name

      if(not r.hover('imagesfirst-name.png')):
        r.hover('imagesarrow-down.png')
        r.click('images/arrow-down.png') 
        r.click('images/arrow-down.png') 
        r.click('images/arrow-down.png') 
        if(not r.hover('imagesfirst-name.png')):
          scroll_up()
          r.hover('imagesfirst-name.png')
      r.click('images/first-name.png') # selecionar name
      r.type('First Name', name) # inserir texto do name

      if(not r.hover('imageslast-name.png')):
        scroll_down()
        if(not r.hover('imageslast-name.png')):
          scroll_up()
          r.hover('imageslast-name.png')
      r.click('images/last-name.png') # selecionar lastname
      r.type('Last Name', lastname) # inserir texto do lastname
      
      if(not r.hover('imagesrole-in-company.png')):
        scroll_down()
        if(not r.hover('imagesrole-in-company.png')):
          scroll_up()
          r.hover('imagesrole-in-company.png')
      r.click('images/role-in-company.png') # selecionar role-in-company
      r.type('Role in Company', signo ) # inserir texto do role-in-company


      # r.wait(6.6)

      if(not r.hover('imagessubmit.png')):
        scroll_down()
        if(not r.hover('imagessubmit.png')):
          scroll_up()
          r.hover('imagessubmit.png')
      r.click('images/submit.png') 
      
read_and_iterate_csv()

r.close()

