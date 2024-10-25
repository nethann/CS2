class EmailFormatError(Exception):
    def __init__(self, error_message="Please enter a valid email address."):
        self.error_message = error_message
        super().__init__(self.error_message)

def is_valid_email(str):
    if '@' not in str:
        raise EmailFormatError()

    username, domain = str.split('@')

    if not username[0].isalpha():
        raise EmailFormatError()

    if not domain.endswith('student.gsu.edu'):
        raise EmailFormatError()

    return True


#my testing cases
try:
    print(is_valid_email("tnagendran1@student.gsu.edu"))  
except EmailFormatError as error:
    print(error)

#with integer in front 
try:
    print(is_valid_email("1tnagendran2@student.gsu.edu"))  
except EmailFormatError as error:
    print(error)

#without @ sign
try:
    print(is_valid_email("tnagendran2student.gsu.edu"))  
except EmailFormatError as error:
    print(error)

#without @student.gsu.edu
try:
    print(is_valid_email("nethan.nagendran@gmail.com"))  
except EmailFormatError as error:
    print(error)