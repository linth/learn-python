'''
user case: generate python code from class diagram (UML).

'''


class UMLClass:
  
    def __init__(self, name) -> None:
        self.name = name
        self.attributes = []
        self.methods = []
        
    def add_attribute(self, attribute_name, attribute_type) -> None:
        self.attributes.append((attribute_name, attribute_type))
        
    def add_method(self, method_name, return_type, parameters):
        self.methods.append((method_name, return_type, parameters))
        
        
def generate_python_class(uml_class):
    python_code = f'class ${uml_class.name}:\n'
    
    for attribute_name, attribute_type in uml_class.attributes:
        python_code += f'    {attribute_name}: {attribute_type}\n'

    for method_name, return_type, parameters in uml_class.methods:
        param_list = ', '.join(parameters)
        python_code += f'    def {method_name}({param_list}) -> {return_type}:\n'
        python_code += f'        pass\n'

    return python_code
  
  
uml_class_data = {
    'name': 'Book',
    'attributes': [('title', 'str'), ('author', 'str'), ('ISBN', 'str'), ('copies', 'int')],
    'methods': [('check_out', 'bool', []), ('return_book', 'None', [])]
}

uml_class = UMLClass(uml_class_data['name'])
for attribute_data in uml_class_data['attributes']:
    uml_class.add_attribute(*attribute_data)

for method_data in uml_class_data['methods']:
    uml_class.add_method(*method_data)

python_code = generate_python_class(uml_class)
print(python_code)