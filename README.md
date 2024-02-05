# "buckstop-refinery"
## Purpose
The purpose of buckstop-refinery is to provide a framework for building and
maintaining data warehouses by acquiring data, cleansing (refining) through an override
feature (errors in original source data), publishing into a warehouse, and then exporting
the data into different formats such as RDBMS, parquet files, Redis, Snowflake, etc.
so that it can be used by the enterprise.  The warehouse becomes the "one-version-of-the-truth".

## Pipeline Steps
### Acquire
This step is for downloading original vendor data from an online source,
and then uploading it to a destination and making a virtual link to the
latest version of that data on the basis of a time-slice, usually a calendar
day.  This step is important because it helps maintain a history of all
sources that are being used to create the warehouse.  Without this, original
sources may be archived.

### Stage
This step reads acquired data from what the Acquire step has produced
The step processes the raw vendor data, normalizing the
data into firm-agreed field names, reformatting where needed, filtering or 
ignoring irrelevant data, and then applying overrides in order to repair
data that has failed previously-found errors from a Check having been run.
The end of a stage is a proposed set of updates found when comparing the
staged results to the previous days worth of warehoused data for the source
in question.  The proposed newly staged data is then made available to the
next step, Check.

### Check
This step takes the result of the Stage step and applies checks that are
important to ensure the integrity of the data from a completeness point of
view and also for accuracy for those data that are present.  By
"completeness", we mean that the key that uniquely identifies the data
element is present as expected and has not been unexpectedly removed.
An "expected removal" would be due to some defined expiration policy for
a data element, whereas "unexpected removal" would be the opposite -- the
data appeared at one time in history, should still be present but has
disappeared due to some error in how the data was produced.  A Check failure
halts the steps and the failed check details are communicated via files
and messages to users monitoring the system.  The monitoring of failures
and warnings is handled by a Monitoring Plug-in.  A variety of monitoring
tools can be plugged in, e.g. Slack, SMS, Email.  An important and typical
step following Check is Override.  Override allows for changing data without
disturbing an original source data, and overrides can be end-dated so they
are no longer applied when the owner of source data makes corrections.

### House
If all checks succeed, the final updated file from Stage is symbolically 
linked to the new warehouse file for the day.  If any check had failed,
then the House step is not run automatically.  The House step can be force-run
if it is found that the Check result is acceptable, as in the case of a warning.
The details for Check results will indicate whether it is advisable and under what conditions
it might be that the House step could be run anyway.  The running of individual
steps in the pipeline is handled by Sequencing System Plug-In.  A variety of sequencing
plug-ins can be used, such as Jenkins, Apache airflow.

### Export
The master object (the warehouse ) is exported into a database or some other representation, e.g.
CSV, Parquet, HDF5, feather, Snowflake.

## Override System
### Override GUI
The overrides for erroneous data is controlled by a relational database, where
the key is the vendor, the region, the file and the valid-from through valid-to
date.  There will also be a specific field that identifies uniquely the record
in the staged data (see Stage step).  The key field is matched with the value
in the database, and the field to be repaired is matched for the old value
and the old value is replaced with the new value.

### Override System
The override software is called during Stage where a lookup of the data to
repair is performed in the Override DB by the key mentioned above.  The
software is run as a decorator and replaces the old (erroneous) value with the 
corrected value according to an override key.  An example would be to historically
change the salary of an employee if HR had inserted it a day late in the HR
database for employee salaries.

## Pipeline Scheduling System
A pipeline or job execution control system can be plugged in. Examples of
such systems are cron, Apache airflow, Jenkins.  Most systems are going
to have a way to declare job dependencies and also be able to display
an interactive GUI for step monitoring and step operations, such as running
or cancelling a step.

## Monitoring System
While orthogonal to the Pipeline control system, the Monitoring system allows
any communication stack to be plugged in for visibility, e.g. Slack.
When notification of a certain priority level or type
is produced, it appears in the chosen medium, and if that medium supports
updating status, a user can mark an items with a status such as "In Progress",
"Completed", etc.

### Pipeline Dependency Definition
Configuration files are supplied to define the steps and arguments to run
for the steps.  The arguments to the pipeline commands, implememented as
a Linux CLI, differ for each pipeline.  One step indicates the next step
to be executed after successful completion.  

### Pipeline GUI
The pipeline status should be visible in a GUI so that operators can notice
when something is failed and needs investigation.  If a Check step failure
is deemed to be acceptable, then the House step can be run by clicking on
the pipeline step in the GUI and instructing the GUI to Run the step.
