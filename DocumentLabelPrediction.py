# Written for Python 3.6
topics = {"Diabetes": "labeled-1.txt",
          "CompSci": "labeled-2.txt"}

unlabeledDocs = ["unlabeled-1.txt", "unlabeled-2.txt", "unlabeled-3.txt", "unlabeled-4.txt",
                 "unlabeled-5.txt", "unlabeled-6.txt"]

stopWords = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once",
             "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for",
             "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is",
             "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until",
             "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were",
             "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above",
             "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before",
             "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then",
             "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he",
             "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i",
             "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing",
             "it", "how", "further", "was", "here", "than"]

topicDictionaries = []
# Will specify the topic of each dictionary in topicDictionaries (Alternative to nested dictionaries)
topicDictionaryLabels = []

# Keeps number of correct and incorrect label predictions
TP = 0
FP = 0

# Populate topic dictionaries by reading labeled documents
for topic in topics:

    bagOfWords = []
    bagOfWordsCount = 0

    file = open(topics[topic], "r")
    textString = file.read().lower().split()

    # Populate bag of words
    for word in textString:

        bagOfWordsCount = bagOfWordsCount + 1

        if word not in stopWords:
            bagOfWords.append(word)

    topicDict = {}

    # Create map of words and their frequencies
    for word in bagOfWords:

        if word in topicDict:
            topicDict[word] = topicDict[word] + 1
        else:
            topicDict[word] = 1

    # Calculate word weights (word count/ bagOfWordsCount)
    for word in topicDict:

        topicDict[word] = (topicDict[word] / bagOfWordsCount)

    topicDictionaries.append(topicDict)
    topicDictionaryLabels.append(topic)

# Read unlabeled documents and then apply topicDictionary weights to predict documents' labels
for document in unlabeledDocs:

    print("========== " + document + " ==========")
    bagOfWords = []
    weightSums = {}

    file = open(document, "r")
    textString = file.read().lower().split()

    # Populate bag of words
    for word in textString:

        if word not in stopWords:
            bagOfWords.append(word)

    # Calculate weightSums of bag of words for each topic dictionary
    for i in range(len(topicDictionaries)):

        weightSum = 0

        for word in bagOfWords:

            if word in topicDictionaries[i]:

                weightSum = weightSum + topicDictionaries[i][word]

        weightSums[topicDictionaryLabels[i]] = weightSum

        print(topicDictionaryLabels[i] + ": " + str(weightSums[topicDictionaryLabels[i]]))

    Max = weightSums[topicDictionaryLabels[0]]
    MaxTopic = topicDictionaryLabels[0]

    for Sum in weightSums:

        if weightSums[Sum] > Max:
            Max = weightSums[Sum]
            MaxTopic = Sum

    print("Predicted topic: " + MaxTopic)

    # Determine if predicted topic was correct
    if document == "unlabeled-1.txt":
        if MaxTopic == "CompSci":
            TP = TP + 1
        else:
            FP = FP + 1
    elif document == "unlabeled-2.txt":
        if MaxTopic == "CompSci":
            TP = TP + 1
        else:
            FP = FP + 1
    elif document == "unlabeled-3.txt":
        if MaxTopic == "CompSci":
            TP = TP + 1
        else:
            FP = FP + 1
    elif document == "unlabeled-4.txt":
        if MaxTopic == "CompSci":
            TP = TP + 1
        else:
            FP = FP + 1
    elif document == "unlabeled-5.txt":
        if MaxTopic == "Diabetes":
            TP = TP + 1
        else:
            FP = FP + 1
    elif document == "unlabeled-6.txt":
        FP = FP + 1
    else:
        print("Unknown document scanned")

precision = TP/(TP + FP)
print("="*37)
print("Precision score: " + str(precision))
