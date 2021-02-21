import requests
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	print('''\033[96m██╗      ██████╗ ███████╗████████╗              
██║     ██╔═══██╗██╔════╝╚══██╔══╝              
██║     ██║   ██║███████╗   ██║                 
██║     ██║   ██║╚════██║   ██║                 
███████╗╚██████╔╝███████║   ██║                 
╚══════╝ ╚═════╝ ╚══════╝   ╚═╝                 
                                                
██████╗ ██╗      █████╗  ██████╗ █████╗ ███████╗
██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗██╔════╝
██████╔╝██║     ███████║██║     ███████║███████╗
██╔═══╝ ██║     ██╔══██║██║     ██╔══██║╚════██║
██║     ███████╗██║  ██║╚██████╗██║  ██║███████║
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝\033[m
	              \033[92mBY: leezyAFK\033[m   ''')

def main():
	
	clear()
	banner()
	
	placa_input = input('\033[34mDigite a placa a ser consultada: \033[m').upper()
	
	request = requests.get('https://apicarros.com/v2/consultas/{}/f63e1e63dd231083d38ce929984aac7d'.format(placa_input), verify=False)
	
	clear()
	
	placa_data = request.json()
	
	if 'message' not in placa_data:
		
		clear()
		banner()
		
		print('\033[96m >>> VEÍCULO ENCONTRADO <<<\033[m')
		print('')
		print('\033[34mCHASSI > {}\033[m'.format(placa_data['chassi']))
		print('\033[34mMODELO > {}\033[m'.format(placa_data['modelo']))
		print('\033[34mMARCA > {}\033[m'.format(placa_data['marca']))
		print('\033[34mCOR > {}\033[m'.format(placa_data['cor']))
		print('\033[34mANO > {}\033[m'.format(placa_data['ano']))
		print('\033[34mPLACA > {}\033[m'.format(placa_data['placa']))
		print('\033[34mMUNICÍPIO > {}\033[m'.format(placa_data['municipio']))
		print('\033[34mUF > {}\033[m'.format(placa_data['uf']))
	
	else:
		print('\033[31m>>> PLACA INVÁLIDA <<<\033[m')
		exit()
		
	option = input('\033[32mDeseja fazer uma nova consulta?[y/n]').lower()
	
	if option == 'y':
				clear()
				main()
	else:
				exit()
				
if __name__ == '__main__':
	main()
	

	
	
	
	
	
	
		