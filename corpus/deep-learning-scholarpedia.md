# Deep Learning - Scholarpedia

[](http://www.scholarpedia.org/article/Deep_Learning)
# Deep Learning

From Scholarpedia

Juergen Schmidhuber (2015), Scholarpedia, 10(11):32832.[doi:10.4249/scholarpedia.32832](http://dx.doi.org/10.4249/scholarpedia.32832)revision #184887 [[link to/cite this article](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&action=cite&rev=184887 "Deep Learning")]

 Jump to: [navigation](http://www.scholarpedia.org/article/Deep_Learning#mw-head), [search](http://www.scholarpedia.org/article/Deep_Learning#p-search)

**Post-publication activity**

Curator:[Juergen Schmidhuber](http://www.scholarpedia.org/article/User:Juergen_Schmidhuber "User:Juergen Schmidhuber")

Contributors:

0.50 - 
[Neil Girdhar](http://www.scholarpedia.org/article/User:Neil_Girdhar "User:Neil Girdhar")

[Risto Miikkulainen](http://www.scholarpedia.org/article/User:Risto_Miikkulainen "User:Risto Miikkulainen")

[Eugene M. Izhikevich](http://www.scholarpedia.org/article/User:Eugene_M._Izhikevich "User:Eugene M. Izhikevich")

*   [Dr. Juergen Schmidhuber, Dalle Molle Institute for Artificial Intelligence, Manno-Lugano, Switzerland](http://www.scholarpedia.org/article/User:Juergen_Schmidhuber "User:Juergen Schmidhuber")

**Deep Learning** has revolutionised Pattern Recognition and Machine Learning. It is about credit assignment in adaptive systems with long chains of potentially causal links between actions and consequences.

The ancient term "Deep Learning" was first introduced to Machine Learning by Dechter (1986), and to Artificial [Neural](http://www.scholarpedia.org/article/Neuron "Neuron") Networks (NNs) by Aizenberg et al (2000). Subsequently it became especially popular in the context of deep NNs, the most successful Deep Learners, which are much older though, dating back half a century. This article will focus on essential developments since the 1960s, addressing supervised, unsupervised, and (briefly) [reinforcement learning](http://www.scholarpedia.org/article/Reinforcement_learning "Reinforcement learning"). There is a recent, more detailed survey with 888 references (Schmidhuber, 2015). LeCun et al (2015) provide a more limited view of more recent Deep Learning history.

A standard NN consists of many simple, connected processors called units, each producing a sequence of real-valued activations. Input units get activated through sensors perceiving the environment, other units through connections with real-valued weights from previously active units. Some units may influence the environment by triggering actions. Learning or credit assignment is about finding weights that make the NN exhibit desired behavior, such as controlling a robot. Depending on the problem and how the units are connected, such behavior may require long causal chains of computational stages, where each stage transforms (often in a non-linear way) the aggregate activation of the network. Deep Learning in NNs is about accurately assigning credit across many such stages.

In a sense, sequence-processing recurrent NNs (RNNs) are the ultimate NNs, because they are general computers (an RNN can emulate the circuits of a microchip). In fully connected RNNs, all units have connections to all non-input units. Unlike feedforward NNs, RNNs can implement while loops, recursion, etc. The program of an RNN is its weight matrix. RNNs can learn programs that mix sequential and parallel information processing in a natural and efficient way.

To measure whether credit assignment in a given NN application is of the deep or shallow type, we consider the length of the corresponding credit assignment paths, which are chains of possibly causal connections between subsequent unit activations, e.g., from input units through hidden units to output units in feedforward NNs (FNNs) without feedback connections, or through transformations over time in RNNs. FNNs with fixed topology have a problem-independent maximal problem depth bounded by the number of layers of units. RNNs, the deepest of all NNs, may learn to solve problems of potentially unlimited depth, for example, by learning to store in their activation-based "short-term [memory](http://www.scholarpedia.org/article/Memory "Memory")" representations of certain important previous observations for arbitrary time intervals.

The difficulty of a problem may have little to do with its depth. Some NNs can quickly learn to solve certain deep but simple problems through random weight guessing (e.g., Hochreiter and Schmidhuber, 1997b). In general, however, finding an NN that precisely models a given training set (of input patterns and corresponding labels) is an NP-complete problem, also in the case of deep NNs (e.g., Sima, 1994).

## First Deep Learners

Certain early NNs (McCulloch and Pitts, 1943) did not learn at all. [Hebb](http://www.scholarpedia.org/article/Donald_Olding_Hebb "Donald Olding Hebb") (1949) published ideas about unsupervised learning. The following decades brought shallow unsupervised NNs and supervised NNs (e.g., Rosenblatt, 1958). Early supervised NNs were essentially variants of linear regressors dating back two centuries (Gauss, Legendre).

Deep Learning networks originated in the 1960s when Ivakhnenko and Lapa (1965) published the first general, working learning [algorithm](http://www.scholarpedia.org/article/Algorithm "Algorithm") for supervised deep feedforward multilayer perceptrons. Their units had polynomial activation functions combining additions and multiplications in Kolmogorov-Gabor polynomials. Ivakhnenko (1971) already described a deep network with 8 layers trained by the "Group Method of Data Handling," still popular in the new millennium. Given a training set of input vectors with corresponding target output vectors, layers are incrementally grown and trained by regression analysis, then pruned with the help of a separate validation set, where regularisation is used to weed out superfluous units. The numbers of layers and units per layer can be learned in problem-dependent fashion.

Like later deep NNs, Ivakhnenko’s nets learned to create hierarchical, distributed, internal representations of incoming data. Many later non-neural methods of Artificial Intelligence and Machine Learning also learn more and more abstract, hierarchical data representations. For example, syntactic pattern recognition methods (Fu, 1977) such as grammar induction discover hierarchies of formal rules to model observations.

## Architectures of Convolutional NNs (CNNs)

The 1970s also saw the birth of the convolutional NN (CNN) architecture (Fukushima’s [Neocognitron](http://www.scholarpedia.org/article/Neocognitron "Neocognitron"), 1979) inspired by neurophysiological insights. Today such architectures are widely used for computer [vision](http://www.scholarpedia.org/article/Vision "Vision"). Here the (typically rectangular) [receptive field](http://www.scholarpedia.org/article/Receptive_field "Receptive field") of a unit with given weight vector (a filter) is shifted step by step across a 2-dimensional array of input values, such as the pixels of an image (usually there are several such filters). The resulting array of subsequent activation events of this unit can then provide inputs to higher-level units, and so on. Due to massive weight replication, relatively few parameters may be necessary to describe the behavior of such convolutional layers, which typically feed downsampling layers consisting of units whose fixed-weight connections originate from physical neighbours in the convolutional layers below. Downsampling units use "Spatial [Averaging](http://www.scholarpedia.org/article/Averaging "Averaging")" to become active if at least one of their inputs is active; their responses are insensitive to certain small image shifts. Weng (1993) later replaced Spatial Averaging by "Max-Pooling" (MP), which is widely used today. Here a 2-dimensional layer or array of unit activations is partitioned into smaller rectangular arrays. Each is replaced in a downsampling layer by the activation of its maximally active unit.

## Backpropagation

Ivakhnenko and Fukushima did not yet use supervised backpropagation (BP) to train the weights of their nets by gradient descent in an objective function, such as the total classification error on a given training set of input patterns and corresponding labels, although BP was also developed back then.

BP’s continuous form was derived in the early 1960s (Kelley, 1960; Bryson, 1961; Bryson and Ho, 1969). Dreyfus (1962) published the elegant derivation of BP based on the chain rule only. BP’s modern efficient version for discrete sparse networks (including FORTRAN code) was published by Linnainmaa (1970). Here the [complexity](http://www.scholarpedia.org/article/Complexity "Complexity") of computing the derivatives of the output error with respect to each weight is proportional to the number of weights. That’s the method still used today. Dreyfus (1973) used BP to change weights of controllers in proportion to such gradients. By 1980, automatic differentiation could derive BP for any differentiable graph (Speelpenning, 1980). Werbos (1982) published the first application of BP to NNs, extending thoughts in his 1974 thesis, which did not yet have Linnainmaa’s modern, efficient form of BP. In 1980-1990, computers became 10,000 times faster per cent than those of 1960-1970, and widely accessible in academic labs. Computational experiments then demonstrated that BP in NNs can indeed yield useful internal representations in hidden layers of NNs (Rumelhart et al., 1986). Wan (1994) produced the first BP-trained NN to win a controlled pattern recognition contest with secret test set. Amari (1998) described BP for natural gradient-based NNs. By 2003, deep BP-based standard FNNs with up to 7 layers were used to successfully classify high-dimensional data (e.g., Vieira and Barradas, 2003).

In the 2000s, computing hardware had again become 10,000 times faster per cent than in the 1980s. Cheap massively parallel Graphics Processing Units (GPUs, originally developed for video games) started to revolutionise NN research. Standard FNNs implemented on GPU were 20 times faster than on CPU (Oh and Jung, 2004). A plain GPU-based FNN trained by BP with pattern distortions (Baird, 1990) set a new record of 0.35% error rate (Ciresan et al., 2010) on the MNIST handwritten digit dataset, which by then had been the perhaps most famous Machine Learning benchmark for decades. This seemed to suggest that advances in exploiting modern computing hardware were more important than advances in algorithms.

## Backpropagation for CNNs

LeCun et al. (1989) first applied BP to Neocognitron-like CNNs, achieving good performance on MNIST. Similar CNNs were used commercially in the 1990s. Ranzato et al. (2007) first applied BP to Max-Pooling CNNs (MPCNNs); advantages of doing this were pointed out subsequently (Scherer et al., 2010).

Efficient parallelized GPU-based MPCNNs (Ciresan et al., 2011a) further improved the MNIST record dramatically, achieving human performance (around 0.2%) for the first time (Ciresan et al., 2012c). To detect human actions in surveillance videos, a 3-dimensional CNN, combined with support vector machines, was part of a larger system using a bag of features approach to extract regions of interest. The system won three 2009 TRECVID competitions. These were possibly the first official international contests won with the help of (MP)CNNs; compare (Ji et al., 2013).

In 2011, an ensemble (Breiman, 1996; Schapire, 1990) of GPU-based MPCNNs also was the first system to achieve superhuman visual pattern recognition in a controlled competition, namely, the IJCNN 2011 traffic sign recognition contest in Silicon Valley (Ciresan et al., 2012c). The system was twice better than humans, and three times better than the nearest nonhuman competitor. Subsequently, similar committees of GPU-MPCNNs became widely used, and also won the 2012 ImageNet classification contest (Krizhevsky et al., 2012), which is popular in the computer vision community. Further progress on ImageNet was achieved through variants of such systems (e.g., Zeiler and Fergus, 2013; Szegedy et al., 2014; Simonyan & Zisserman, 2015).

In 2012, a GPU-MPCNN committee also was the first Deep Learning NN to win a contest on visual object discovery in large images (Ciresan et al., 2013), namely, the ICPR 2012 Contest on Mitosis Detection in Breast Cancer Histological Images. Here deep MPCNNs are trained on labelled patches of big images, then used as feature detectors to be shifted across unknown visual scenes, using various rotations and zoom factors. Image parts that yield highly active output units are likely to contain objects similar to those the NN was trained on. A similar GPU-MPCNN committee was the first Deep Learner to win a pure image segmentation contest (Ciresan et al., 2012a), namely, the ISBI 2012 Segmentation of Neuronal Structures in EM Stacks Challenge. The MPCNN learned to predict for each pixel whether it belongs to the background. Fast MPCNN image scanners avoid redundant computations and speed up naive implementations by up to three orders of magnitude (Masci et al., 2013), extending earlier efficient methods for CNNs without MP (Vaillant et al., 1994).

It is fair to say that deep GPU-CNNs have revolutionised computer vision. For example, GPU-MPCNNs helped to recognise multi-digit numbers in Google Street View images (Goodfellow et al., 2014b), where part of the NN was trained to count visible digits. Other successful recent CNN applications include scene parsing (Farabet et al., 2013), shadow detection (Khan et al., 2014), and video classification (Karpathy et al., 2014), to name a few.

## Fundamental Deep Learning Problem and Unsupervised Pre-Training of RNNs and FNNs

There are extensions of backpropagation (BP) for supervised RNNs (e.g., Williams, 1989; Robinson and Fallside, 1987; Werbos, 1988). During training by "BP through time" (BPTT), the RNN is "unfolded" into an FNN that has essentially as many layers as there are time steps in the observed sequence of input vectors.

The drawbacks of BP and BPTT became obvious in 1991, when the vanishing/exploding gradient problem or "Fundamental Deep Learning Problem" was identified and analysed (Hochreiter, 1991): With standard activation functions, cumulative backpropagated error signals either shrink exponentially in the number of layers (or time steps), or grow out of bounds. The problem is most apparent in RNNs, the deepest of all NNs.

To some extent, Hessian-free [optimization](http://www.scholarpedia.org/article/Optimization "Optimization") can alleviate the problem for FNNs (Moller, 1993; Pearlmutter, 1994) and RNNs (Martens and Sutskever, 2011).

To overcome the vanishing gradient problem, an early generative model was proposed, namely, an unsupervised stack of RNNs called the neural history compressor (Schmidhuber, 1992b). A first RNN uses unsupervised learning to predict its next input. Each higher level RNN tries to learn a compressed representation of the info in the RNN below, trying to minimise the description length (or negative log probability) of the data. The top RNN may then find it easy to classify the data by supervised learning. One can also "distill" the knowledge of a higher RNN (the teacher) into a lower RNN (the student) by forcing the lower RNN to predict the hidden units of the higher one. In the early 1990s, such systems could solve previously unsolvable "Very Deep Learning" tasks involving hundreds of subsequent computational stages.

A conceptually very similar but FNN-based system was the [deep belief network](http://www.scholarpedia.org/article/Deep_Belief_Networks "Deep Belief Networks") (DBN, Hinton and Salakhutdinov, 2006), a stack of restricted [Boltzmann machines](http://www.scholarpedia.org/article/Boltzmann_machine "Boltzmann machine") (RBMs, Smolensky, 1986) with a single layer of feature-detecting units. They can be trained by the contrastive divergence algorithm (Hinton, 2002). At least in theory under certain assumptions, adding more layers improves a bound on the data’s negative log probability (Hinton et al., 2006), equivalent to the data’s description length - just like with the RNN history compressor above. A GPU-DBN implementation (Raina et al., 2009) was orders of magnitudes faster than previous CPU-DBNs; see also (Coates et al., 2013). DBNs achieved good results on phoneme recognition (Mohamed and Hinton, 2010). Autoencoder stacks (Ballard, 1987) became a popular alternative way of pre-training deep FNNs in unsupervised fashion, before fine-tuning them through BP (e.g., Bengio et al., 2007).

Generally speaking, unsupervised learning (UL) can help to encode input data in a form advantageous for further processing. For example, FNNs may profit from pre-training by competitive UL prior to BP-based fine-tuning (Maclin and Shavlik, 1995). Many UL methods generate distributed, [sparse representations](http://www.scholarpedia.org/article/Sparse_representation "Sparse representation") of input patterns. Ideally, given an ensemble of input patterns, redundancy reduction through a deep NN will create a factorial code (a code with statistically independent components) of the ensemble (Barlow et al., 1989). Such codes may be sparse and can be advantageous for (1) data compression, (2) speeding up subsequent BP, (3) trivialising the task of subsequent naive yet optimal Bayes classifiers. Methods for deep UL FNNs include hierarchical [self-organizing](http://www.scholarpedia.org/article/Self-organization "Self-organization")[Kohonen maps](http://www.scholarpedia.org/article/Kohonen_Network "Kohonen Network") (e.g., Koikkalainen and Oja, 1990), hierarchical Gaussian potential function networks (Lee and Kil, 1991), layer-wise UL of feature hierarchies fed into SL classifiers (Behnke, 1999), the Self-Organising Tree Algorithm (Herrero et al., 2001), and nonlinear Autoencoder (AEs) with 5 or more layers (e.g., Kramer, 1991). Predictability Minimization (Schmidhuber, 1992c) searches for factorial codes through nonlinear feature detectors that fight nonlinear predictors, trying to become both as informative and as unpredictable as possible. Hierarchical CNNs in a Neural Abstraction Pyramid (e.g., Behnke, 2003b) can be trained to reconstruct images corrupted by structured noise, thus enforcing increasingly abstract image representations in deeper and deeper layers.

In many applications of the 2000s, however, DBNs and other unsupervised methods were largely replaced by purely supervised FNNs, especially MPCNNs (see above). Here history repeated itself, because already in the 1990s, unsupervised RNN-based history compressors (see above) were largely replaced by purely supervised LSTM RNNs (see below).

## Very Deep Learning in Supervised Sequence-Processing RNNs

Supervised Long Short-Term Memory (LSTM) RNNs have been developed since the 1990s (e.g., Hochreiter and Schmidhuber, 1997b; Gers and Schmidhuber, 2001; Graves et al., 2009). Parts of LSTM RNNs are designed such that backpropagated errors can neither vanish nor explode, but flow backwards in "civilized" fashion for thousands or even more steps. Thus LSTM variants could learn previously unlearnable Very Deep Learning tasks (including some unlearnable by the 1992 history compressor above) that require to discover the importance of (and memorize) events that happened thousands of discrete time steps ago, while previous standard RNNs already failed in case of minimal time lags of 10 steps. It is possible to evolve good problem-specific LSTM-like topologies (Bayer et al., 2009).

Recursive NNs (Goller and Küchler, 1996) generalize RNNs, by operating on hierarchical structures, recursively combining child representations into parent representations. Bi-directional RNNs (BRNNs) (Schuster and Paliwal, 1997) are designed for input sequences whose starts and ends are known in advance, such as spoken sentences to be labeled by their phonemes. DAG-RNNs (Baldi and Pollastri, 2003) generalize BRNNs to multiple dimensions. Recursive NNs, BRNNs and DAG-RNNs unfold their full potential when combined with LSTM (Graves et al., 2009).

Particularly successful in competitions were stacks of LSTM RNNs (Fernandez et al., 2007) trained by Connectionist Temporal Classification (CTC, Graves et al., 2006), a gradient-based method for finding RNN weights that maximize the probability of teacher-given label sequences, given (typically much longer and more high-dimensional) streams of real-valued input vectors. CTC performs simultaneous segmentation (alignment) and recognition. In 2009, CTC-trained LSTM became the first RNN to win controlled international contests, namely, 3 competitions in connected handwriting recognition. Hannun et al (2014) used CTC-trained RNNs to break a famous speech recognition benchmark record, without using any traditional speech processing methods such as Hidden Markov Models (HMMs) or Gaussian Mixture Models.

Unlike HMMs and previous RNNs, LSTM can learn to recognise context-sensitive [languages](http://www.scholarpedia.org/article/Language "Language"). By 2007, LSTM had started to revolutionise speech recognition, outperforming traditional HMMs in keyword spotting tasks (Fernandez et al., 2007). By 2013, LSTM achieved best known results on the famous TIMIT phoneme recognition benchmark (Graves et al., 2013). Hybrids of traditional methods and LSTM RNNs obtained best known performance on large-vocabulary speech recognition (Sak et al., Google, 2014a; Li & Wu, 2015a). LSTM also helped to improve the state of the art in numerous other fields, including image caption generation (in conjunction with CNNs) (Vinyals et al., Google, 2014), machine translation (Sutskever et al., Google, 2014), text-to-speech synthesis (Fan et al., 2015; Zen & Sak, 2015, now available for Google Android), photo-real talking heads (Fan et al., Microsoft, 2015), syntactic parsing for natural language processing (Vinyals et al., Google, 2014b), and many other applications. In 2015, CTC-trained LSTM dramatically improved Google Voice (by 49%), and is now available to a billion smartphone users (Sak et al, 2015).

Gradient-based LSTM is no panacea though. Other methods sometimes outperformed LSTM at least on certain tasks (e.g., Jaeger, 2004; Schmidhuber et al., 2007; Martens and Sutskever, 2011; Zimmermann et al., 2012; Pascanu et al., 2013b; Koutnik et al., 2014). Several alternative RNN-related methods with fast memory control have been proposed over the decades (e.g., AMAmemory 2015).

## Some Tricks to Improve NNs

BP-like methods can be used to search for "simple," low-complexity NNs with high generalization capability. For example, weight decay (e.g., Hanson and Pratt, 1989) encourages near-zero weights, by penalizing large weights. Related weight priors are implicit in additional penalty terms (MacKay, 1992) or in methods based on validation sets (e.g., Hastie and Tibshirani, 1990). Similar priors (or biases towards simplicity) are implicit in constructive and pruning algorithms, e.g., layer-by-layer sequential network construction (e.g., Ivakhnenko, 1971), input pruning (Moody, 1992), unit pruning (e.g., Ivakhnenko, 1971; Mozer and Smolensky, 1989), weight pruning (e.g., LeCun et al., 1990b), fast and short weight matrix-computing programs (Schmidhuber, 1997), and Flat Minimum Search (FMS, Hochreiter and Schmidhuber, 1999). DBN training can be improved (Cho et al., 2012) through Tikhonov-type regularization (Tikhonov et al., 1977). See also sparsity-enforcing methods mentioned earlier.

Dropout (Hinton et al., 2012b) removes units from NNs during training to improve generalisation. It is closely related to older, biologically plausible techniques for adding noise to neurons or synapses during training (e.g., Hanson, 1990). NNs with competing units (e.g., Schmidhuber, 1989b; Maass, 2000; Goodfellow et al., 2013) tend to outperform those with non-competing units, and avoid catastrophic forgetting through BP when training sets change over time (Srivastava et al., 2013).

The popular activation function f of Rectified Linear Units (ReLUs) is f(x) = x for x > 0; f(x) = 0 otherwise. ReLU NNs are useful for RBMs (Nair and Hinton, 2010; Maas et al., 2013), outperformed sigmoidal activation functions in deep NNs (Glorot et al., 2011), and helped to obtain best results on several benchmark problems across multiple domains (e.g., Krizhevsky et al., 2012).

Many additional tricks for improving NNs have been described (e.g., Montavon et al., 2012; Schmidhuber, 2015).

## Consequences for [Neuroscience](http://www.scholarpedia.org/article/Neuroscience "Neuroscience")

Artificial NNs (ANNs) can help to better understand biological NNs (BNNs). The feature detectors learned by single-layer visual ANNs are similar to those found in early visual processing stages of BNNs. Likewise, the feature detectors learned in deep layers of visual ANNs should be highly predictive of what neuroscientists will find in deep layers of BNNs. While the visual cortex of BNNs may use quite different learning algorithms, its objective function to be minimized may be rather similar to the one of visual ANNs. In fact, results obtained with relatively deep artificial NNs (e.g., Yamins et al., 2013) seem compatible with insights about the visual pathway in the primate cerebral cortex, which has been studied for many decades.

## Deep Learning with Spiking Neurons?

Current deep NNs greatly profit from GPUs, which are little ovens, much hungrier for energy than biological [brains](http://www.scholarpedia.org/article/Brain "Brain"), whose neurons efficiently communicate by brief spikes (e.g., Hodgkin and Huxley, 1952), and often remain quiet. Many computational models of such spiking neurons have been proposed and analyzed (e.g., Gerstner and Kistler, 2002). Future energy-efficient hardware for DL in NNs may implement aspects of such models - see numerous references in the survey (Schmidhuber, 2015, Sec. 5.26). In practical applications, however, current artificial networks of spiking neurons cannot yet compete with the best traditional deep NNs.

## Deep Reinforcement Learning (RL)

Reinforcement Learning (RL) is the most general type of learning. General RL agents must discover, without the aid of a teacher, how to interact with a dynamic, initially unknown, partially observable environment in order to maximize their expected cumulative [reward signals](http://www.scholarpedia.org/article/Reward_signals "Reward signals") (e.g., Kaelbling et al., 1996; Sutton and Barto, 1998; Wiering and van Otterlo, 2012). There may be arbitrary, a priori unknown delays between actions and perceivable consequences. The RL problem is as hard as any problem of computer science, since any task with a computable description can be formulated in the general RL framework (e.g., Hutter, 2005). Deep FNNs and RNNs are useful tools for various types of RL. Many references on this since the 1980s can be found in the recent survey (Schmidhuber, 2015, Sec. 6).

## Outlook

Deep Learning in NNs is more than a temporary fad. Physics seems to dictate that any future efficient computational hardware will have to be brain-like, with many compactly placed processors in 3-dimensional space, sparsely connected by many short and few long wires, to minimize total connection cost (even if the "wires" are actually light beams). The basic architecture is essentially the one of a deep, sparsely connected, 3-dimensional RNN, and Deep Learning methods for such RNNs are expected to become even much more important than they are today.

The contents of this article may be used for educational and non-commercial purposes, including articles for Wikipedia and similar sites.

## References

I. Aizenberg, N.N. Aizenberg, and J. P.L. Vandewalle (2000). Multi-Valued and Universal Binary Neurons: Theory, Learning and Applications. Springer Science & Business Media. First work to introduce the term "Deep Learning" to Neural Networks; compare a popular [G+ post on this](https://plus.google.com/100849856540000067209/posts/7N6z251w2Wd?pid=6127540521703625346&oid=100849856540000067209).

AMAmemory (2015): [Answer at reddit AMA (Ask Me Anything) on "memory networks" etc (with references)](http://www.reddit.com/r/MachineLearning/comments/2xcyrl/i_am_j%C3%BCrgen_schmidhuber_ama/cp0q12t)

Amari, S.-I. (1998). Natural gradient works efficiently in learning. Neural Computation, 10(2):251– 276.

Baird, H. (1990). Document image defect models. In Proc. IAPR Workshop on Syntactic and [Structural Pattern Recognition](http://www.scholarpedia.org/article/Structural_Pattern_Recognition "Structural Pattern Recognition"), Murray Hill, NJ.

Baldi, P. and Pollastri, G. (2003). The principled design of large-scale recursive neural network architectures – DAG-RNNs and the protein structure prediction problem. J. Mach. Learn. Res., 4:575–602.

Ballard, D. H. (1987). Modular learning in neural networks. Proc. AAAI, pp. 279–284.

Barlow, H. B., Kaushal, T. P., and Mitchison, G. J. (1989). Finding minimum [entropy](http://www.scholarpedia.org/article/Entropy "Entropy") codes. Neural Computation, 1(3):412–423.

Bayer, J., Wierstra, D., Togelius, J., and Schmidhuber, J. (2009). Evolving memory cell structures for [sequence learning](http://www.scholarpedia.org/article/Sequence_learning "Sequence learning"). Proc. ICANN (2), pp. 755–764.

Behnke, S. (1999). Hebbian learning and competition in the neural abstraction pyramid. Proc. IJCNN, vol 2, pp. 1356–1361.

Behnke, S. (2003b). Hierarchical Neural Networks for Image Interpretation, vol LNCS 2766 of Lecture Notes in Computer Science, Springer.

Bengio, Y., Lamblin, P., Popovici, D., and Larochelle, H. (2007). Greedy layer-wise training of deep networks. In Cowan, J. D., Tesauro, G., and Alspector, J., editors, Proc. NIPS 19, pp. 153–160. MIT Press.

Bryson, A. E. (1961). A gradient method for optimizing multi-stage allocation processes. In Proc. Harvard Univ. Symposium on digital computers and their applications.

Bryson, A. and Ho, Y. (1969). Applied [optimal control](http://www.scholarpedia.org/article/Optimal_control "Optimal control"): optimization, estimation, and control. Blaisdell Pub. Co.

Cho, K., Ilin, A., and Raiko, T. (2012). Tikhonov-type regularization for restricted Boltzmann machines. Proc. ICANN 2012, pp. 81–88. Springer.

Ciresan, D. C., Giusti, A., Gambardella, L. M., and Schmidhuber, J. (2012a). Deep neural networks segment neuronal membranes in electron microscopy images. Proc. NIPS, pp. 2852–2860.

Ciresan, D. C., Giusti, A., Gambardella, L. M., and Schmidhuber, J. (2013). Mitosis detection in breast cancer histology images with deep neural networks. Proc. MICCAI, vol 2, pp. 411–418.

Ciresan, D. C., Meier, U., Gambardella, L. M., and Schmidhuber, J. (2010). Deep big simple neural nets for handwritten digit recognition. Neural Computation, 22(12):3207–3220.

Ciresan, D. C., Meier, U., Masci, J., Gambardella, L. M., and Schmidhuber, J. (2011a). Flexible, high performance convolutional neural networks for image classification. Proc. IJCAI, pp. 1237–1242.

Ciresan, D. C., Meier, U., Masci, J., and Schmidhuber, J. (2012b). Multi-column deep neural network for traffic sign classification. Neural Networks, 32:333–338.

Ciresan, D. C., Meier, U., and Schmidhuber, J. (2012c). Multi-column deep neural networks for image classification. Proc. CVPR 2012. Long preprint arXiv:1202.2745v1 [cs.CV].

Coates, A., Huval, B., Wang, T., Wu, D. J., Ng, A. Y., and Catanzaro, B. (2013). Deep learning with COTS HPC systems. Proc. ICML’13.

R. Dechter (1986). Learning while searching in constraint-satisfaction problems. University of California, Computer Science Department, Cognitive Systems Laboratory. First paper to introduce the term "Deep Learning" to Machine Learning; compare a popular [G+ post on this](https://plus.google.com/100849856540000067209/posts/7N6z251w2Wd?pid=6127540521703625346&oid=100849856540000067209).

Dreyfus, S. E. (1962). The numerical solution of variational problems. Journal of Mathematical Analysis and Applications, 5(1):30–45.

Dreyfus, S. E. (1973). The computational solution of optimal control problems with time lag. IEEE Transactions on Automatic Control, 18(4):383–385.

Fan, B.; Wang, L.; Soong, F. K.; Xie, L. (2015). Photo-Real Talking Head with Deep Bidirectional LSTM. Proc. ICASSP 2015.

Farabet, C., Couprie, C., Najman, L., and LeCun, Y. (2013). Learning hierarchical features for scene labeling. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8):1915–1929.

Fernandez, S., Graves, A., and Schmidhuber, J. (2007). An application of [recurrent neural networks](http://www.scholarpedia.org/article/Recurrent_neural_networks "Recurrent neural networks") to discriminative keyword spotting. Proc. ICANN (2), pp. 220–229.

Fernandez, S., Graves, A., and Schmidhuber, J. (2007). Sequence labelling in structured domains with hierarchical recurrent neural networks. Proc. IJCAI.

Fu, K. S. (1977). Syntactic Pattern Recognition and Applications. Berlin, Springer.

Fukushima, K. (1979). Neural network model for a mechanism of pattern recognition unaffected by shift in position - Neocognitron. Trans. IECE, J62-A(10):658–665.

Gers, F. A. and Schmidhuber, J. (2001). LSTM recurrent networks learn simple context free and context sensitive languages. IEEE Transactions on Neural Networks, 12(6):1333–1340.

Gerstner, W. and Kistler, W. K. (2002). Spiking Neuron Models. Cambridge University Press.

Glorot, X., Bordes, A., and Bengio, Y. (2011). Deep sparse rectifier networks. Proc. AISTATS, vol 15, pp. 315–323.

Goodfellow, I. J., Warde-Farley, D., Mirza, M., Courville, A., and Bengio, Y. (2013). Maxout networks. Proc. ICML.

Goodfellow, I. J., Bulatov, Y., Ibarz, J., Arnoud, S., and Shet, V. (2014b). Multi-digit number recognition from street view imagery using deep convolutional neural networks. arXiv preprint arXiv:1312.6082 v4.

Goller, C.; Küchler, A. (1996). Learning task-dependent distributed representations by backpropagation through structure. IEEE International Conference on Neural Networks, 1996, vol. 1, pp. 347-352.

Graves, A., Fernandez, S., Gomez, F. J., and Schmidhuber, J. (2006). Connectionist temporal classification: Labelling unsegmented sequence data with recurrent neural nets. Proc. ICML’06, pp. 369–376.

Graves, A., Liwicki, M., Fernandez, S., Bertolami, R., Bunke, H., and Schmidhuber, J. (2009). A novel connectionist system for improved unconstrained handwriting recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, 31(5).

Graves, A., Mohamed, A.-R., and Hinton, G. E. (2013). Speech recognition with deep recurrent neural networks. Proc. ICASSP, pp. 6645–6649.

Hannun, A.; Case, C; Casper, J.; Catanzaro, B.; Diamos, G.; Elsen, E.; Prenger, R.; Satheesh, S.; Sengupta, S.; Coates, A.; Ng, A. Y. (2014). Deep Speech: Scaling up end-to-end speech recognition. arXiv preprint [http://arxiv.org/abs/1412.5567](http://arxiv.org/abs/1412.5567)

Hanson, S. J. and Pratt, L. Y. (1989). Comparing biases for minimal network construction with back-propagation. In Touretzky, D. S., editor, Proc. NIPS, 1, pp. 177–185. San Mateo, CA: Morgan Kaufmann.

Hanson, S. J. (1990). A stochastic version of the delta rule. Physica D: Nonlinear Phenomena, 42(1):265–272.

Hastie, T. J. and Tibshirani, R. J. (1990). Generalized additive models. Monographs on Statisics and Applied Probability, 43.

Hebb, D. O. (1949). The Organization of Behavior. Wiley, New York.

Herrero, J., Valencia, A., and Dopazo, J. (2001). A hierarchical unsupervised growing neural network for clustering gene expression patterns. Bioinformatics, 17(2):126–136.

Hinton, G. and Salakhutdinov, R. (2006). Reducing the dimensionality of data with neural networks. Science, 313(5786):504–507.

Hinton, G. E. (2002). Training products of experts by minimizing contrastive divergence. Neural Computation, 14(8):1771–1800.

Hinton, G. E., Osindero, S., and Teh, Y.-W. (2006). A fast learning algorithm for deep belief nets. Neural Computation, 18(7):1527–1554.

Hinton, G. E., Srivastava, N., Krizhevsky, A., Sutskever, I., and Salakhutdinov, R. R. (2012b). Improving neural networks by preventing co-adaptation of feature detectors. Technical Report arXiv:1207.0580.

Hochreiter, S. (1991). Untersuchungen zu dynamischen neuronalen Netzen. Diploma thesis, Institut fuer Informatik, Lehrstuhl Prof. Brauer, Tech. Univ. Munich. Advisor: J. Schmidhuber.

Hochreiter, S. and Schmidhuber, J. (1997a). Flat minima. Neural Computation, 9(1):1–42.

Hochreiter, S. and Schmidhuber, J. (1997b). Long Short-Term Memory. Neural Computation, 9(8):1735–1780. Based on TR FKI-207-95, TUM (1995).

Hodgkin, A. L. and Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. The Journal of Physiology, 117(4):500.

Hutter, M. (2005). Universal Artificial Intelligence: Sequential Decisions based on [Algorithmic Probability](http://www.scholarpedia.org/article/Algorithmic_Probability "Algorithmic Probability"). Springer, Berlin.

Ivakhnenko, A. G. and Lapa, V. G. (1965). Cybernetic Predicting Devices. CCM Information Corporation.

Ivakhnenko, A. G. (1971). Polynomial theory of [complex systems](http://www.scholarpedia.org/article/Complex_systems "Complex systems"). IEEE Transactions on Systems, Man and Cybernetics, (4):364–378.

Jaeger, H. (2004). Harnessing nonlinearity: Predicting chaotic systems and saving energy in wireless communication. Science, 304:78–80.

Ji, S., Xu, W., Yang, M., and Yu, K. (2013). 3D convolutional neural networks for human action recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(1):221–231.

Kaelbling, L. P., Littman, M. L., and Moore, A.W. (1996). Reinforcement learning: a survey. Journal of AI research, 4:237–285.

Karpathy, A., Toderici, G., Shetty, S., Leung, T., Sukthankar, R., and Fei-Fei, L. (2014). Large-scale video classification with convolutional neural networks. Proc. CVPR.

Kelley, H. J. (1960). Gradient theory of optimal flight paths. ARS Journal, 30(10):947–954.

Khan, S. H., Bennamoun, M., Sohel, F., and Togneri, R. (2014). Automatic feature learning for robust shadow detection. Proc. CVPR.

Koikkalainen, P. and Oja, E. (1990). Self-organizing hierarchical feature maps. Proc. IJCNN, pp. 279–284.

Koutnik, J., Greff, K., Gomez, F., and Schmidhuber, J. (2014). A Clockwork RNN. Proc. ICML, vol 32, pp. 1845–1853. arXiv:1402.3511 [cs.NE].

Kramer, M. (1991). Nonlinear principal component analysis using autoassociative neural networks. AIChE Journal, 37:233–243.

Krizhevsky, A., Sutskever, I., and Hinton, G. E. (2012). Imagenet classification with deep convolutional neural networks. Proc. NIPS, page 4.

LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W., and Jackel, L. D. (1989). Back-propagation applied to handwritten zip code recognition. Neural Computation, 1(4):541–551.

LeCun, Y., Denker, J. S., and Solla, S. A. (1990b). Optimal brain damage. In Touretzky, D. S., Proc. NIPS 2, pp. 598–605. Morgan Kaufmann.

LeCun, Y., Bengio, Y., Hinton, G. (2015). Deep Learning. Nature 521, 436-444. [Link.](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html) See [critique by J. Schmidhuber (2015)](http://people.idsia.ch/~juergen/deep-learning-conspiracy.html)

Lee, S. and Kil, R. M. (1991). A Gaussian potential function network with hierarchically selforganizing learning. Neural Networks, 4(2):207–224.

Li, X.; Wu, X (2015). Constructing Long Short-Term Memory based Deep Recurrent Neural Networks for Large Vocabulary Speech Recognition. Proc. ICASSP 2015. [http://arxiv.org/abs/1410.4281](http://arxiv.org/abs/1410.4281)

Linnainmaa, S. (1970). The representation of the cumulative rounding error of an algorithm as a Taylor expansion of the local rounding errors. Master’s thesis, Univ. Helsinki.

Linnainmaa, S. (1976). Taylor expansion of the accumulated rounding error. BIT Numerical Mathematics, 16(2):146–160.

Maas, A. L., Hannun, A. Y., and Ng, A. Y. (2013). Rectifier nonlinearities improve neural network acoustic models. Proc. ICML.

Maass, W. (2000). On the computational power of winner-take-all. Neural Computation, 12:2519–2535.

MacKay, D. J. C. (1992). A practical [Bayesian](http://www.scholarpedia.org/article/Bayesian_statistics "Bayesian statistics") framework for backprop networks. Neural Computation, 4:448–472.

Maclin, R. and Shavlik, J. W. (1995). Combining the predictions of multiple classifiers: Using competitive learning to initialize neural networks. Proc. IJCAI, pp. 524–531.

Martens, J. and Sutskever, I. (2011). Learning recurrent neural networks with Hessian-free optimization. Proc. ICML, pp. 1033–1040.

Masci, J., Giusti, A., Ciresan, D. C., Fricout, G., and Schmidhuber, J. (2013). A fast learning algorithm for image segmentation with max-pooling convolutional networks. Proc. ICIP13, pp. 2713–2717.

McCulloch, W. and Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. Bulletin of Mathematical Biophysics, 7:115–133.

Mohamed, A. and Hinton, G. E. (2010). Phone recognition using restricted Boltzmann machines. Proc. ICASSP, pp. 4354–4357.

Moller, M. F. (1993). Exact calculation of the product of the Hessian matrix of feed-forward network error functions and a vector in O(N) time. Technical Report PB-432, Computer Science Department, Aarhus University, Denmark.

Montavon, G., Orr, G., and Mueller, K. (2012). Neural Networks: Tricks of the Trade. Number LNCS 7700 of Lecture Notes in Computer Science. Springer Verlag.

Moody, J. E. (1992). The effective number of parameters: An analysis of generalization and regularization in nonlinear learning systems. Proc. NIPS’4, pp. 847–854. Morgan Kaufmann.

Mozer, M. C. and Smolensky, P. (1989). Skeletonization: A technique for trimming the fat from a network via relevance assessment. In Proc. NIPS 1, pp. 107–115. Morgan Kaufmann.

Nair, V. and Hinton, G. E. (2010). Rectified linear units improve restricted Boltzmann machines. Proc. ICML.

Oh, K.-S. and Jung, K. (2004). GPU implementation of neural networks. Pattern Recognition, 37(6):1311–1314.

Pascanu, R., Mikolov, T., and Bengio, Y. (2013b). On the difficulty of training recurrent neural networks. In ICML’13: JMLR: W&CP vol 28.

Pearlmutter, B. A. (1994). Fast exact multiplication by the Hessian. Neural Computation, 6(1):147–160.

Raina, R., Madhavan, A., and Ng, A. (2009). Large-scale deep unsupervised learning using graphics processors. Proc. ICML, pp. 873–880.

Ranzato, M. A., Huang, F., Boureau, Y., and LeCun, Y. (2007). Unsupervised learning of invariant feature hierarchies with applications to object recognition. Proc. CVPR, pp. 1–8.

Robinson, A. J. and Fallside, F. (1987). The utility driven dynamic error propagation network. Technical Report CUED/F-INFENG/TR.1, Cambridge University Engineering Department.

Rosenblatt, F. (1958). The perceptron: a probabilistic model for information storage and organization in the brain. Psychological Review, 65(6):386.

Rumelhart, D. E., Hinton, G. E., and Williams, R. J. (1986). Learning internal representations by error propagation. In Rumelhart, D. E. and McClelland, J. L., editors, Parallel Distributed Processing, volume 1, pp. 318–362. MIT Press.

Sak, H., Senior, A., Rao, K., Beaufays, F., Schalkwyk, J. (2015): [Google Research Blog](http://googleresearch.blogspot.ch/2015/09/google-voice-search-faster-and-more.html)

Scherer, D., Mueller, A., and Behnke, S. (2010). Evaluation of pooling operations in convolutional architectures for object recognition. Proc. ICANN, pp. 92–101.

Schmidhuber, J. (1989b). A local learning algorithm for dynamic feedforward and recurrent networks. Connection Science, 1(4):403–412.

Schmidhuber, J. (1992b). Learning complex, extended sequences using the principle of history compression. Neural Computation, 4(2):234–242. Based on TR FKI-148-91, TUM, 1991.

Schmidhuber, J. (1992c). Learning factorial codes by predictability minimization. Neural Computation, 4(6):863–879.

Schmidhuber, J. (1997). Discovering neural nets with low [Kolmogorov complexity](http://www.scholarpedia.org/article/Algorithmic_information_theory "Algorithmic information theory") and high generalization capability. Neural Networks, 10(5):857–873.

Schmidhuber, J., Wierstra, D., Gagliolo, M., and Gomez, F. J. (2007). Training recurrent networks by Evolino. Neural Computation, 19(3):757–779.

Schmidhuber, J. (2015). Deep learning in neural networks: An overview. Neural Networks, 61, 85-117. [arXiv preprint 1404.7828](http://arxiv.org/abs/1404.7828)

Schuster, M. and Paliwal, K. K. (1997). Bidirectional recurrent neural networks. IEEE Transactions on Signal Processing, 45:2673–2681.

Sima, J. (1994). Loading deep networks is hard. Neural Computation, 6(5):842–850.

Simonyan, K., and Zisserman, A. (2015). Very Deep Convolutional Networks for Large-Scale Image Recognition. arXiv preprint [http://arxiv.org/abs/1409.1556](http://arxiv.org/abs/1409.1556)

Smolensky, P. (1986). Parallel distributed processing: Explorations in the microstructure of cognition, vol. 1. chapter Information Processing in [Dynamical Systems](http://www.scholarpedia.org/article/Dynamical_Systems "Dynamical Systems"): Foundations of Harmony Theory, pp. 194–281. MIT Press.

Speelpenning, B. (1980). Compiling Fast Partial Derivatives of Functions Given by Algorithms. PhD thesis, Department of Computer Science, University of Illinois, Urbana-Champaign.

Srivastava, R. K., Masci, J., Kazerounian, S., Gomez, F., and Schmidhuber, J. (2013). Compete to compute. Proc. NIPS, pp. 2310–2318.

Sutskever, I., Vinyals, O., and Le, Q. V. (2014). Sequence to sequence learning with neural networks. Proc. NIPS’2014. arXiv preprint arXiv:1409.3215 [cs.CL].

Sutton, R. and Barto, A. (1998). Reinforcement learning: An introduction. Cambridge, MA, MIT Press.

Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Vanhoucke, V., and Rabinovich, A. (2014). Going deeper with convolutions. arXiv preprint arXiv:1409.4842 [cs.CV].

Tikhonov, A. N., Arsenin, V. I., and John, F. (1977). Solutions of ill-posed problems. Winston.

Vaillant, R., Monrocq, C., and LeCun, Y. (1994). Original approach for the localisation of objects in images. IEE Proc. on Vision, Image, and Signal Processing, 141(4):245–250.

Vieira, A. and Barradas, N. (2003). A training algorithm for classification of high-dimensional data. Neurocomputing, 50:461–472.

Vinyals, O.; Toshev, A.; Bengio, S.; Erhan, D. (2014). Show and Tell: A Neural Image Caption Generator. arXiv Preprint [http://arxiv.org/pdf/1411.4555v1.pdf](http://arxiv.org/pdf/1411.4555v1.pdf)

Vinyals, O.; Kaiser, L.; Koo, T.; Petrov, S.; Sutskever, I.; Hinton, G. (2014b). Grammar as a Foreign Language. Preprint [http://arxiv.org/abs/1412.7449](http://arxiv.org/abs/1412.7449)

Wan, E. A. (1994). Time series prediction by using a connectionist network with internal delay lines. In Weigend, A. S. and Gershenfeld, N. A., editors, Time series prediction: Forecasting the future and understanding the past, pp. 265–295. Addison-Wesley.

Williams, R. J. (1989). Complexity of exact gradient computation algorithms for recurrent neural networks. Technical Report Technical Report NU-CCS-89-27, Boston: Northeastern University, College of Computer Science.

Wiering, M. and van Otterlo, M. (2012). Reinforcement Learning. Springer.

Weng, J., Ahuja, N., and Huang, T. S. (1993). Learning recognition and segmentation of 3-D objects from 2-D images. Proc. 4th Intl. Conf. Computer Vision, Berlin, Germany, pp. 121-128.

Werbos, P. J. (1974). Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences. PhD thesis, Harvard University.

Werbos, P. J. (1982). Applications of advances in nonlinear sensitivity analysis. In Proceedings of the 10th IFIP Conference, 31.8 - 4.9, NYC, pp. 762–770.

Werbos, P. J. (1988). Generalization of backpropagation with application to a recurrent gas market model. Neural Networks, 1.

Yamins, D., Hong, H., Cadieu, C., and DiCarlo, J. J. (2013). Hierarchical modular optimization of convolutional networks achieves representations similar to macaque IT and human [ventral stream](http://www.scholarpedia.org/article/What_And_Where_Pathways "What And Where Pathways"). Proc. NIPS, pp. 1–9.

Zeiler, M. D. and Fergus, R. (2013). Visualizing and understanding convolutional networks. Technical Report arXiv:1311.2901 [cs.CV], NYU.

Zen, H. and Sak, H. (2015). Unidirectional Long Short-Term Memory Recurrent Neural Network with Recurrent Output Layer for Low-Latency Speech Synthesis. Proc. ICASSP, pp. 4470-4474

Zimmermann, H.-G., Tietz, C., and Grothmann, R. (2012). Forecasting with recurrent neural networks: 12 tricks. In Montavon, G., Orr, G. B., and Mueller, K.-R., editors, Neural Networks: Tricks of the Trade (2nd ed.), vol 7700 of Lecture Notes in Computer Science, pp. 687–707. Springer.

## External links

[Who Invented Backpropagation?](http://people.idsia.ch/~juergen/who-invented-backpropagation.html)

[J. Schmidhuber's Deep Learning website](http://people.idsia.ch/~juergen/deeplearning.html)

Sponsored by: [Prof. Risto Miikkulainen, The University of Texas at Austin, Austin, TX, USA](http://www.scholarpedia.org/article/User:Risto_Miikkulainen "User:Risto Miikkulainen")
[Reviewed by](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=152220): [Eugene M. Izhikevich, Editor-in-Chief of Scholarpedia, the peer-reviewed open-access encyclopedia](http://www.scholarpedia.org/article/User:Eugene_M._Izhikevich "User:Eugene M. Izhikevich")
[Reviewed by](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=0): [Prof. Risto Miikkulainen, The University of Texas at Austin, Austin, TX, USA](http://www.scholarpedia.org/article/User:Risto_Miikkulainen "User:Risto Miikkulainen")
Accepted on: [2015-11-27 14:37:33 GMT](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=152272)

 Retrieved from "[http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=184887](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=184887)" 

*   [Log in](http://www.scholarpedia.org/w/index.php?title=Special:UserLogin&returnto=Deep+Learning "You are encouraged to log in; however, it is not mandatory [o]")

##### Namespaces

*   [Page](http://www.scholarpedia.org/article/Deep_Learning "View the content page [c]")
*   [Discussion](http://www.scholarpedia.org/w/index.php?title=Talk:Deep_Learning&action=edit&redlink=1 "Discussion about the content page [t]")

##### Variants[](http://www.scholarpedia.org/article/Deep_Learning#)

##### Views

*   [Read](http://www.scholarpedia.org/article/Deep_Learning)
*   [View source](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&action=edit "This page is protected.
You can view its source [e]")
*   [View history](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&action=history "Past revisions of this page [h]")

##### Actions[](http://www.scholarpedia.org/article/Deep_Learning#)

##### Search

[](http://www.scholarpedia.org/article/Main_Page "Visit the main page")

##### Navigation

*   [Main page](http://www.scholarpedia.org/article/Main_Page "Visit the main page [z]")
*   [About](http://www.scholarpedia.org/article/Scholarpedia:About)
*   [Propose a new article](http://www.scholarpedia.org/article/Special:ProposeArticle)
*   [Instructions for Authors](http://www.scholarpedia.org/article/Scholarpedia:Instructions_for_Authors)
*   [Random article](http://www.scholarpedia.org/article/Special:Random "Load a random page [x]")
*   [FAQs](http://www.scholarpedia.org/article/Help:Frequently_Asked_Questions)
*   [Help](http://www.scholarpedia.org/article/Scholarpedia:Help)

##### Focal areas

*   [Astrophysics](http://www.scholarpedia.org/article/Encyclopedia:Astrophysics)
*   [Celestial mechanics](http://www.scholarpedia.org/article/Encyclopedia:Celestial_Mechanics)
*   [Computational neuroscience](http://www.scholarpedia.org/article/Encyclopedia:Computational_neuroscience)
*   [Computational intelligence](http://www.scholarpedia.org/article/Encyclopedia:Computational_intelligence)
*   [Dynamical systems](http://www.scholarpedia.org/article/Encyclopedia:Dynamical_systems)
*   [Physics](http://www.scholarpedia.org/article/Encyclopedia:Physics)
*   [Touch](http://www.scholarpedia.org/article/Encyclopedia:Touch)
*   [More topics](http://www.scholarpedia.org/article/Scholarpedia:Topics)

##### Activity

*   [Recently published articles](http://www.scholarpedia.org/article/Special:RecentlyPublished)
*   [Recently sponsored articles](http://www.scholarpedia.org/article/Special:RecentlySponsored)
*   [Recent changes](http://www.scholarpedia.org/article/Special:RecentChanges "A list of recent changes in the wiki [r]")
*   [All articles](http://www.scholarpedia.org/article/Special:AllPages)
*   [List all Curators](http://www.scholarpedia.org/article/Special:ListCurators)
*   [List all users](http://www.scholarpedia.org/article/Special:ListUsers)
*   [Scholarpedia Journal](http://www.scholarpedia.org/article/Special:Journal)

##### Tools

*   [What links here](http://www.scholarpedia.org/article/Special:WhatLinksHere/Deep_Learning "A list of all wiki pages that link here [j]")
*   [Related changes](http://www.scholarpedia.org/article/Special:RecentChangesLinked/Deep_Learning "Recent changes in pages linked from this page [k]")
*   [Special pages](http://www.scholarpedia.org/article/Special:SpecialPages "A list of all special pages [q]")
*   [Printable version](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&printable=yes)
*   [Permanent link](http://www.scholarpedia.org/w/index.php?title=Deep_Learning&oldid=184887 "Permanent link to this revision of the page")

*   [](https://twitter.com/scholarpedia)
*   [](https://plus.google.com/112873162496270574424)
*   [](http://www.facebook.com/Scholarpedia)
*   [](http://www.linkedin.com/groups/Scholarpedia-4647975/about)

*    This page was last modified on 2 December 2017, at 00:40.
*   This page has been accessed 161,729 times.
*   "Deep Learning" by [Juergen Schmidhuber](http://www.scholarpedia.org/article/Deep_Learning) is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US). Permissions beyond the scope of this license are described in the [Terms of Use](http://www.scholarpedia.org/article/Scholarpedia:Terms_of_use)

*   [Privacy policy](http://www.scholarpedia.org/article/Scholarpedia:Privacy_policy "Scholarpedia:Privacy policy")
*   [About Scholarpedia](http://www.scholarpedia.org/article/Scholarpedia:About "Scholarpedia:About")
*   [Disclaimers](http://www.scholarpedia.org/article/Scholarpedia:General_disclaimer "Scholarpedia:General disclaimer")
