# Bienvenida al sistema.
print('Bienvenido al sistema de cálculo de inversiones.')

# Un input para establecer cantidad a invertir.
initial_capital = float(input('¿Cuánto desea invertir? '))

# Otro input para el interés anual y periodo.
interest_rate = float(input('¿A qué interés anual (%) está invirtiendo? '))
period = float(input('¿Y por cuántos años va a mantener esta inversión? '))

# Hacer el cálculo con interés compuesto:
final_capital = initial_capital * (1 + interest_rate/100) ** period
net_return = round(final_capital - initial_capital,2)
# Devolver resultado por terminal:
print(f'En {period} años habrás recibido {net_return}€ de interés.')