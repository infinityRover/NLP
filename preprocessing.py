paragraph="Helllo"
import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
ps=PorterStemmer()
wordnet=WordNetLemmatizer()
sentences=nltk.sent_tokenize(paragraph)
corpus=[]
for i in range(len(sentences)):
  review=re.sub('[^a-zA-Z]',' ',sentences[i])
  review=review.lower()
  review=review.split()
  review=[ps.stem(word) for word in review if not word in set(stopword.words('english'))]
  review= ' '.join(review)