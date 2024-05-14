d_test = {'id1':'10', 'digit':'15'}
choise = d_test.get('id') or d_test.get('digit') or 0
print(choise)