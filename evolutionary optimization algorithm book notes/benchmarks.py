import numpy as np

def sphere_function(x):
   return np.sum(np.power(x, 2), axis=0)

def ackley_function(x):
   sum_1 = np.sqrt(np.sum(np.power(x, 2) /x.shape[0], axis=0))
   term_1 = -20*np.power(np.e, (-0.2*sum_1))
   
   sum_2 = np.sum(np.cos(2*np.pi*x) /x.shape[0], axis=0)
   term_2 = -np.power(np.e, sum_2)
   
   return 20 + np.e + term_1 + term_2   

def auckley_test_function(x):
   result = 0
   for i in range(0, x.shape[0]-1):
      term_1 = 3*(np.cos(2*x[i]) + np.sin(2*x[i+1]))
      term_2 = np.power(np.e, -0.2*np.sqrt(np.power(x[i], 2), np.power(x[i+1], 2)))
      result = result + term_1 + term_2
   
   return result

def rosenbrock_function(x):
   result = 0
   for i in range(x.shape[0]-1):
      term_1 = 100*np.power(x[i+1]-np.power(x[i], 2), 2)
      term_2 = np.power(x[i]-1, 2)
      result = result + term_1 + term_2
      
   return result

def fletcher_powell_function(x):
   a = np.random.uniform(-100, 100, (x.shape[0], x.shape[0]))
   b = np.random.uniform(-100, 100, (x.shape[0], x.shape[0]))
   alpha = np.linspace(-np.pi, np.pi, x.shape[0])
   
   result = 0
   for i in range(x.shape[0]):
      A = 0
      B = 0
      for j in range(x.shape[0]):
         A += a[i][j]*np.sin(alpha[j]) + b[i][j]*np.cos(alpha[j])
         B += a[i][j]*np.sin(x[j]) + b[i][j]*np.cos(x[j])
      result += np.power(A-B, 2)

   return result

def grienwank_function(x):
   term_1 = np.sum(np.power(x, 2)*(1/4000))
   term_2 = 1
   for i in range(x.shape[0]):
      term_2 *= np.cos(x[i]*(1/np.sqrt(i+1)))
      
   return 1 + term_1 - term_2

def penalty_1_function(x, k=100, a=10, m=4):
   n = x.shape[0]
   y = 1 + 0.25*(x + 1)
   
   term_1 = 0
   for i in range(n-1):
      term_1 += np.power((y[i]-1), 2) * (1 + 10*np.power(np.sin(np.pi*y[i+1]), 2)) + np.power((y[n-1]-1), 2)
   term_1 = 10*np.power(np.sin(np.pi*y[0]), 2) + term_1
   
   u = x.copy()
   u[u>a] = k*np.power((u[u>a]-a), m)
   u[(u>=-a) & (u<=a)] = 0
   u[u<-a] = k*np.power((-u[u<-a]-a), m)
         
   return (np.pi/n) * term_1 + np.sum(u)

def penalty_2_function(x, k=100, a=5, m=4):
   n = x.shape[0]
   
   term_1 = 0
   for i in range(n-1):
      part_1 = np.power((x[i]-1), 2) * (1+np.power(np.sin(3*np.pi*x[i+1]), 2))
      part_2 = np.power((x[n-1]-1), 2) * (1+np.power(np.sin(2*np.pi*x[n-1]), 2))
      term_1 += part_1 + part_2 
   term_1 = np.power(np.sin(3*np.pi*x[0]), 2) + term_1
      
   u = x.copy()
   u[u>a] = k*np.power((u[u>a]-a), m)
   u[(u>=-a) & (u<=a)] = 0
   u[u<-a] = k*np.power((-u[u<-a]-a), m)
   
   return 0.1*term_1 + np.sum(u)

def quartic_function(x, power=4):
   result = 0
   for i in range(x.shape[0]):
      result += (i+1)*np.power(x[i], power)
      
   return result

def tenth_power_function(x):
   return np.sum(np.power(x, 10), axis=0)

def rastrigin_function(x):
   return 10*x.shape[0] + np.sum(np.power(x, 2) - 10*np.cos(2*np.pi*x), axis=0)

def schwefel_double_function(x):
   result = 0
   for i in range(x.shape[0]):
      sum_2 = 0
      for j in range(i+1):
         sum_2 += x[j]
      result += np.power(sum_2, 2)
   return result

def schwefel_max_function(x):
   return (np.maximum.reduce(abs(x)))

def schwefel_absolute_function(x):        
   term_1 = 0
   term_2 = 1
   for i in range(x.shape[0]):
      term_1 += abs(x[i])
      term_2 *= abs(x[i])
   return term_1 + term_2

def schwefel_sine_function(x):
   result = 0
   for i in range(x.shape[0]):
      result += x[i]*np.sin(np.sqrt(abs(x[i])))
      
   return -result

def step_function(x):
   result = 0
   for i in range(x.shape[0]):
      result += np.power(np.floor(x[i] + 0.5), 2)
      
   return result

def absolute_function(x):
   result = 0
   for i in range(x.shape[0]):
      result += abs(x[i])
      
   return result

def shekel_foxhole_function(x, num_holes=5):
   a = np.tile(np.array([-32, -16, 0, 16, 32]), num_holes)
   b = np.array([])
   for i in range(num_holes):
      b = np.hstack((b, np.repeat((16 * i - 32), num_holes)))
   a = np.vstack((a, b))
      
   result = 0
   for j in range(num_holes*num_holes):
      term_1 = 0
      for i in range(x.shape[0]):
         term_1 += np.power((x[i]-a[i][j]), 6)
      result += 1/(j+term_1)
      
   return np.power((0.002+result), -1)

def michalewicz_function(x, m=2):
   result = 0
   for i in range(x.shape[0]):
      result += np.sin(x[i]) * np.power(np.sin( ((i+1)*np.power(x[i], 2)) / np.pi ), 2*m)
      
   return -result

def sine_envolope(x):
   result = 0
   for i in range(x.shape[0]-1):
      term_1 = np.sin(np.sqrt(x[i]**2 + x[i+1]**2))-0.5 
      term_2 = np.power(1 + 0.001*(x[i]**2 + x[i+1]**2), 2)
      result += (term_1 / term_2)
      
   return 0.5 + result

def eggholder_function(x):
   result = 0
   for i in range(x.shape[0]-1):
      term_1 = (x[i+1]+47) * np.sin( np.sqrt(abs(x[i+1] + x[i]/2 + 47)) )
      term_2 = x[i] * np.sin(np.sqrt(abs(x[i] - x[i+1] - 47)))
      result += term_1 + term_2
      
   return result