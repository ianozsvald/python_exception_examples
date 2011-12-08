
# Python 2.x has an ambiguous except syntax, Python 3.x is stricter so the
# following examples help to identify the right way to handle Py2/3 compatible
# exceptions
# Background: http://www.python.org/dev/peps/pep-3110/

# Note that 'as' and ',' are both accepted in Python 2.x but only 'as' in Python 3.x:
# http://docs.python.org/reference/compound_stmts.html#try

# Works in both Python 2.7 and 3.2
# Considered bad form - all exceptions are silently swallowed
# This can be useful in an outer loop if you log the exception
try:
    1/0
    print("Will never get here")
except:
    print("Catches all exceptions, this is bad form")

# This variant catches just one type of exception, this is
# the more useful way to handle exceptions
try:
    1/0
    print("Will never get here")
except ZeroDivisionError:
    print("This is a ZeroDivisionError")

# Works in both Python 2.7 and 3.2 - note use of "as"
# This variant catches a known error (e.g. to handle specific situations)
# and it also has a catch-all which could be used for logging
try:
    "a" + 22
    print("Will never get here")
except ZeroDivisionError:
    print("This is a ZeroDivisionError")
except Exception as err:
    print("This catches any other type of error: " + str(err))

# Works on Python 2.7, Fails on Python 3.2
# due to syntax changes - avoid using the ","
#try:
#    1/0
#    print("Will never get here")
#except ZeroDivisionError, err: # this form fails in Python 3.2
#    print("Got divide by zero: " + str(err))

# Works in both Python 2.7 and 3.2
# Here we catch several known exceptions and handle them in the same
# block of code
try:
    1/0
    print("Will never get here")
except (ZeroDivisionError, KeyError) as err:
    print("Got divide by zero: " + str(err))

try:
    1/0
    print("Will never get here")
except ZeroDivisionError:
    print("This is a ZeroDivisionError")
    # we can extract the traceback for logging
    import sys
    (tb_type, tb_value, tb_traceback) = sys.exc_info() # extract our traceback
    import traceback
    tb_as_list = traceback.extract_tb(tb_traceback)
    print("First bit of our traceback:" + str(tb_as_list)[:30] + "...")
    # and then re-raise the exception if it needs to go further up the line
    # by uncommenting the 'raise' statement on the next line - this 'raise'
    # will preserve the original stack/traceback
    #raise


