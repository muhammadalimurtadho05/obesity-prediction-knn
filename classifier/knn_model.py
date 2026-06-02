import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  

import warnings
warnings.filterwarnings("ignore")

class knn_model:
    def __init__(self):
        FILE_PATH = 'classifier/dataset/dtts.xlsx'
        self.df = pd.read_excel(FILE_PATH)
        self.df.columns = self.df.columns.str.strip()
    
    def labelEncoding(self):
        categorical_cols = [
            "Gender", "family_history_with_overweight", "FAVC",
            "CAEC", "SMOKE", "SCC", "CALC", "MTRANS",
            "NObeyesdad" 
        ]
        
        label_encoders = {}
        df_encoded = self.df.copy()
        for col in categorical_cols:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
            label_encoders[col] = le
        
        return label_encoders, df_encoded
    
    def training_dataset(self):
        TARGET_COL = "NObeyesdad"
        label_encoders, df_encoded = self.labelEncoding()

        x = df_encoded.drop(columns=[TARGET_COL])
        y = df_encoded[TARGET_COL]

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size = 0.2, random_state = 42 
        )

        x_train = x_train.apply(pd.to_numeric, errors='coerce').fillna(0)
        x_test  = x_test.apply(pd.to_numeric, errors='coerce').fillna(0)

        model = KNeighborsRegressor(n_neighbors=3)
        model.fit(x_train, y_train)

        y_pred = model.predict(x_test)
        print(f"MAE : {mean_absolute_error(y_test, y_pred):.4f}")
        print(f"MSE : {mean_squared_error(y_test, y_pred):.4f}")
        print(f"R2  : {r2_score(y_test, y_pred):.4f}")

        return model, x_train
        
    def testing(self, test_raw):
        label_encoders, df_encoded = self.labelEncoding()
        model, x_train = self.training_dataset()


        sample_encoded = {}
        for col, val in test_raw.items():
            if col in label_encoders:
                sample_encoded[col] = label_encoders[col].transform([str(val)])[0]
            else:
                sample_encoded[col] = val
                
        sample_df = pd.DataFrame([sample_encoded])
        sample_df = sample_df[x_train.columns]
        sample_df = sample_df.apply(pd.to_numeric, errors='coerce').fillna(0)

        result = model.predict(sample_df)[0]          
        # inverse transform ke label asli
        label = label_encoders["NObeyesdad"].inverse_transform([round(result)])[0]
        # print(f"Prediksi (angka) : {result:.4f}")
        # print(f"Prediksi (label) : {label}")
        return label
