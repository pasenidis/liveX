import os

print(
"""
oooo   o8o                        ooooooo  ooooo 
`888   `"'                         `8888    d8'  
 888  oooo  oooo    ooo  .ooooo.     Y888..8P    
 888  `888   `88.  .8'  d88' `88b     `8888'     
 888   888    `88..8'   888ooo888    .8PY888.    
 888   888     `888'    888    .o   d8'  `888b   
o888o o888o     `8'     `Y8bod8P' o888o  o88888o by Edward Pasenidis
""")
wID = int(os.popen('wp id').read())
print('Window ID:', wID)
srcFile = str(input('Source file: '))
choice = str(input('Do you want sound enabled [yes/no]: '))

if (choice == "yes"):
    command = f"wp run mpv --wid={wID} {srcFile} --loop=inf --player-operation-mode=pseudo-gui --force-window=yes"
    os.popen(command)
elif (choice == "no"):
    command = f"wp run mpv --wid={wID} {srcFile} --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio"
    os.popen(command)
else:
    print("Wrong answer format.")
