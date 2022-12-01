Day 1 of #30Days of coding Challenge

programming Language: Python

Problem statement: Product of Array Except for self

Problem Description:

Find the product of other elements in the array except the ith element. Meaning multiply the rest of the elements in the array without including the current position.

Example: 

[1,2,3,4] -> [24,12,8,6]

1st index : 2*3*4
2nd index : 1*3*4
3rd index : [1*2*4]
4th index : [1*2*3]

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

