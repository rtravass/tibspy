# numbers = [1, 2, 3, 4, 5]
# print(numbers * 2)

#================================
# import numpy as np

# numbers = np.array([10, 20, 30, 40])
# print(numbers * 2)

# op:
# [20 40 60 80]


#==========one dimensional numpy array====================

# import numpy as np

# sales = np.array([10, 20, 30, 40])

# print(sales)
# print(sales.ndim)
# print(sales.shape)
# print(sales.size)
# print(sales.dtype)

# op: [10 20 30 40]
# 1
# (4,)
# 4
# int64



#==========two dimensional numpy array====================

# import numpy as np

# sales = np.array([
#     [10,20,30],
#     [40, 50, 60]
# ])

# print(sales)
# print(sales.ndim)
# print(sales.shape)
# print(sales.size)
# print(sales.dtype)

# op:
# [[10 20 30]
#  [40 50 60]]
# 2
# (2, 3)
# 6
# int64


#=============Converting list to numpy array======

# import numpy as np

# daily_sales = [10, 20, 30, 40]
# sales_array = np.array(daily_sales)

# print(sales_array)
# print(sales_array.ndim)
# print(sales_array.shape)
# print(sales_array.size)
# print(sales_array.dtype)


# op:
# [10 20 30 40]
# 1
# (4,)
# 4
# int64


#=======================extracting a range with slicing ===========
# import numpy as np

# sales = np.array([10, 20, 30, 40, 50, 60])

# print(sales[1:4])
# print(sales[:4])
# print(sales[1:])

# op:
# [20 30 40]
# [10 20 30 40] 
# [20 30 40 50 60]


#=======================extracting a range with slicing in 2d array ===========

# import numpy as np

# sales = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(sales[0])
# print(sales[:, 1])
# print(sales[1,2])


# op:
# [10 20 30]
# [20 50]
# 60


#======================filtering data with boolean conditions ==========

# import numpy as np

# sales = np.array([10, 20, 70, 90, 50, 30]) 
# mask = sales > 30
# print(mask)
# print(sales[mask])

# op:
# [False False  True  True  True False]
# [70 90 50]