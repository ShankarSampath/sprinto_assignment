# Test Automation Assignment

This is Test Automation Assignment based on SeleniumBase & PYtest Framework with Python,cleartrip website.
Further i can integrate with CI- Jenkins part to make our scripts executable for each build. 


The collection of tests contains:
 * Book ticket for a week for Delhi & Bangalore based on price in Ascending Order 

## Project Structure
Here you can find a short description of main directories and it's content

* (data) -  there are sets of data for each tests
* (pages) - there are sets of method for each test step 
* (tests) - there are sets of tests for main functionalities of website
* (reports) - if you run tests with Allure, tests reports will be saved in this directory

## Project Features
* framework follows page object pattern
* the ability to easily generate legible and attractive test reports using Allure please find below steps
* its easy to execute in terminal using pytest markers -  (-m)

## To Start With

* To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file. Run the command below in terminal:

	```
	$ pip install -r requirements.txt
    $ pip install allure-pytest 
	```


## To Run Automation Test

* To run selected test without Allure report you execute in terminal using pytest markers 

```
pytest -m Regression --headless or pytest -m regression 
```


## Generate Test Report

To generate all tests report using Allure you need to run tests by command first:

pip install allure-pytest 
```
$ pytest -m Regression --alluredir=<reports directory path>
```

Here it is ## pytest -m regression --alluredir=reports  

After that you need to use command:
```
$ allure serve <reports directory path>
```

Here it is ## allure serve reports
