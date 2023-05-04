### Visa Approval Machine Learning Pipeline

Visa Approval means written confirmation or grant certificate provided by Specific authority of country to the person based on predefined criteria.
You have met all the qualifications and are approved to receive a visa.Visa approval used to facilitate the visa application process for a person traveling to another country for a specific purpose.

### Problem Statement
Visa Approval is a manual process by any country which is very time consuming task but this Machine learning models help to shortlist the visa application of person to avoid the manual task to reduce the human intervention and speedup the process based on their previous data.
 
#### In this project we are going to build a Classification based model.
* This model is to check if Visa get approved or not based on the given dataset.
* This can be used to Recommend a suitable profile for the applicants for whom the visa should be certified or denied based on the certain criteria which influences the decision.

### Data Description

The client will send data in multiple sets of files in batches at a given location.Data will contain different Case id and 10 columns of different attributes for case id which is mention as below.The last column will have the "Denied/Certified" value for each case id.

#### Field Name and its description
  The data contains the different attributes of the employee and the employer. The detailed data dictionary is given below.

* continent	--A continent is a large continuous mass of land conventionally regarded as a collective region. There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia (listed from largest to smallest in size). Sometimes Europe and Asia are considered one continent called Eurasia.
* education_of_employee	--This field having generally four categories of degrees  of employee which are bechelor's,Doctorate,Master's and High School
* has_job_experience	--Does the employee has any job experience? Y= Yes; N = No
* requires_job_training	 --This field indicate that is any job training required to employee.Y = Yes; N = No
* no_of_employees	--Number of employees in the employer's company
* yr_of_estab	--Year in which the employer's company was established
* region_of_employment --This filed indicate details of the areas, zones, lands of country that belongs to an employee.
* prevailing_wage	 --the average wage paid to similarly employed workers in a specific occupation in the area of intended employment
* unit_of_wage	--Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly
* full_time_position --Is the position of work full-time? Y = Full Time Position; N = Part Time Position

### Data Validation
Apart from training files, we also require a "schema" file from the client, which contain all the relevant information about the training files such as:
* Name of the files, 
* Length of Date value in FileName, 
* Length of Time value in FileName, 
* Number of Columnns, 
* Name of Columns and
* their dataype

In This step, we perform different sets of validation on the given set of training files.
    
* Name Validation: We validate the name of the files based on the given name in the schema file. We have  created a regex patterg as per the name given in the schema fileto use for validation. After validating the pattern in the name, we check for the length of the date in the file name as well as the length of time in the file name. If all the values are as per requirements, we move such files to "Good_Data_Folder" else we move such files to "Bad_Data_Folder."
    
* Number of Columns: We validate the number of columns present in the files, and if it doesn't match with the value given in the schema file, then the file id moves to "Bad_Data_Folder."
    
* Name of Columns: The name of the columns is validated and should be the same as given in the schema file. If not, then the file is moved to "Bad_Data_Folder".
    
* The datatype of columns: The datatype of columns is given in the schema file. This is validated when we insert the files into Database. If the datatype is wrong, then the file is moved to "Bad_Data_Folder."
    
* Null values in columns: If any of the columns in a file have all the values as NULL or missing, we discard such a file and move it to "Bad_Data_Folder".

### Configuration Details

This project is set up like a standard Python project. The initialization process also creates a virtualenv within this project, stored under the .venv directory. To create the virtualenv it assumes that there is a python3 executable in your path with access to the venv package. If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv manually once the init process completes.

To manually create a virtualenv on windows:
```bash
python -m venv .venv
```
you would activate the virtualenv like this:
```bash
.venv\Scripts\activate.bat
```
if you are getting below error at the time of activating virtual environment then run below mention code to solve the error.

```bash
D:\End_to_End_ML_Project\Project_ML_Pipeline\visa_approval_ml_pipeline\.venv\Scripts\Activate.ps1 cannot be loaded 
because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
```

```bash
solution
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
```

Once the virtualenv is activated, you can install the required dependencies.
```bash
pip install -r requirements.txt
```



Execution of this project is started from main.py python file.we need to run this project using below mention command.

```bash 
Python main.app
```

There is two option available out of which one is used for manual file prediction and other is for already in prediction batch file. We have to give the absolute path where the file is kept for production.

Once prediction is completed the file will be placed at prediction output file.



* Create conda environment 
```bash
conda create -n <env_name> python=<version_number>

```

* Activate created conda environment
```bash
activate conda <env_name>

```

*To create and run requirements file
```bash
pip freeze > requirements.txt
pip install -r requirements.txt

```

* Execution of workflow `without` new conda environment
```bash
mlflow run . --no-conda
```

* Execution of workflow `with` new conda environment
```bash
mlflow run .

```
* Execution of workflow `without` new conda environment with parameter
```bash
mlflow run . -P param=values --no-conda

```

* Run only entry point
```bash
mlflow run . -e <entry-point-name> --no-conda
```

* Basic Git command used in this project
```bash
git init  # Initialize the  folder as local git folder.
git add . # Add the changes in stagging area.
git commit -m "<message name>"  # Commit the changes in local system.
git branch -M main   # Change the branch name.
git remote add origin <'github_repo_url'>  # Add the git repository.
git push origin main # Upload the changes done in local system to git repo.
```


### Screen shot
Below are some screen shot of runnable project.

### Deployment

