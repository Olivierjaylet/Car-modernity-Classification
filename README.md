# Car Modernity Classification with Transfer Learning

This project applies transfer learning using a pre-trained ResNet-18 model to classify car modernity based on images. 
The goal is to categorize car designs by their production year and calculate a modernity score, which reflects the automotive design evolution.

## Project Overview

The project focuses on using transfer learning to extract visual attributes from car images and predict their design modernity. The modernity score is a weighted sum of predicted probabilities for different year categories. The deep learning pipeline leverages a pre-trained ResNet-18 model on ImageNet and adapts it to classify cars into production year ranges.

### Key Features:
- **Transfer Learning**: Fine-tuning a ResNet-18 model pre-trained on ImageNet.
- **Modernity Score Calculation**: Classifying car designs into production year categories and calculating a weighted modernity score.
- **PyTorch Implementation**: Using PyTorch for building and training the model.
- **Dataset**: DVM-CAR dataset, with car images labeled by production year.

## Dataset

The dataset used in this project is the **DVM-CAR** dataset, which contains car images labeled with details such as brand, model, production year, and color. The images are categorized into five production year ranges:
- **0**: 2000-2003
- **1**: 2006-2008
- **2**: 2009-2011
- **3**: 2012-2014
- **4**: 2015-2017

### Data Preprocessing:
- **Train/Validation/Test Split**: The dataset is split into 70% training, 20% validation, and 10% test sets. Car models are kept intact within each split.
- **Image Resizing**: All images are resized to 224x224 pixels to match the input size expected by ResNet-18.
- **Normalization**: Images are normalized using the mean and standard deviation of ImageNet.
- **Data Augmentation**: Random cropping and resizing transformations are applied to the training dataset for better generalization.

## Model Architecture

We use a **ResNet-18** model pre-trained on ImageNet for feature extraction. Two transfer learning strategies are explored:
1. **Fixed Feature Extractor**: Using ResNet-18 as a fixed feature extractor and training only the final classification layer.
2. **Fine-tuning**: Fine-tuning the entire ResNet-18 model, along with the newly added classification layer.

### Modernity Score Calculation:
The modernity score for a car is computed as the weighted sum of predicted probabilities across production year categories.

