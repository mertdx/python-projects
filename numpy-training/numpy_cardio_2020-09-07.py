# %%
# q1: Sadece boolean False degerinden olusan, 5x5 boyutunda bir ndarray oluşturunuz.
import numpy as np
false_array = np.zeros((5, 5)).astype(bool)

# %%
# q2: 1'den 1000'e kadar olan tam sayılardan oluşan bir ndarray oluşturunuz ve bunun içinden 42'ye tam bölunebilen sayıları secip, ayrı bir ndarray'de toplayınız.
numbers = np.arange(1, 1001)
# np.mod() ile yapamadım.
result_list = [x for x in numbers if x % 42 == 0]
result_ndarray = np.array(result_list)

# %%
# q3: bir ndarray içinden, en küçük ve en büyük değerleri secen bir kod yazınız.


def max_and_min(arr):
    result = [arr.min(), arr.max()]
    return result


x = max_and_min(np.arange(20))
# %%
# q4: bir ndarray içinden, en büyük 3 sayıyı secen bir kod yazınız.


def big_three(arr):
    indexes = np.argpartition(arr, -3)[-3:]
    result = arr[indexes]
    return result


x = big_three(np.array([36, 3, 5, 1, 2, 10, 11, 24]))
# %%
# q5: [0, 1, 0, 1...] (toplam uzunluğu 40) olacak şekilde bir ndarray oluşturunuz.
x = np.zeros(40)
x[1::2] = 1
# %%
# q6: bir ndarray'i reverse ediniz.
arr = np.arange(20)
arr = np.flip(arr)
# %%
# q7: 7x7 uzunlugunda bir birim matris oluşturunuz.
arr = np.eye(7)
# %%
# q8: Kenarlarında 1, ortasında 0 olan, 10x10 bir matris oluşturunuz.
arr = np.ones((5, 5))
arr[1:-1, 1:-1] = 0
'''
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]

 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

'''

# %%
# q9: Siyah kareler için 1, beyaz kareler için 0 olacak şekilde, bir satranç tahtasını temsil eden bir matris oluşturunuz.
# yapamadım, olmadı :(
arr = np.zeros((8, 8))
arr[1::2] = 1
# %%
# q10: 10x10 boyutunda, 0 ile 100 (dahil) arasında float sayılardan oluşan bir matris yaratınız.
arr = np.linspace(0, 100, 100)
arr = arr.reshape(10, 10)

# %%
# q11: q10'daki matris'deki her sayıyı, taban değerine yuvarlayınız.
arr = np.linspace(0, 100, 100)
arr = arr.reshape(10, 10)
result = np.floor(arr)

# %%
# q12: 5x5 boyutunda 2 adet ndarray'in, birbirine eşit olup olmadığını bulunuz.
arr1 = np.full((5, 5), 7)
arr2 = np.full((5, 5), 8)
result = np.array_equal(arr1, arr2)

# q13: 5x5 boyutunda bir ndarray olsun. 5x5=25 hücrenin ortalamasını alıp, 5x5 hücrenin en ortasındaki hücreye yazdırınız.

# %%
