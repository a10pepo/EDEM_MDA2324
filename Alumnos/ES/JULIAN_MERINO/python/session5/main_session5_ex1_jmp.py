import pandas as pd

pokemon = pd.read_csv('Alumnos/ES/JULIAN_MERINO/python/session5/pokemon_data.csv', dtype = {
    'Name': str,
    'Type 1': str,
    'Type 2': str,
})

#describe = pokemon.describe()
#print(describe)

head = pokemon.head()
tail = pokemon.tail()
columns = pokemon.columns
names = pokemon['Name']

#print(*names)

#Option 1
#names_speeds = pokemon[['Name', 'Speed']]
#print(names_speeds)

#Option 2
#first_5 = pokemon['Name'][0:5]
#print(first_5)

#Option 2.1
#print(pokemon.iloc[0:3])

#Get the name of row n
#print(pokemon.iloc[10,1])

#Iterates through the list all names and appends it to a list called pokemon_list
#for i, pokemon_list in pokemon.iterrows():
#    print(f'{i} - {pokemon_list['Name']}')

#Water-type pokemons now, using LOC:
#Integrated
#water_poke = pokemon.loc[pokemon['Type 1'] == 'Water']
#print(water_poke)
#By variables
#condition = pokemon['Type 1'] == 'Water'
#water_poke = pokemon.loc[condition]
#print(water_poke.to_string(index = False))

#Create a new column calculated from other ones:
pokemon['Total'] = pokemon['HP'] + pokemon['Attack'] + pokemon['Defense'] + pokemon['Speed']
print(pokemon)

#Print the best 5 and show Name and Total
print(pokemon.sort_values('Total', ascending = False).head(5)[['Name', 'Total']])

#And we get rid of Total column
print(pokemon)
pokemon = pokemon.drop(columns = 'Total')
print(pokemon)

#We save the data in a csv file
pokemon.to_csv('pokemon_modified.csv', index = False)
