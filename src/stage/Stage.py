class Stage():
    '''
    Used to stage data to a staging location from a parsed Vendor object.

    A Vendor object represents a vendor file.
    That file is parsed with a Stage object and then placed into a staged location
    for checking by a Check object for that particular Stage object.

    Stage objects are represented in storage as a path/region/category/name
    where the path is the staging_path, region is a region like "eu", "us", etc. from
    the set of Region objects.

    Category is the type of warehouse file that is being represented by the Stage object,
    for example a "sid" for a symbol identifier.  A Category will represent a "type identifier"
    in the system.  So, if there is a typed object like Job or WorkOrder or Symbol Identifier
    there would be categories of "job_id", "work_order_id", and "symbol_id"

    A Job warehouse file would then be like: path/region/job_id/date/job_id.subtype.csv
    e.g. /myroot/us-east/rockefeller/eu/job_id/2024/01/04/job_id.minerals.csv

    This would be a region "eu" warehouse file for mineral jobs created for 2024/01/04.

    TODO:
    Subtype is another way to distinguish warehouses across job_id's.
    There may be job_id's for certain types of jobs, that sub-type of a Job will be the subtype
    name. May change depending on requirements
    We can make this flexible later if need be.
    '''
    pass