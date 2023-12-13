# RETO 28

mad_vlc = str(input('Introduce una frase que contenga las palabras "Madrid" y "Valencia" '))
while (mad_vlc.find('Madrid') == -1) or (mad_vlc.find('Valencia') == -1):
   mad_vlc = str(input('Esa frase no contenía las dos palabras, introduce una frase que contenga las palabras "Madrid" y "Valencia"'))
vlc_mad = mad_vlc.replace('Madrid', 'X').replace('Valencia', 'Madrid').replace('X', 'Valencia')
print(f'La frase en un principio era: {mad_vlc} y se ha transformado en {vlc_mad}')