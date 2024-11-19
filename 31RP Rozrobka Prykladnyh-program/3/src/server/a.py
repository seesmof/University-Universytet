class Employee:
    mode='default'
    can_delete=False
    varbose_name='employees'

def get_class_fields(class_name):
    return [v for v in dir(class_name) if not v.startswith('__')]

print(get_class_fields(Employee))