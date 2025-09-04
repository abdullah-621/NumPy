"""
| ফাংশন                     | কাজের ধরন           | শর্ত                                     |
| ------------------------- | ------------------- | ---------------------------------------- |
| `array_split(a,n,axis=1)` | কলাম ভাগ (flexible) | অসমান ভাগ হলে কিছু অংশ ছোট/খালি হতে পারে |
| `hsplit(a,n)`             | কলাম ভাগ (strict)   | অবশ্যই সমান ভাগ হতে হবে                  |
| `array_split(a,n,axis=0)` | row ভাগ (flexible)  | অসমান ভাগ হলে চলবে                       |
| `vsplit(a,n)`             | row ভাগ (strict)    | অবশ্যই সমান ভাগ হতে হবে                  |

"""



import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr = np.array_split(a,3,axis=1)
new_arr2 = np.hsplit(a,3)
new_arr3 = np.array_split(a,3,axis=0)
new_arr4 = np.vsplit(a,3)
print(new_arr)
print(new_arr2)
print(new_arr3)
print(new_arr4)