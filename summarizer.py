import numpy as np
import pandas as pd
import nltk
#nltk.download('punkt')
# one time execution
import re
from rouge import Rouge

df = pd.read_csv('tennis_articles_v4.csv')
print(df.head())
print()

print(df['article_text'][0])
print()
print(df['article_text'][1])
print()
print(df['article_text'][2])
print()

from nltk.tokenize import sent_tokenize
sentences = []
for s in df['article_text']:
  sentences.append(sent_tokenize(s))

sentences = [y for x in sentences for y in x] # flatten list

print(sentences[:5])
print()

word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

print(len(word_embeddings))
print()

# remove punctuations, numbers and special characters
clean_sentences = pd.Series(sentences).str.replace('[^a-zA-Z]', ' ')

# make alphabets lowercase
clean_sentences = [s.lower() for s in clean_sentences]

# nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

# function to remove stopwords
def remove_stopwords(sen):
    sen_new = ' '.join([i for i in sen if i not in stop_words])
    return sen_new

# remove stopwords from the sentences
clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

# Extract word vectors
word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

sentence_vectors = []
for i in clean_sentences:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((100,))
  sentence_vectors.append(v)


# similarity matrix
sim_mat = np.zeros([len(sentences), len(sentences)])

from sklearn.metrics.pairwise import cosine_similarity

for i in range(len(sentences)):
  for j in range(len(sentences)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

import networkx as nx

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

# Extract top 10 sentences as the summary
for i in range(10):
  print(ranked_sentences[i][1])

ar1 = "When I'm on the courts or when I'm on the court playing, I'm a competitor and I want to beat every single person whether they're in the locker room or across the net.So I'm not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match. Major players feel that a big event in late November combined with one in January before the Australian Open will mean too much tennis and too little rest. Speaking at the Swiss Indoors tournament where he will play in Sundays final against Romanian qualifier Marius Copil, the world number three said that given the impossibly short time frame to make a decision, he opted out of any commitment. 'I felt like the best weeks that I had to get to know players when I was playing were the Fed Cup weeks or the Olympic weeks, not necessarily during the tournaments. Currently in ninth place, Nishikori with a win could move to within 125 points of the cut for the eight-man event in London next month. He used his first break point to close out the first set before going up 3-0 in the second and wrapping up the win on his first match point. The Spaniard broke Anderson twice in the second but didn not get another chance on the South Africans serve in the final set. 'We also had the impression that at this stage it might be better to play matches than to train. The competition is set to feature 18 countries in the November 18-24 finals in Madrid next year, and will replace the classic home-and-away ties played four times per year for decades. Federer said earlier this month in Shanghai in that his chances of playing the Davis Cup were all but non-existent."

ar2 = "When Im on the courts or when Im on the court playing, Im a competitor and I want to beat every single person whether theyre in the locker room or across the net.So Im not the one to strike up a conversation about the weather and know that in the next few minutes I have to go and try to win a tennis match. I think just because youre in the same sport doesnt mean that you have to be friends with everyone just because youre categorized, youre a tennis player, so youre going to get along with tennis players. Seeking a ninth title at his hometown event, and a 99th overall, Federer will play 93th-ranked Marius Copil on Sunday. Nishikori held serve throughout against Kukushkin, who came through qualifying. He used his first break point to close out the first set before going up 3-0 in the second and wrapping up the win on his first match point. But first the 20-time Grand Slam winner wants to train on the Paris Masters court this afternoon before deciding whether to appear for his opening match against either Milos Raonic or Jo-Wilfried Tsonga. On Monday, I am free and will look how I feel, Federer said after winning the Swiss Indoors."
rouge = Rouge()
scores = rouge.get_scores(ar1,ar2)
print(scores)