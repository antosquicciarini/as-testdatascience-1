# Dataset Overview

This project uses the Forest CoverType dataset from the UCI Machine Learning Repository.

## 🌲 Dataset Summary

- **Source**: https://archive.ics.uci.edu/dataset/31/covertype  
- **Instances**: 581,012  
- **Features**: 54 (10 numerical, 44 binary)  
- **Target**: Cover type (7 forest categories)  
- **Missing Values**: None  

The dataset contains cartographic variables from the US Forest Service Region 2. Each sample represents a 30x30 meter cell of forest.

## 🔢 Feature Types

**Numerical features (10):**

- Elevation  
- Aspect  
- Slope  
- Horizontal_Distance_To_Hydrology  
- Vertical_Distance_To_Hydrology  
- Horizontal_Distance_To_Roadways  
- Hillshade_9am  
- Hillshade_Noon  
- Hillshade_3pm  
- Horizontal_Distance_To_Fire_Points  

**Categorical (one-hot encoded):**

- Wilderness_Area1 to Wilderness_Area4 (4 binary features)  
- Soil_Type1 to Soil_Type40 (40 binary features)

## 🎯 Target Variable

- `Cover_Type` is a categorical variable with 7 classes:
  1. Spruce/Fir
  2. Lodgepole Pine
  3. Ponderosa Pine
  4. Cottonwood/Willow
  5. Aspen
  6. Douglas-fir
  7. Krummholz

Classes are imbalanced, with types 1 and 2 being most frequent.

## 🧹 Preprocessing Summary

- No missing values → no imputation needed.
- Numerical features are standardized using `StandardScaler`.
- Binary features are concatenated post-scaling.
- Train/test split: 80% train, 20% test with stratification on target.

## 📊 Exploratory Data Analysis (EDA)

Key steps performed in the notebook:

- Class distribution plot  
- Feature correlation matrix  
- PCA for variance explanation  
- t-SNE and UMAP for visualizing class separability  
- Mutual information heatmap for feature relevance  
- Analysis of target class vs. elevation, hillshade, and distances  
- Soil_Type and Wilderness_Area class-wise profiles

For plots and further details, see `notebooks/covertype.ipynb`.