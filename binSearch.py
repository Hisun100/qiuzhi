"""
@list :排好序的列表
@a    :待查找的元素
函数作用：
若a在list中则放回True
否则，返回False
"""
def binSearch(list,a):
	left = 0 
	right = len(list)-1
	mid = (left+right)//2
	if a < mid:
		right = mid -1
	elif a> mid:
		left = mid
	else:
		return True
	return False

if __name__ == '__main__':
	print(binSearch([1,2,3,4,7,8,9],5))
