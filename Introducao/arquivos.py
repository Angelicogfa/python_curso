#%%
file = open('teste.txt', 'w')
file.writelines('\nTeste1')
file.writelines('\nTeste 2')
file.writelines('\nTeste 3')
file.flush()
file.close()

arquivo = open('teste.txt')
arquivo
arquivo.readlines()
arquivo.seek(0)

for line in arquivo:
    print(line)
