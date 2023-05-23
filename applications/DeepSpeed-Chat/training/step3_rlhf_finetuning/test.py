from datasets import load_dataset

dataset = load_dataset('/data/fze/dataset/PKU-SafeRLHF-10K')['train'].train_test_split(test_size=0.1)
print(dataset.column_names)
# train_set = dataset['train'].train_test_split(test_size=0.1)
print(dataset['train'])
print(len(dataset['train']))