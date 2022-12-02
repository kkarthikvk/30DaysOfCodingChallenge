Day 1 of #30Days of coding Challenge

programming Language: Python

Problem statement: Product of Array Except for self

Problem Description:

Find the product of other elements in the array except the ith element. Meaning multiply the rest of the elements in the array without including the current position.

Example: 

[1,2,3,4] -> [24,12,8,6]

1st index : 2X3X4

2nd index : 1X3X4

3rd index : 1X2X4

4th index : 1X2X3

Given condition all are positive Intergers.

Approach 1:
The straight forward approach. See the optimizing the approach later.

psudo code:

	a = given_list
	b = []
	loop i,v1  through a:
		prd = 1
		loop j,v2 through a:
			if i== j:
				continue
			else:
				prd *= v2
		b.append(prd)

Approach 2:
Need to optimize the code. So instead looping twice will loop once.

psudo code:

	import math
	a = given_list[]
	b = []
	loop i,v1 through a:
		c = a[:i] + a[i+1]
		prd = math.prod(c)
		b.append(c)

