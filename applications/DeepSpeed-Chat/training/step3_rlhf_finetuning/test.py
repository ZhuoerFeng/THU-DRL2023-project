from datasets import load_dataset

dataset = load_dataset('/data/fze/dataset/PKU-SafeRLHF-10K')
print(dataset.column_names)
train_set = dataset['train']
print(train_set[0])