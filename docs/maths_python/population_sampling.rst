=======================
Population_sampling
=======================

| VCMNA307: Apply set structures to solve real-world problems

* Exploring variation in proportion and means of random samples, drawn from a population

----

Sample Means: Increasing samples
----------------------------------------

| The code below generates a population of 10000 individuals with a mean of 50 and a standard deviation of 10. 
| It then draws random samples of a given size from the population and calculates the sample means. 
| Finally, it plots histograms of the sample means to visualize their variation.

.. image:: images/sample_means_inc_samples.png
    :width: 800
    :align: center

| Increasing the number of samples drawn from a population generally leads to more accurate estimates of the population mean. 
| This is because as the number of samples increases, the distribution of sample means tends to become more tightly clustered around the true population mean. 
| This phenomenon is known as the Central Limit Theorem.


| In other words, as the number of samples increase, the sample means are more likely to be close to the population mean, and the variation among the sample means decreases. 
| This can be seen in the histograms above: as the number of samples increases, the histograms become taller and narrower, indicating that the sample means are becoming more concentrated around the population mean.


----

Sample Means: Increasing sample size
----------------------------------------

| The code below generates a population of 10000 individuals with a mean of 50 and a standard deviation of 10. 
| It then draws random samples of a given size from the population and calculates the sample means. 
| Finally, it plots histograms of the sample means to visualize their variation.

.. image:: images/sample_means_inc_size.png
    :width: 800
    :align: center

| Increasing the size of the samples drawn from a population generally leads to more accurate estimates of the population mean. 
| This is because as the sample size increases, the sample means tend to become more tightly clustered around the true population mean. 
| This phenomenon is also a consequence of the Central Limit Theorem.

| As the sample size increases, the sample means are more likely to be close to the population mean, and the variation among the sample means decreases. 
| This can be seen in histograms of the sample means: as the sample size increases, the histograms become taller and narrower, indicating that the sample means are becoming more concentrated around the population mean.


| It's important to note that increasing the sample size has diminishing returns. 
| As the sample size gets larger and larger, the improvement in accuracy becomes smaller and smaller. 
| At some point, increasing the sample size further may not be worth the additional cost and effort.



