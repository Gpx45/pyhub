
class ConnectionError(Exception):
    pass
# We inherited the Exception class, in this case, everything Exception is broughtself.
# ConnectionError behaves, and has the same methods as Exception.
#--------------------------------------------------------------------------


# raise ConnectionError('Cannot connect... is it time to panic?')

try:
    raise ConnectionError('Whoops!')
except ConnectionError as err:
    print('Got: ',str(err))
