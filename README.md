# Fasta_to_protvec_features

ProtVec is an autoencoder based deep learning model which is similar to Word2vec.
ProtVec is first introduced in this following paper 
 "ProtVec: A Continuous Distributed Representation of Biological Sequences".
 The github page of ProtVec : https://github.com/kyu999/biovec
 
 First, 
 
 pip install biovec
 
 import biovec
 pv = biovec.models.ProtVec("P21397.fasta", corpus_fname="P21397.txt")
 
 This will generate three files .
 1. P21397.fasta.flat
 2. P21397.fasta.gdx
 3. P21397-corpusfile.txt
 
 The pre-trained model "swissprot-reviewed.model" is also available in ProtVec github page.
 Now only P21397.fasta.flat is required to get the features from protein sequences.
 

 
