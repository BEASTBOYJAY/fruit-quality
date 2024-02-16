
# Apple Quality 

this the machine learning model in which I used RandomForesrClassifier and got sore of 87%.


## API Reference

#### Get item

```http
 import pandas as pd
```



| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `read_csv()` | `string` |  to read your dataframe |

#### Get item

```http
  from sklearn.tree import RandomForestClassifier
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `n_estimators`      | `int` | to input how many decision trees to train |
| `min_sample_split`      | `int` | to limit the minimum number of sample split|
| `min_sample_leaf`      | `int` | to limit the minimum number of leaf of a decision tree |
| `max_depth`      | `int` | to input the maximum number of level can a decision tree can go |



## Run Locally

Clone the project

```bash
  git clone https://github.com/BEASTBOYJAY/fruit-quality.git
```

Install dependencies

```bash
  pip Install pandas
  pip Install seaborn
  pip Install scikit-learn
  pip install streamlit
  pip install streamlit-lottie
```

Start the project,run in terminal

```bash
  streamlit run <file name> or Home_page.py
```


## Acknowledgements

 - [Sklearn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
 - [To learn RandomForest](https://youtube.com/playlist?list=PLKnIA16_RmvZyqP3WGUo7iVziIIea_1bp&si=KcAknxDZrjYo9QdY)


