import rpa as r
import csv

r.init(visual_automation = True)

# use url('your_url') to go to web page, url() returns current URL
r.url('http://rpachallenge.com/')
r.wait(5.1)

r.hover('start.png') # mover mouse para o botao start
r.click('start.png') # clicar no botao start


def scroll_down():
  r.hover('arrow-down.png')
  r.click('arrow-down.png')
  r.click('arrow-down.png')
  r.click('arrow-down.png')

def scroll_up():
  r.hover('arrow-up.png')
  r.click('arrow-up.png')
  r.click('arrow-up.png')
  r.click('arrow-up.png')


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
    
      if(not r.hover('address.png')):
        scroll_down()
        if(not r.hover('address.png')):
          scroll_up()
          r.hover('address.png')
      r.click('address.png') # selecionar address
      r.type('Address', endereco + ", " + numero + " - " +bairro) # inserir texto do address

      if(not r.hover('email.png')):
        scroll_down()
        if(not r.hover('email.png')):
          scroll_up()
          r.hover('email.png')
      r.click('email.png') # selecionar email
      r.type('email', email) # inserir texto do email
      
      if(not r.hover('phone-number.png')):
        scroll_down()
        if(not r.hover('phone-number.png')):
          scroll_up()
          r.hover('phone-number.png')
      r.click('phone-number.png') # selecionar phone-number
      r.type('Phone Number', celular) # inserir texto do phone-number

      if(not r.hover('company-name.png')):
        scroll_down()
        if(not r.hover('company-name.png')):
          scroll_up()
          r.hover('company-name.png')
      r.click('company-name.png') # selecionar company-name
      r.type('Company Name', signo + " " + cor) # inserir texto do company-name

      if(not r.hover('first-name.png')):
        r.hover('arrow-down.png')
        r.click('arrow-down.png') 
        r.click('arrow-down.png') 
        r.click('arrow-down.png') 
        if(not r.hover('first-name.png')):
          scroll_up()
          r.hover('first-name.png')
      r.click('first-name.png') # selecionar name
      r.type('First Name', name) # inserir texto do name

      if(not r.hover('last-name.png')):
        scroll_down()
        if(not r.hover('last-name.png')):
          scroll_up()
          r.hover('last-name.png')
      r.click('last-name.png') # selecionar lastname
      r.type('Last Name', lastname) # inserir texto do lastname
      
      if(not r.hover('role-in-company.png')):
        scroll_down()
        if(not r.hover('role-in-company.png')):
          scroll_up()
          r.hover('role-in-company.png')
      r.click('role-in-company.png') # selecionar role-in-company
      r.type('Role in Company', signo ) # inserir texto do role-in-company


      # r.wait(6.6)

      if(not r.hover('submit.png')):
        scroll_down()
        if(not r.hover('submit.png')):
          scroll_up()
          r.hover('submit.png')
      r.click('submit.png') 
      
read_and_iterate_csv()

r.close()

