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
import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수가 실행된 시간은: %.6f 초" %(end - start))

myfunc()

#%%
import time

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print("함수가 실행된 시간은: %.6f 초" %(end - start))
        return result
    return wrapper

@elapsed
def myfunc(msg):
    print("%s를 출력합니다." %msg)

myfunc("you need a python")

