!# 
def iterative_factoria(n):
    fact = 1
    for i in range (2, n + 1):
        fact *= i
    return fact
    
print(iterative_factoria(5))

def recur_factoria(n):
    if n == 1:
        return n
    else:
        temp = recur_factoria(n - 1)
        temp = temp * n
    return temp
    
print(recur_factoria(5))

# permutations

def permute(string, pocket = "")

def iterative_factoria(n):
    fact = 1
    for i in range (2, n + 1):
        fact *= i
    return fact

print(iterative_factoria(5))

def recur_factoria(n):
    if n == 1:
        return n
    else:
        temp = recur_factoria(n - 1)
        temp = temp * n
    return temp

print(recur_factoria(5))

# permutations

def permute(string, pocket = ""):
    if len(string) ==0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string [i]
            front = string[0:i]
print(permute("ABCD", ""))

