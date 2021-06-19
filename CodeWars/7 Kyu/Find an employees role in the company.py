def find_employees_role(name):
  try: (first, last) = name.split(' ')
  except: return 'Does not work here!'
  for e in employees:
    if e['first_name'] == first and e['last_name'] == last: return e['role']
  return 'Does not work here!'