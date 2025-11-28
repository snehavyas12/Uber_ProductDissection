# PRODUCT DISSECTION FOR UBER (RIDE HAILING PLATFORM)

This  project  dissects  Uber’s  approach to redefining urban mobility by addressing long-standing 
gaps in reliability, transparency, safety, and efficiency through technology-driven innovation.

OBJECTIVES: 
1.  Dissect Uber’s product features and their role in problem-solving. 
2.  Present a real-world case study of an operational challenge. 
3.  Design a database schema to support Uber’s main flows. 
4.  Justify schema design decisions with a clear rationale. 
5.  Visualize with an ER Diagram. 
6.  Summarize findings for presenting to stakeholders.
   
The real world problems solved by Uber with their unique strategy and coming of age technology is studied next. The top features of the organization are mentioned which will provide the base of the schema design.

A conceptual model is the raw core model of the business. Only the entities and the flow of the data is studied here. Conceptual model is crucial in designing the database and schema as it is the first  step towards all the follwoing analysis. We include 7 main entities and the cardinality between them. 

Further we do schema description of Uber. Each entity from conceptual model gets turned into logical model. In logical model we get the attributes of the entities. This model in my projects strictly follows 3F of normalization. The entities are: User, Driver, Ride, Payments, Fair & Pricing, Taing & Review ans Support tickets. The primary key(s) and foreign keys are designed in the logical model.

The pyhsical model has the Entity-Relationship (ER) Diagram which is the lowest level of detail. The diagram has entities, their attributes, the flow, the cardinality among the schema. Overall,  this  design  balances  efficiency,  integrity,  and  scalability, aligning with Uber’s strategy to deliver a smooth and trustworthy ride-sharing experience. 