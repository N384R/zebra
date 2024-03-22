class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n

if __name__ == "__main__":
    mul3 = Mul(3)

#%%

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    
print(mul3(11))

# %%
