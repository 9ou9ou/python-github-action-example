# CICD Tutoriel

Welcome aboard dear reader, in this repository, you will find the differents setups and configurations used to create a **CI/CD** to heroku Service.

## The application 
We will beguin with the application running in the local environment. It is a really simple application that show Hello World message. To run it, you can run the following command

``` bash
git clone https://github.com/9ou9ou/python-github-action-example.git
cd python-github-action-example
python3 src/app.py
```

Also a unit function is implemented to test the returned value of the index function. To run it, you simply specify the python src path and use pytest like the following

```
export PYTHONPATH=src
pytest
```

We obtain this result
![](images/test.png)

## Continous Integration
In this paragraph, we will speak about the process of **CI** using Github action. To this reason, we created a workflow under the **.github/workflows** folder