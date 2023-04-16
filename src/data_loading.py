from datasets import load_dataset

train_dataset = load_dataset('GEM/xmediasum', split='train')

# print(dataset.keys())
# print(len(dataset['train']))
# print(len(dataset['test']))
# print(len(dataset['validation']))

print(train_dataset[0].keys())
