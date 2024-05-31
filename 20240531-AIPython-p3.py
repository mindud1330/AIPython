from sklearn import tree
import matplotlib.pyplot as plt

parents_height = [[180,165],[175, 160],[180,172],[165,160],[171,152]]
child_height = [3,2,2,1,1]

# dicision tree model
dt_model = tree.DecisionTreeClassifier() 
dt_model.fit(parents_height, child_height)

# predict value
input_value = [[175,153]]
dt_pred=dt_model.predict(input_value)
print(dt_pred)
