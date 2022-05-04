
def printTour(arr,n):
     
    
    start = 0
    c = 0
    d = 0

    for i in range(n):
      c += arr[i][0] - arr[i][1]
      if c < 0:           
        start = i+1       
        d += c         
        c = 0           
     
    return start if (c+d)>=0 else -1
   
arr = [[6,4], [3,6], [7,3]]
start = printTour(arr,3)
if start == -1:
  print("No hay una solucion posible !!!")
else:
  print("start = {}".format(start))
 
