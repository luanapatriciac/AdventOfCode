import hashlib

result = hashlib.md5(b'abcdef609043')
#print(result.hexdigest())

for i in range(1000000000):
	result = hashlib.md5(b'yzbqklnj'+ bytes(str(i),"utf-8"))

	if result.hexdigest().startswith("000000"):
		correct_result = result
		print(i)
		break

print(correct_result)	


#------------
