# Visma-Solutions-programming-task

I created a class called Identity which identifies the type of request and validates it by the criteria included in the assignment. First I created a method to parse all of the necessary info from a uri. Then I created another method to validate the request using the parsed data from parse_uri method. If the requirements are not met the method raises an error with a brief description of the problem that has occurred. If no error is raised the method returns a tuple containing path and parameters. I would improve the validate method by improving the checks of if the parameter is an integer or a string as the method isdigit only distinguishes integers from other datatypes. So for example “1.0”.isdigit() would return False as 1.0 is a float instead of int.

I’m not completely sure if I understood the last part about the client correctly. I created a class called Client which has three methods that represent different functions of an app. First the request is validated using the validate method from Identity class and if all checks pass the request will be completed.

The project was written in python.
