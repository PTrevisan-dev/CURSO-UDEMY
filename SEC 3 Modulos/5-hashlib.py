import hashlib as hs

# 1 verificar os algoritimos disponiveis 
print(hs.algorithms_available)

# 2 verfificar algoritimos de acordo com o SO

print(hs.algorithms_guaranteed)

# 3 usando o SHA256 pra criptografar mas n sao os melhores isso aqui e so um modulo nativo existem coisas mais robustas isso tem no hashlib-comp.txt

algorithm = hs.sha256()
print(algorithm.digest())
message = 'Esta tudo bem !! sabe pq ? PQ EU CHEGUEI !!!!!!'.encode()
algorithm.update(message)
print(algorithm)

# 4 utilizando o MD5 utilizado para compaovar a integridade de dados comparando o HASH 
MD5 = hs.md5()
MD5.update(message)
print(MD5.hexdigest())