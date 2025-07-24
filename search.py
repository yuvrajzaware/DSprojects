l=[]
for i in range(1,51):
    l.append(i)
print(l)
def linear(l,idl):
  if idl in l:
     print("found")
  else:
     print("not found")
idl=int(input("Enter ID1: "))
linear(l,idl)

def binary(arr,idb):
   low=0
   high=len(l)
   while(low<=high):
      mid=(low+high)//2
      if(l[mid]==idb):
         return True
      elif(l[mid]>idb):
         high=mid-1
      else:
         low=mid+1
   return False
idb=int(input("Enter ID2: "))
r=binary(l,idb)
if(r==True):
   print("Found")
else:
   print("not found")