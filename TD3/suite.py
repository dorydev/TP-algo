#Exo 1:

#Avec liste

def suite(terme, raison, iteration):
    liste_terme = [terme]

    for i in range(iteration):
        terme = terme * raison
        liste_terme.append(terme)

        #généralisation 
        #terme = terme * raison ^ iteration
    return liste_terme


res = suite(1, 0.987, 10)
#print(res)

#exo 2
#Directe

n = 0
u = 1
r = 5.0
#print(f'u({n}) = {u}')
for n in range(10):
    u = u + r
    #print(f'u({n+1}) = {u}')

#Exo 3:

def collatz(n):

    for i in range(1, n + 1):
        if n % 2 == 0:
            n  = n / 2

        else:
            n = 3 * n + 1

    return n
res = collatz(7)
#print(res)


#exo 4:

def fibonacci(n):
    f_0 = 0
    f_1 = 1

    for i in range(2, n):
        suite = f_0 + f_1

        f_0 = f_1
        f_1 = suite

        return suite
    
res = fibonacci(10)
#print(res)

#exo 5

def logistique(mu, u0, n):

    for i in range(u0, n):
        u = mu * u0 ( 1 - u0)
        return u

res = logistique(4, 0.75, 10)
#print(res)

#exo 6:



#exo 7:

def heron(n):

    u_0 = 3/2

    for i in range(n):

        termes = 1/2 * (u_0 + 2 / u_0)
    return termes
    
#exo 8:
    
def recursive(n):
    u = 2
    for i in range(n):
        u = (2 * (u ** 2)) / ((u ** 2) + 2)
    return u
    
if __name__=="__main__":
    n = 10
    for i in range(n+1):
        print(u(i))


#exo 9:
        
def suite_rec(n):

    for i in range(n):
        pass