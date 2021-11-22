# Introduction
1. This is an instructions/guide document on how to run the HomeChef tool on the system.
2. This tool uses a GUI which opens as a separate window as soon as the code is executed.
3. All the output is displayed on the GUI.
4. Suggested ingredients that can be used for the search: Chicken, mushroom, potato, avocado

# How to Run
1. Instruction: Run HomeChefApp.py file 
2. Instruction Video: https://vimeo.com/630508238/d5bb2ad9d1

# Installing Additional Packages
1. **Install Selenium using conda**
> `conda install -c conda-forge selenium` 
- The import statements for all the installed packages are part of the code.

2. **Install pypdf2 using conda**
- Installing pypdf2 from the conda-forge channel can be achieved by adding conda-forge to your channels with:
> `conda config --add channels conda-forge`
- Once the conda-forge channel has been enabled, pypdf2 can be installed with:
> `conda install pypdf2`
- It is possible to list all of the versions of pypdf2 available on your platform with:
`conda search pypdf2 --channel conda-forge`

3.  **Install pyQT5**
- Run the following command to install pyQT5 on Anaconda:
> `conda install -c dsdale24 pyqt5`

4.  **Install ChromeDriver**
ChromeDriver is required for the code written on Selenium for scraping YoutTube and Google. The Selenium web driver speaks directly to the browser using the browser’s own engine to control it.
- Download Chrome WebDriver:
- Visit https://sites.google.com/a/chromium.org/chromedriver/download
- Select the compatible driver for your Chrome version
- To check the Chrome version you are using, click on the three vertical dots on the top right corner
- Then go to Help -> About Google Chrome
- Move the driver file to a PATH:
- Go to the downloads directory, unzip the file, and move it to usr/local/bin PATH
