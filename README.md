# Research-and-development
13-07-2022:
Code in pyToch for age-detection 
________________________________________________


14-07-2022:
learning deep learning, started with basic concepts
started with https://www.youtube.com/playlist?list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi this playlist.
________________________________________________


15-07-2022:
supervised ML(known o/p) -> regression and classification
regression -> when output is continuous
classification -> when output has fixed no of categories 
classification -> binary, multiclass, multilable classification

binary -> 1 o/p with two categories eg, 
            height + weight => gender(o/p) 
              _        _          M
              _        _          F  
              
              so here we can see that there is only one o/p i.e, gender 
              that has two categories.
 
multicalss -> 1 o/p with more than two categories eg,
             height + weight => gender(o/p) 
              _        _          M
              _        _          F  
              _        _          N
              so here we can see that there is only one o/p i.e, gender
              but it has three categories.
              
Multilable -> It has many o/ps eg,
         Movies |  Action    Romance   thriller   suspense  
        Endgame :     1         0         1          1
        So, here we have more than one o/p i.e, more than one o/p categories.


Unsupervised ML(unknown o/p) -> clustering, segmentation, reduce dimension

semi-supervised ML 

Deep learning -> ANN and CNN and  RNN
ANN ->  inputs are in the form of tabular kind of datasets
           features1  |  features2 | ....     o/p
                      |            |
                      |            |
                      
                       
CNN ->  Images, videos 

RNN -> text, time series, sequential data
____________________________________________________

18-07-2022:

ANN
Neural Network ->
forward propagation: 
                        
Activation Functions:

1. Sigmoid: 1/1+(e^-y) 
2. RelU: o/p = max(y,0), 
y -> actuall output 
y'-> o/p from NN.

therefore, loss = (y-y')^2 
So, we need to minimize the loss as much as possible such that accuracy would be maximum
for that we need to update the weights which is done with the help of OPTIMIZER.

new Weight  = old Weight - n*d(loss)/dw           , n = learning rate, that should be very small, n=0.0001

eg,  W2 new = W2 - n*d(loss)/dw2 

Optimizer: Gradient Descent.

_______________________________________________________

19-07-2022:

Chain rule in back propagation
Vanishing Gradient Problem
Exploding Gradient Problem

_______________________________________________________

20-07-2022:

Drop Out 
Regularization
Leaky RelU






















