biblioteca = {
    'Victor Hugo': ['Les Miserables, Les Orientales'] ,
    'Guy de Maupassant': ['Bel-Ami'],
    'Albert Camus': ['L Étranger']

}
key = input('Introdiceti autorul: ')
if key in biblioteca:
    print('Cartea cu autorul ales este:', biblioteca[key])
else:
    print('Author not found')
