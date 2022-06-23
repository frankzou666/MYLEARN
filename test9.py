from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import nltk
import numpy as np
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
from gensim.utils import simple_preprocess
import multiprocessing


def main():
    sentence = """A kite is traditionally a tethered heavier-than-air craft with wing surfaces that react
against the air to create lift and drag. A kite consists of wings, tethers, and anchors.
Kites often have a bridle to guide the face of the kite at the correct angle so the wind
can lift it. A kite’s wing also may be so designed so a bridle is not needed; when
kiting a sailplane for launch, the tether meets the wing at a single point. A kite may
have fixed or moving anchors. Untraditionally in technical kiting, a kite consists of
tether-set-coupled wing sets; even in technical kiting, though, a wing in the system is
still often called the kite.
The lift that sustains the kite in flight is generated when air flows around the kite’s
surface, producing low pressure above and high pressure below the wings. The
interaction with the wind also generates horizontal drag along the direction of the
wind. The resultant force vector from the lift and drag force components is opposed
by the tension of one or more of the lines or tethers to which the kite is attached. The
anchor point of the kite line may be static or moving (such as the towing of a kite by
a running person, boat, free-falling anchors as in paragliders and fugitive parakites
or vehicle).
The same principles of fluid flow apply in liquids and kites are also used under water.
A hybrid tethered craft comprising both a lighter-than-air balloon as well as a kite
lifting surface is called a kytoon."""
    sentences=['The same principles of fluid flow apply ','rce vector from the lift and drag force']
    window=300
    min_word_count=3
    workers = multiprocessing.cpu_count()



    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(sentence.lower())
    nltk.download('stopwords', quiet=True)
    stopwords = nltk.corpus.stopwords.words('english')
    sentens_vocs=[]
    for i,item in enumerate(sentences):
        tagg_doc=TaggedDocument(simple_preprocess(item),[i])
        sentens_vocs.append(tagg_doc)
    model=Doc2Vec(min_count=2,vector_size=100,workers=workers)
    model.build_vocab(sentens_vocs)
    model.train(sentens_vocs,total_examples=model.corpus_count,epochs=10)




if __name__ == '__main__':
    main()