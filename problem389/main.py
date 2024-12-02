# This problem was asked by Google.

# Explain the difference between composition and inheritance. 
# In which cases would you use each?

## Solution ##

# Composition and inheritance are general strategies used to model software.

# In inheritance, the core building block is the class, and works well for software that is used to model other business domains that have a well mapped-out, hierarchical structure. 
# For example, in an HR system, you might have different types of employees and represent them each with a different subclass, under the parent class Employee.

# Composable systems tend to rely on interfaces which any object or class can individually implement. 
# For example, a video game might contain objects which can individually cast spells, have hitpoints, have a hitbox, be collidable, or otherwise interact with the game world. 
# In this case, a composable system works well, as we can have a physics system, a rendering system, a hitpoints system, a spell system, etc. 
# Each system can be designed, tested, and used in isolation.

# In general, we should prefer composition over inheritance. 
# The reason being that composable systems are more flexible and powerful than inheritance-based ones, especially when each system is independent. 
# When each system is independent, a new object or class can pull in functionality from each system, which makes each the whole system multiplicatively more powerful. 
# It also avoids the infamous diamond problem in inheritance-based systems, where a class inherits from 2 parent classes with the same method. 
# In this case, it is hard for a programmer to know on which class the method would be called.
