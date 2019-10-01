# Text-Summerizer
Automatic summarization involves reduces a text file into a passage or paragraph that conveys the main meaning of the text. The searching of important information from a large text file is very difficult job for the users thus to automatic extract the important information or summary of the text file. 



### Introduction

Text summarization is the process of reducing a text Document with a computer program in order to create a summary that retains the most important points of the original document. As The problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. It is very difficult for human beings to manually summarize large documents of text. Text Summarization methods can be classified into extractive and abstractive summarization. An extractive summarization method consists of selecting important sentences, paragraphs etc. from the original document and concatenating them into shorter form. The importance of sentences is decided based on statistical and linguistic features of sentences. Extractive methods work by selecting a subset of existing words, phrases, or sentences in the original text to form the summary. The extractive summarization systems are typically based on techniques for sentence extraction and aim to cover the set of sentences that are most important for the overall understanding of a given document.

### Methodolgy

### The TextRank Model

Graph-based ranking algorithms are essentially a way of deciding the importance of a vertex within a graph, based on global information recursively drawn from the entire graph. The basic idea implemented by a graph-based ranking model is that of “voting” or “recommendation”. When one vertex links to another one, it is basically casting a vote for that other vertex. The higher the number of votes that are cast for a vertex, the higher the importance of the vertex. Moreover, the importance of the vertex casting the vote determines how important the vote itself is, and this information is also taken into account by the ranking model. Hence, the score associated with a vertex is determined based on the votes that are cast for it, and the score of the vertices casting these votes. Formally, let be a directed graph with the set of vertices V and set of edges E For a given vertex Vi
The score of a vertex is defined as follows (Brin and Page, 1998):

 
<img width="639" alt="Screenshot 2019-10-01 at 1 16 03 PM" src="https://user-images.githubusercontent.com/45623734/65943664-a26a4900-e44d-11e9-8a2f-113073f56605.png">

Consequently,a new formula for graph-based ranking that takes into account edge weights when computing the score associated with a vertex in the graph. Notice that a similar formula can be defined to integrate vertex weight-

<img width="690" alt="Screenshot 2019-10-01 at 1 16 23 PM" src="https://user-images.githubusercontent.com/45623734/65943676-ad24de00-e44d-11e9-908b-86b8db12831d.png">



### TextRank Algorithm-

TextRank is an extractive and unsupervised text summarization
technique.TextRank algorithm that we will be following:

• The first step would be to concatenate all the text contained in the
  articles
• Then split the text into individual sentences
• In the next step, we will find vector representation (word embeddings) for each and every sentence
• Similarities between sentence vectors are then calculated and stored in a matrix
• The similarity matrix is then converted into a graph, with sentences as vertices and similarity scores as edges, for             sentence rank calculation
• Finally, a certain number of top-ranked sentences form the final summary


### Sentence Extraction -
The other TextRank application that we investigate consists of sentence extraction for automatic summarization. In a way, the problem of sentence extraction can be regarded as similar to keyword extraction, since both applications aim at identifying sequences that are more “representative” for the given text. In keyword extraction, the candidate text units consist of words or phrases, whereas in sentence extraction, we deal with entire sentences. TextRank turns out to be well suited for this type of applications, since it allows for a ranking over text units that is recursively computed based on information drawn from the entire text.


### TextRank for Sentence Extraction-

To apply TextRank, we first need to build a graph associated with the text, where the graph vertices are representative for the units to be ranked. For the task of sentence extraction, the goal is to rank entire sentences, and therefore a vertex is added to the graph for each sentence in the text. The co-occurrence relation used for keyword extraction cannot be applied here, since the text units in consideration are significantly larger than one or few words, and “co-occurrence” is not a meaningful relation for such large contexts. Instead, we are defining a different relation, which determines a connection between two sentences if there is a “similarity” relation between them, where “similarity” is measured as a function of their content overlap. Such a relation between two sentences can be seen as a process of “recommendation”: a sentence that addresses certain concepts in a text, gives the reader a “recommendation” to refer to other sentences in the text that address the same concepts, and therefore a link can be drawn between any two such sentences that share common content. The overlap of two sentences can be determined simply as the number of common tokens between the lexical representations of the two sentences, or it can be run through syntactic filters, which only count words of a certain syntactic category, e.g. all open class words, nouns and verbs, etc. Moreover, to avoid promoting long sentences, we are using a normalization factor, and divide the content overlap of two sentences with the length of each sentence. Formally, given two sentences and , with a sentence being represented by the set of words that appear in the sentence:S, the similarity of Si and Sj is defined as:

<img width="690" alt="Screenshot 2019-10-01 at 1 19 07 PM" src="https://user-images.githubusercontent.com/45623734/65943838-0f7dde80-e44e-11e9-857c-39b2ee148d14.png">


### Conclusion

TextRank – a graph based ranking model for text processing, and show how it can be successfully used for natural language applications. In particular, we proposed and evaluated two innovative unsupervised approaches for keyword and sentence extraction, and showed that the accuracy achieved by TextRank in these applications is competitive with that of previously proposed state-of-the-art algorithms. An important aspect of TextRank is that it does not require deep linguistic knowledge, nor domain or language specific annotated corpora, which makes it highly portable to other domains, genres, or language.



