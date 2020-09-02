Limitations
===========

Software Testing is very popular both in industry and academia, but it
does have limitations. You should know that:

* Software Testing cannot prove programs correct.

  No matter how much testing you do, it is possible that you missed one that would reveal a bug. 

> "Program testing can be used to show the presence of bugs, but never to show their absence!" -E. Dijkstra

* Software Testing is expensive.

  Writing and maitaining code does not come for free. Several factors need to be taken into account to decide if Software Testing (or any other Verification and Validation technique) is a good choice for the software you are developing. The complexity of the code to be tested is one factor. In one limit, the complexity could be extremely low. In that case, maintainers assume that bugs are very unlikely and, if they happen, they can be solved quickly at a low cost. In another limit, complexity is extremely high. In that case, the cost of bugs is so high that maintainers prefer to use techniques that ascertain that the code is correct (see Dijkstra quotation above). Having said that, many software projects lie in between these two extreme cases. Software Testing is very popular for that reason.








