from metaflow import FlowSpec, Parameter, step

class TrainingFlow(FlowSpec):
    # Define the parameters for the flow
    max_depth = Parameter('max_depth', default=2, help='Max depth of the random forest classifier')
    n_estimators = Parameter('n_estimators', default=100, help='Number of estimators for the random forest classifier')
    random_state = Parameter('random_state', default=0, help='Random state for the random forest classifier')
    
    @step
    def start(self):
        # Start the flow
        self.next(self.ingest_data)
        
    @step
    def ingest_data(self):
        from sklearn.datasets import load_iris
    
        # Load the iris dataset
        iris = load_iris()
        
        self.X = iris.data
        self.y = iris.target
        
        self.next(self.split_data)

    @step
    def split_data(self):
        from sklearn.model_selection import train_test_split
        # Split the data into train and test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.next(self.train)

    @step
    def train(self):
        from sklearn.ensemble import RandomForestClassifier
        # Train the model
        self.rf = RandomForestClassifier(max_depth=self.max_depth, n_estimators=self.n_estimators, random_state=self.random_state)
        self.rf.fit(self.X_train, self.y_train)
        self.next(self.show_metrics)

    @step
    def show_metrics(self):
        from sklearn.metrics import classification_report
        # Print some metrics
        y_pred = self.rf.predict(self.X_test)
        print(classification_report(self.y_test, y_pred))
        self.next(self.register_model)
        
    @step
    def register_model(self):
        import pickle
        # Save the model in a pickle file in local storage
        with open("model.pkl", "wb") as f:
            pickle.dump(self.rf, f)
        self.next(self.end)
        
    @step
    def end(self):
        pass
    
if __name__ == '__main__':
    TrainingFlow()
