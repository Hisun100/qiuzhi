"""
对于第n个台阶来说，只能从n-1或者n-2的台阶跳上来，所以
F(n) = F(n-1) + F(n-2)
斐波拉契数序列，初始条件
n=1:只能一种方法
n=2:两种
递归一下就好了
"""

def jumpFloor(number):
	# write code here
	if number <=0:
		return -1
	if number == 1:
    	return 1
	if number == 2:
    	return 2
	return jumpFloor(number-1) + jumpFloor(number-2)
if __name__ == '__main__':
	print(jumpFloor(4))

