
# Python 2.x has an ambiguous except syntax, Python 3.x is stricter so the
# following examples help to identify the right way to handle Py2/3 compatible
# exceptions
# Background: http://www.python.org/dev/peps/pep-3110/

# Note that 'as' and ',' are both accepted in Python 2.x but only 'as' in Python 3.x:
# http://docs.python.org/reference/compound_stmts.html#try

# Works in both Python 2.7 and 3.2
try:
    1/0
    print("Will never get here")
except:
    print("Catches all exceptions, this is bad form")

# Works on Python 2.7, Fails on Python 3.2
#try:
#    1/0
#    print("Will never get here")
#except ZeroDivisionError, err: # this form fails in Python 3.2
#    print("Got divide by zero: " + str(err))

# Works in both Python 2.7 and 3.2
try:
    1/0
    print("Will never get here")
except ZeroDivisionError as err:
    print("Got divide by zero: " + str(err))

# Works in both Python 2.7 and 3.2
try:
    1/0
    print("Will never get here")
except (ZeroDivisionError, KeyError) as err:
    print("Got divide by zero: " + str(err))

