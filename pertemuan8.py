'''for i in range(1,5):   #bais
    for j in range(1,1):  #kolom
        print(f'Pulangan i ke-{i}, perulangan j ke-{j}')
    print()'''


a = int(input('banyak bintang ='))
for i in range(1,a+1):   
    for j in range(1,a+1):
        if i<=j:
            print ('*', end='\t')
    print()
