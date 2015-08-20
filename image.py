import self#create normal .py file and call it and use it with dom model
T = int(raw_input())
for x in range(T):
	Px,Py,Qx,Qy = map(int, raw_input().split())
	self.image(Px,Py,Qx,Qy)
