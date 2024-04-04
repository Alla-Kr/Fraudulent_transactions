# Fraudulent_transactions
Classification task (detecting fraudulent transactions)

## Task
It is necessary to implement a set of measures to detect fraud in the banking sector.
It is necessary to detect situations when a fraudster makes payments on a card without the knowledge of the owner. One of the most effective tools for solving the problem of identifying fraudulent banking transactions is machine learning. Note that the sample is often unbalanced and cannot be so; fraudulent transactions of the total number of transactions fluctuate around 2%.

### Metric selection
In our case, having an unbalanced sample, Accuracy is not applicable.
If it is important to minimize false negatives, then the Recall metric will be more appropriate. Recall measures the proportion of all true positive cases that the model classified correctly.
Thus, the higher the Recall, the fewer false negatives the model has. This is especially important in cases where false negatives can have serious consequences
In such tasks that solve the problem of detecting high risk, the Recall metric is the most suitable; you can also focus on the complex metric F 1 score.

**Technical task:** build a machine learning model that, based on the proposed characteristics of transactions, will predict the class - whether the transaction is fraudulent or not.

**Main goals of the project:**
1. Create a dataset from multiple sources of information.
2. Design new features using Feature Engineering and identify the most important ones when building the model.
3. Examine the data provided and identify patterns.
4. Build several models and select the best one based on a given metric.
5. Develop a service for production

### Result
Jupyter notebook with completed tasks and conclusions:
- [Full notebook (version recommended for viewing)](Transaction_fraud_project_FULL_version.ipynb)
- [Notebook with solution (several graphs have been shortened as well as several outputs to reduce file weight)](Transaction_fraud_project(fewer_graphs).ipynb)
- [ML section](Transaction_fraud_project_ML.ipynb)
- [WEB](web)
  
__Please note that I obtained these data myself; they reflect the real state of affairs in the banking transaction industry. The industry is evolving and so is fraud. It is difficult to identify dependencies by eye, and machine learning algorithms help cope with the task with enviable accuracy.__
