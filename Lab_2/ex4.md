Q1:Describe the algorithm you will use to find the room. Assume all the
information you have is the one given by the sign; you have no
knowledge of the floor plan

Ans: I would use a linear search algorithm. Starting from the first room indicated by the sign, I would check each room number in order and compare it with the target room (EY128). If the current room is not EY128, I move to the next room and repeat the process until the correct room is found.

Q2:How many ”steps” it will take to find room EY128? And what is a “step” in this
case?

Ans: It will take 15 steps to find the room EY128. Here, a step refers to checking one room number and comparing it with EY128 before moving to the next room.

Q3:Is this a best-case scenario, worst-case scenario, or neither?

Ans: It is the worst-case scenario.

Q4: With this particular sign and floor layout, explain what a worst-case or best-
case scenario would look like

Ans: Worst case is searching from EY100 to EY128. And bestcase would starting from EY138 from other     side to EY128.

Q5:Suppose after a few weeks in the term you memorize the layout of the floor.
How would you improve the algorithm to make it more efficient?

Ans: After memorizing the layout, I would use a directed search instead of linear search. Instead of checking every room, I would go directly in the direction where EY128 is located. This reduces unnecessary comparisons and makes the search closer to constant time, since I no longer need to examine every room.