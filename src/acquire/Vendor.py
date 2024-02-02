class Vendor():
    '''
    Class to represent a vendor file by path, vendor name, date, filename.

    Example:  my_path/vendor_name/date/filename

    There is a logical and physical location of a vendor file.
    The logical is the latest file for the time_frequency (date) in question.
    The default time_frequency is a single date
    A vendor_name is configured in the configuration system.
    my_path value will be dependent on whether the file lives in the logical or physical
    location.

    Objects of Class Vendor are used to pass around files and do object-like operations
    like check if equal.

    Equality of a file means that the file is the same in content and vendor_name/date/filename
    Notice that a logical and physical file could be the same even if they are at a different
    path.  This is so that we can see if a logical and physical file are the same content,
    same vendor_name, date and filename.  If they are, then they should be the same physical
    file but just linked to from logical to physical location.  This will prevent redundancy.


    '''

    pass