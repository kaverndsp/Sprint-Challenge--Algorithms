#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(1) Assuming that the expression will only be evaluated once.

b) O(n) For loop has to iterate through n'th input size.

c) O(n) I believe this to be true because of the runtime complexity of recursion

## Exercise II

Solving for the most efficient algorithm would look something similar to a binary search.

Begin at the middle floor. If the egg breaks at the middle floor, we can eliminate all the floors above, and move now only towards lower floors. Find the new middle floor between the ground and the new threshold, and do another egg drop comparasion. Keep doing these comparasions until the egg does not break. When the egg does not break, we have found the value of f.

This would be O(log (n))

Solving for the most realistic solution though (since an egg is super fragile and would break from even a ground level) might yield better runtime in my opinion.

A runtime for this would be o(n), with most cases being o(1)
Set a bool for eggnotbroke and set to false. Set a while loop and for each level that an egg breaks, at + 1 to a variable of eggs broken. When egg doesn't break return eggnotbroke to true and break out of loop. The number of eggs broken will give us the number of floors.
