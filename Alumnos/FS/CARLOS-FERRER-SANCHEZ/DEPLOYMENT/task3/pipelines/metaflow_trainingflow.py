from metaflow import FlowSpec, Parameter, step
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

class TrainingFlow(FlowSpec):
    max_depth = Parameter('max_depth', default=2, help='Max depth of the random forest classifier')
    n_estimators = Parameter('n_estimators', default=100, help='Number of estimators for the random forest classifier')
    random_state = Parameter('random_state', default=0, help='Random state for the random forest classifier')
    
    @step
    def start(self):
        self.next(self.ingest_data)
        
    @step
    def ingest_data(self):
        from sklearn.datasets import load_iris
    
        iris = load_iris()
        
        self.X = iris.data
        self.y = iris.target
        
        self.next(self.split_data)

    @step
    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.random_state)
        self.next(self.train)

    @step
    def train(self):
        self.model = RandomForestClassifier(
            max_depth=self.max_depth,
            n_estimators=self.n_estimators,
            random_state=self.random_state
        )
        self.model.fit(self.X_train, self.y_train)
        self.next(self.show_metrics)

    @step
    def show_metrics(self):
        self.y_pred = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.report = classification_report(self.y_test, self.y_pred)
        print(f"Accuracy: {self.accuracy}")
        print(f"Classification Report:\n{self.report}")
        self.next(self.register_model)
        
    @step
    def register_model(self):
        with open('random_forest_model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
        print("Model saved as random_forest_model.pkl")
        self.next(self.end)
        
    @step
    def end(self):
        pass
    
if __name__ == '__main__':
    TrainingFlow()
