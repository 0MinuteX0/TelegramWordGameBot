from time import time
start_time = time()

f = open("ListЯ.txt").read().split("\n")
list1 = "\", \"".join(f)
open("ListЯ.txt", "w").write(f"[\"{list1}\"]")

end_time = time() - start_time
print(end_time)