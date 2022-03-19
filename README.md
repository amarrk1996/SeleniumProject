##Installation
Install python (latest 3.8)
Install Pycharm
Configure Pycharm with selenium package (selenium should be associated with the project)
Created the package>> C:\Users\Amar\PycharmProjects\SeleniumProject
directory where py is installed(executable location)>>cd C:\Users\Amar\PycharmProjects\SeleniumProject\venv\Scripts
check if selenium is installed>>pip list
pip command to install selenium>>pip install -U selenium

##Run selenium tests on Chrome, Firefox & IE browser
Pre-requisites
Download Chrome, Firefox & IE Drivers
#Keep all 3 downloaded zip files in single folder and extract them
#Packages to be import:
from selenium import webdriver
from selenium.webdriver.common.keys import keys

>Launching the application
>Print Title and current url
>Navigation Backward and Forward
>Conditional Command

Locators

Text Box :

Radio Button :
CheckBox :
Drop Down :
Mouse Right Click :
Mouse double Click :


Important Links
Top 8 Python Testing Frameworks in 2021
https://blog.testproject.io/2020/10/27/top-python-testing-frameworks/

https://dev.azure.com/amarrkayapure/amarrkayapure/_apps/hub/ms.vss-build-web.ci-designer-hub

local git repository (same as current project location of pycharm)
C:\Users\Amar\PycharmProjects\SeleniumProject

git hub repository
https://github.com/amarrk1996

devops repos git repository
https://dev.azure.com/amarrkayapure/amarrkayapure/_git/MySeleniumProject

About unittest frame work
Important!!!! : Since based on Junit, camelCase naming method is in use, instead of Python’s snake_case naming convention

PyUnit (Unittest)
PyUnit (Unittest) is a unit testing framework for Python that was inspired by JUnit. It is the default Python testing framework that comes out of the box with the Python package, and thus the one most developers start their testing with.

Pros

Since it is part of the standard Python library there are no additional modules required to install – it comes out of the box with the Python package.
Offers simple and flexible test case execution.
Quick generation of test reports, both XML reports and unittest-sml-reporting.
Cons

The intent of the test code sometimes becomes unclear, since it supports abstraction.
A huge amount of boilerplate code is required.
Since based on Junit, camelCase naming method is in use, instead of Python’s snake_case naming convention.
Bottom line: If you are looking for basic unit testing and are familiar with xUnit frameworks, you will find it very easy to get started with PyUnit and it would probably be the most comfortable one for you, with no need for any additional dependencies





