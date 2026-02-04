## Entity Relationship Diagram (ERD)

An Entity Relationship Diagram (ERD) was created during the planning phase to define the core data structure of the application before implementing any database models.

The ERD focuses on the MVP feature of food logging and includes two main entities: **User** (provided by Django’s built-in authentication system) and **FoodEntry**, which represents a single food log entry created by a user.

A one-to-many relationship is defined between **User** and **FoodEntry**, where one user can create multiple food entries, and each food entry belongs to exactly one user. This relationship enforces data ownership and ensures users can only access their own data.

The ERD serves as a reference for the Django model design and provides a clear, scalable foundation for future feature expansion.

![ERD diagram](images/erd.png)