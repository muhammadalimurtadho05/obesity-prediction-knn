import pandas as pd
import math

class knn_model:
    def __init__(self):
        FILE_PATH = 'classifier/dataset/dtts.xlsx'
        self.df = pd.read_excel(FILE_PATH)
        self.df.columns = self.df.columns.str.strip()
    
    def labelEncoding(self):
        categorical_cols = [
            "Gender", "family_history_with_overweight", "FAVC",
            "CAEC", "SMOKE", "SCC", "CALC", "MTRANS", "NObeyesdad"
        ]
        
        label_encoders  = {} 
        label_decoders = {} 
        df_encoded = self.df.copy()
        for col in categorical_cols:
            unique_vals = sorted(df_encoded[col].astype(str).unique())
            mapping     = {v: i for i, v in enumerate(unique_vals)}
            inv_mapping = {i: v for v, i in mapping.items()}
            df_encoded[col] = df_encoded[col].astype(str).map(mapping)
            label_encoders[col] = mapping
            label_decoders[col] = inv_mapping

        return label_encoders, label_decoders, df_encoded
    
    def euclidean(self, df_encoded, fitur, test_encoded, target):
        distances = []
        for idx, row in df_encoded.iterrows():
            dist = math.sqrt(sum(
                (test_encoded.get(col, 0) - row[col]) ** 2
                for col in fitur
            ))
            
            distances.append((dist, row[target]))
        return distances
    
    def predict(self, test_row :dict, k :int = 3):
        label_encoders, label_decoders, df_encoded = self.labelEncoding()
        
        test_encoded = {}
        
        for col, val in test_row.items():
            if col in label_encoders:
                test_encoded[col] = label_encoders[col].get(str(val), -1)
            else:
                test_encoded[col] = val
        
        target = "NObeyesdad"
        fitur = [col for col in df_encoded.columns if col != target]
        distances = self.euclidean(df_encoded,fitur,test_encoded,target)
        
        
        distances.sort(key=lambda x: x[0])
        knn = distances[:k]
        votes = {}
        for _, label in knn:
            if label in votes:
                votes[label] += 1
            else:
                votes[label] = 1
        predicted_encoded = max(votes, key=votes.get)

        # Decode hasil prediksi
        predicted_label = label_decoders[target][predicted_encoded]
        return predicted_label


    

# model = knn_model()
# label_encoders, label_decoders, df_encoded = model.labelEncoding()
# sample_raw = {
#     "Gender": "Male",
#     "Age": 25,
#     "Height": 1.75,
#     "Weight": 90,
#     "family_history_with_overweight": "yes",
#     "FAVC": "yes",
#     "FCVC": 2,
#     "NCP": 3,
#     "CAEC": "Sometimes",
#     "SMOKE": "no",
#     "CH2O": 2,
#     "SCC": "no",
#     "FAF": 1,
#     "TUE": 1,
#     "CALC": "Sometimes",
#     "MTRANS": "Public_Transportation"
# }

# tes = model.predict(sample_raw)
# print(tes)