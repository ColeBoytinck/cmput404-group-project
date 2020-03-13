# cmput404-group-project
Group project for the 404, team EarlyBirds

Website URL: https://cmput404-group-project-mandala.herokuapp.com/

# Documentation
### Documentation can be found on our GitHub Wiki or from the links below
[Endpoint Documentation](https://github.com/AustinGrey/cmput404-group-project/wiki/Endpoints-Documentation)<br>
[Front End Documentation](https://github.com/AustinGrey/cmput404-group-project/wiki/Front-End-Documentation)<br>
[UI Storyboard](https://github.com/AustinGrey/cmput404-group-project/wiki/UI-Storyboard)<br>

# Test Data
## Creating Test Data
The following command will create a copy of your database and dump it into a file for others to load

    python manage.py dumpdata --indent 2 --format yaml > test_data.yaml

## Loading Test Data
The following command will load the file created in the above command into your database

    python manage.py loaddata test_data.yaml
