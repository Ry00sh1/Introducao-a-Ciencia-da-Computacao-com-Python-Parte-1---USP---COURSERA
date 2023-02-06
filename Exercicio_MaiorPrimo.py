def maior_primo(n):
    def é_primo(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    
    for i in range(n, 1, -1):
        if é_primo(i):
            return i
