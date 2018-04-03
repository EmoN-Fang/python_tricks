import numpy as np

x = np.array([[[0], [1], [2]]])
print("x=",x)
"""
x=

[[[0]
  [1]
  [2]]]
"""
print(x.shape)  # (1, 3, 1)  from outside to inside, 
                            #delete the first[], theres only 1 line, 
                            #delete the second [], theres 3 line,
                            # delete the third [], one object in each.


x1 = np.squeeze(x)  

print("x1=",x1)  # [0 1 2]
print(x1.shape)  # (3,)


x2 = np.squeeze(x, axis=(0))

print("x2=",x2)
'''
x=

[[0]
  [1]
  [2]]
  '''
print(x2.shape) #(3,1)



x3 = np.squeeze(x, axis=2)
print(x3) 
'''
x3 = [[0 1 2]]
'''
print(x3.shape) #(1,3)

y = np.array([[0],[2],[3]])
print("y=",y)
'''
('y=',
      [[0],
       [2],
       [3]])
'''

print(y.shape) #(3,1)


z = np.array([0,1,2])
print("z=",z)
print(z.shape) #(3,)

z1 = z.reshape((1,3))
print(z1)  # [[0,1,2]]
print(z1.shape)

z2 = z.reshape(3,1)
print("z2=",z2)  
'''
[[0]
  [1]
  [2]]
  '''
print(z2.shape) #(3,)



print (x[:,1,:])   # [[1]]   delete only the second[]
print (x[:,1])     # [[1]]  delete only the second []
print(x[0,1])      #[1]   delete the first and the second []
print(x[0,1,0])    #1   delete all the []


k = np.squeeze(x[:,1])
print(k) # 1

print(z1[:,1])  #[1]