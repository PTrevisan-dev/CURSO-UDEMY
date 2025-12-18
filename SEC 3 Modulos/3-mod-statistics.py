import statistics as st

# 1 - media 
print(st.mean([3, 4, 5, 6, 7, 9]))

# 2 - aplicando mediana
print(st.median([1, 2, 3, 4, 5]))
print(st.median([1, 2, 13, 1, 4, 5]))

# 3 - aplicando moda 
print(st.mode([1, 2, 13, 1, 4, 5, 7, 10, 7, 3, 5, 7, 9, 8, 2, 7, 9]))

# 4 - desvio padrao 
'''
- quanto mais proximo de 0 for o desvio padrao, siginifica que os 
dados do conjunto estao menos dispersos
'''

print(st.stdev([1, 2, 13.5, 1, 4.6, 5, 7.4, 10.5, 7, 3, 5, 7, 9.7, 8.7, 2, 7.5, 9]))

'''git de merda n esta funcionando linha so pra ver se consigo dar commit '''

print('eu amo o git mas odeio quem usa cmg ')
