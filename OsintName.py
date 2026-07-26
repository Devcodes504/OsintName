import requests
import time
from colorama import Fore,Style,init

banner = fr"""{Fore.MAGENTA}
   ____       _       __  _   __                   
  / __ \_____(_)___  / /_/ | / /___ _____ ___  ___ 
 / / / / ___/ / __ \/ __/  |/ / __ `/ __ `__ \/ _ \
/ /_/ (__  ) / / / / /_/ /|  / /_/ / / / / / /  __/
\____/____/_/_/ /_/\__/_/ |_/\__,_/_/ /_/ /_/\___/ {Style.RESET_ALL}
{Fore.YELLOW} ©Created by NEXUS
                                                {Style.RESET_ALL}   """



def buscar_usuario(usuario, usuario_url, usuario_guion):
    sitios = {
    "Github": f"https://github.com/{usuario_url}",
    "Facebook": f"https://facebook.com/{usuario_url}",
    "Tik Tok": f"https://tiktok.com/@{usuario_url}",
    "Instagram": f"https://instagram.com/{usuario_url}",
    "Twitter/X": f"https://x.com/{usuario_url}",
    "YouTube": f"https://youtube.com/@{usuario_url}",
    "Reddit": f"https://reddit.com/user/{usuario_guion}",
    "Pinterest": f"https://pinterest.com/{usuario_url}",
    "Twitch": f"https://twitch.tv/{usuario_url}",
    "Telegram": f"https://t.me/{usuario_url}"
}
    
    print(f"{Fore.GREEN}Buscando usuario:{Style.RESET_ALL} {Fore.GREEN}{usuario}{Style.RESET_ALL}\n")
    
    for nombre, url in sitios.items():
        try:
            rps = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
            if rps.status_code == 200:
                print(f"{Fore.GREEN}[✓] Usuario encontrado en {nombre}: {Style.RESET_ALL} {Fore.CYAN}{url}{Style.RESET_ALL} ")
            else:
             print(f"{Fore.RED}[!] usuario no encontrado: {nombre}{Style.RESET_ALL}")
        except:
               print(f"[!]no encontrado{nombre}")
               
               
def salir():
               exit()
               time.sleep(1.5)
               
while True:
    print(banner)
    print(f"{Fore.MAGENTA}[1]{Style.RESET_ALL} {Fore.GREEN}Buscar usuario{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}[2]{Style.RESET_ALL} {Fore.GREEN}Salir{Style.RESET_ALL}\n")
    pregunta = int(input(f"{Fore.MAGENTA}[+]{Style.RESET_ALL} {Fore.YELLOW}Ingrese una opcion: {Style.RESET_ALL}"))
    
    if pregunta == 1:
       usuario =  input(f"\n{Fore.MAGENTA}[+]{Style.RESET_ALL} {Fore.YELLOW}Ingrese el nombre: {Style.RESET_ALL}")
       usuario_url = usuario.replace(" ", "")
       usuario_guion = usuario.replace(" ", "_")
     
       buscar_usuario(usuario, usuario_url, usuario_guion)
       
    if pregunta == 2:
         salir()