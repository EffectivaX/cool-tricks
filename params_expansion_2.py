'''
@author: Google Jr
@program: parameter expansion
'''

class ParameterExpansion:
    # old way
    def process_student_info(self, name, last_name, subject, score):
        print(f"{name} {last_name} scored {score} in {subject}")
    
    # new way
    def process_student_info_using_args(self, *args, **kwargs):
        if len(args) == 4:
            name, last_name, subject, score = args
            print(f"{name} {last_name} scored {score} in {subject}")
        elif len(args) == 3 and 'details' in kwargs:
            name, last_name, details = args[0], args[1], kwargs['details']
            print(f"{name} {last_name} scored {details['score']} in {details['subject']}")



if __name__ == "__main__":
    pe = ParameterExpansion()
    
    # Example 1: Using individual arguments
    print("Example 1:")
    pe.process_student_info("Andile", "Mbele", "Computational Thinking", 100)

    # Example 2: Using a dictionary
    print("Example 2:")
    student_details = {"name": "Andile", "last_name": "Mbele", "subject": "Computational Thinking", "score": 100}
    pe.process_student_info_using_args(**student_details)