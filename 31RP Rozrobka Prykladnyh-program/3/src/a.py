class Employee:
    mode='default'
    can_delete=False
    varbose_name='employees'

print([v for v in dir(Employee) if not v.startswith('__')])