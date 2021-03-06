#Reading Assignment # 10 
 
### Summary of *Bug Prediction Based on Fine-Grained Module Histories* [1]

#### Download Link 
http://dl.acm.org/citation.cfm?id=2337247

#### Keywords	 
* ii1: Bug Prediction : This term refers to the ability to predict a future bug by building a model using the historical metrics, which are mined from version histories of software modules.
* ii2: Fine-grained Prediction: This term refers to the use of method-level details while using historical metrics, mined from version histories of software modules, to build a model for predicting bugs.
* ii3: Fine-grained Histories: It refers to the use of fine-grained metrics, by creating metadata or a structure which will store the history or change information at very fine grained level , for example, capturing details of a method level change instead of package level or file level change alone.
* ii4: Historical Metrics:They are metrics coming from various categories such as code-related metrics, process-related metrics, organizational metrics and geographical metrics for capturing version history in different categories.


#### Key Points
* iii1: Related Work: The paper says that bug prediction has been widely studied and recent findings show the usefulness of collecting historical metrics from software repositories for bug prediction models. Prediction models have been build using bug-fix information. Bug prediction has been done using file-level and package-level historical metrics and it has been observed that results from file-level metrics are more interesting. Fine-grained prediction has been a challenge because obtaining method histories from existing version control systems is a difficult problem.
* iii2: Motivational Statements: Although a lot of previous work has been done on bug prediction using file-level and package-level historical metrics, there is a need to do bug prediction at a fine-grained level such as method level. In ESEC/FSE 2011 conference, fine-grained prediction was selected as one of the future directions. Studies of fine-grained prediction are necessary because desirable results may be obtained when compared to coarse-grained prediction.
* iii3: Study Instruments: In order to collect detailed histories, the authors have proposed a fine grained version control system - Historage. Historage was constructed on top of Git and can control method histories of Java. The authors then empirically evaluate the prediction models with eight open source projects written in Java.
* iii4: New Results: The authors have come up with a new framework to capture fine-grained method-level historical metrics. Using eight open source projects, package level , file-level and method-level prediction models were compared based on effort-based evaluation. They found that method-level prediction is more effective than package-level and file-level prediction when considering efforts. They also observed that past bug information on methods does not correlate with post bugs in methods, and organizational metrics may not contribute to method-level prediction. Code-related metrics have positive correlations and interval-related metrics have negative correlations.

#### Suggestions for Improvement 
* iv1: The authors have created Historage for capturing metadata with respect to fine-grained histronics. This could be annoying for the developers if they have to classify or give fine-grained details at various levels each time they make the code change. They could come up with a methodology to automatically dig out this information from available version control systems such as GitHub.
* iv2: The version control tool is capable only for open-source software written in Java. If they had written a methodology for automatically picking out methods, they could have had the ability to adapt to any kind of language or software repository.
* iv3: They have used effort-based evaluation which may not reflect actual efforts. They could use other metrics and come up with a comparison between them.
* iv4: Although random forest modelling is quite robust, they could have used other models and compared the results. 

#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. The "Ecological Inference in Empirical Software Engineering" paper makes use of the conclusion from "Benchmarking Classification Models.." paper - that simple statistic measures like TPR, FPR do not work well in a software defect prediction context as it is possible for two groups to use the same model on same data set and yet come with different results just because they had different threshold values. So the authors use ROC and statistical testing methods in their experiment to model defects. The authors of this paper use this information and argue that method-level fine-grained historical metrics give interesting bug-prediction models which yield better results as compared to file-level or package-level historical metics. 

####Reference
[1] Hideaki Hata, Osamu Mizuno and Tohru Kikuno. Bug Prediction Based on Fine-Grained Module Histories. In ICSE '12 Proceedings of the 34th International Conference on Software Engineering Pages 200-210.
[2] D. Posnett, V. Filkov, and P. Devanbu. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM Inter- national Conference on Automated Software Engineering, pages 362–371. IEEE Computer Society, 2011. 

