

(a) What kind of diagram is this and what are such diagrams usually used to
represent?
(b) Does this diagram represent the structure or the behaviour of a system?
(c) What are the elements labelled (i)?
(d) What do the arrows labelled (ii), (iii) and (iv) represent?
(e) Which happens first: (ii), (iii) or (iv)?
(f) Explain the difference between a synchronous and an asynchronous message.
(g) Does this diagram contain synchronous or asynchronous messages?
(h) What does the arrow labelled (vii) represent?
(i) What does the dashed line labelled (viii) represent?
(j) What do the thin vertical rectangles labelled (ix) and (x) represent?
(k) Does the diagram represent a concurrent or a procedural interaction?
(l) If (vi) were replaced with a label, what would that label represent?
(m) What does the arrow labelled (v) represent and what would this correspond to if
A was an object in an object-oriented system?
(n) What does the grey shading represent on the thin vertical rectangle labelled (ix)?
Why is only part of the rectangle shaded?
(o) If A and C represent objects, is there necessarily an association in the class model for this system between the classes to which A and C belong?  Explain your
answer.
Your answer:
a) This is a Sequence Diagram, used to represent temporal interactions between objects
b) It represents system behavior
c) (i) represents the system or subsystem name
d) The arrows represent:
● (ii) is a call message
● (iii) is a message from A to B
● (iv) is a message from B to C
e) The sequence order is: (ii) → (iii) → (iv)
f) Synchronous messages (solid arrows) require waiting for return, asynchronous messages (dashed arrows) don't
g) The diagram contains synchronous messages (solid arrows)
h) (vii) represents a return message
i) (viii) represents a lifeline
j) (ix) and (x) are activation bars, showing when objects are active
k) This is a procedural interaction
l) If (vi) were replaced with a label, it would represent the message name
m) (v) represents a return message, corresponding to a method return in an object-oriented system
n) The grey shading shows when the object is active, partial shading indicates the object is only active during specific periods
o) No, an association is not necessarily required in the class model, as message passing can be implemented through temporary references