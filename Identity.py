
class Identity:
    
    def __init__(self) -> None:
        self.ALLOWED_SCHEME = 'visma-identity'
        self.ALLOWED_PATHS = ['login', 'confirm', 'sign']
    
    def parse_uri(self, uri: str):
        '''Parses a given uri and returns it's scheme, path and parameters'''
        scheme = uri.split(':')[0]
        
        path = uri.split('/')[2]  
        path = path.split('?')[0]\
        
        parameters = uri.split('?')[1]
        parameters = parameters.split('&')
        
        parameters_dict = {}
        
        # Put parameters in a dictionary
        for param in parameters:
            parameters_dict[param.split('=')[0]] = param.split('=')[1]
            
        return scheme, path, parameters_dict
    
    def validate(self, uri: str):
        '''Validates scheme, path and parameters of a uri and returns path and parameters as a dictionary if uri is valid'''
        
        scheme, path, parameters = self.parse_uri(uri)
        
        # Check if scheme is allowed
        if not scheme == self.ALLOWED_SCHEME:
            raise ValueError('Scheme is invalid')
        
        # Check if path is allowed
        if not path in self.ALLOWED_PATHS:
            raise ValueError('Path is not allowed')
        
        
        if path == 'login': #Validate login
            if not 'source' in parameters:
                raise Exception(f'Path {path} missing required parameter source')
            
            if parameters['source'].isdigit():
                raise ValueError(f'Required parameter source is not string')
            
            if not len(parameters) == 1:
                raise Exception(f"Expected one parameter for path {path}, received {len(parameters)}")
        
        elif path == 'confirm': #Validate confirm
            if not 'source' in parameters:
                raise Exception(f'Path {path} missing required parameter source')
            
            if not 'paymentnumber' in parameters:
                raise Exception(f'Path {path} missing required parameter payment number')
            
            if parameters['source'].isdigit():
                raise ValueError(f'Required parameter source is not string')
            
            if not parameters['paymentnumber'].isdigit():
                raise ValueError(f'Required parameter paymentnumber is not int')
            
            if not len(parameters) == 2:
                raise Exception(f"Expected two parameters for path {path}, received {len(parameters)}")
        
        elif path == 'sign': #Validate sign
            if not 'source' in parameters:
                raise Exception(f'Path {path} missing required parameter source')
            
            if not 'documentid' in parameters:
                raise Exception(f'Path {path} missing required parameter documentid')
            
            if parameters['source'].isdigit():
                raise ValueError(f'Required parameter source is not string')
            
            if parameters['documentid'].isdigit():
                raise ValueError(f'Required parameter documentid is not string')
            
            if not len(parameters) == 2:
                raise Exception(f"Expected two parameters for path {path}, received {len(parameters)}")
            
        return path, parameters
    


class Client(Identity):
    
    def __init__(self) -> None:
        pass
    
    def login(self):
        self.validate() # Add uri
        # Complete the action if no error was raised
    
    def confirm(self):
        self.validate() # Add uri
        # Complete the action if no error was raised
    
    def sign(self):
        self.validate() # Add uri
        # Complete the action if no error was raised
    