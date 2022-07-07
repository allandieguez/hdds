# Hypothesis Backlog

## Context

Every hypothesis should be listed in this document. The document is alive, so every time a new hypothesis is created, or an existing hypothesis is validated or refuted, or even discarded, the document changes. The same goes with priority changes: the document will **always** sort the **backlog** in descending order of estimated aggregated value to solve the problem. When enough hypothesis are validated, it is expected that the project is finished and it's core value has been delivered to the full extent.

## Sections

This document is composed by 3 sections:
1. [Evaluated](#Evaluated): Validated/refuted hypothesis that are already finished, so no more experiments have to be created to evaluate them. The list is already sorted in descending order of value due to the nature of the **backlog**.
2. [Backlog](#Backlog): Hypothesis backlog split into thre sections: [Ongoing](#Ongoing), containing the refined hypothesis that is currently being evaluated, [Ready](#Ready), containing the refined hypothesis that should be evaluated by experiments and sorted by estimated value for the solution, and [Discovery](#Discovery), containing hypothesis that should be first refined before being sorted into the backlog.
3. [Discarded](#Discarded): Hypothesis that were discarded before evaluation, because an external event (e.g. business insight) shows that there is no value added to the project, whatever the evaluation outcome is.

## Template

All hypothesis should follow the template described below. An hypothesis should have at least the **Description** field filled to be in the **Backlog** listed for **Discovery**. If the hypothesis is **ready for evaluation**, it should at least also have the **Estimated Value** field filled out. A **discarded hypothesis** should have filled the **Discarded Reason**. A **validated or refuted hypothesis** should have filled all the sub-fields **Evidence Support**, **Experiments** and **Conclusion** from the field **Evaluation**.

### < (H#) Hypothesis Name >

#### Description
Mandatory field. No hypothesis should be created without a description.
> Succint description of the hypothesis, describing clearly an issue of the problem at hand.

#### Estimated Value
Optional field. Only an hypothesis that is Ready (past Discovery) may have this filled.   
> Description of the estimated value in the context of the problem. If possible, this should contain a quantitative estimate (e.g. "if valid, raises conversion by 10%"), but a qualitative one (e.g. ""if refuted, it is impossible to model") is also allowed. This field will be used for sorting the hypothesis in the Backlog.

#### Evaluation 
Optional fields. To be filled while the hypothesis is being evaluated.

##### Conclusion
> Final conclusion (validated or refuted) and remarks about the hypothesis.
##### Evidence Support
> Evidences that support the hypothesis, preferrably statistically based. May contain qualitative remarks like an example (data sample) or domain knowledge based business insight.
##### Experiments
> List of experiments created in the attempt of evaluating the hypothesis. The experiments should be sorted from newest to oldest, and the top experiment should be the one that validated or refuted the hypothesis.

#### Discarded Reason
Optional field. Should be filled when the hypothesis is discarded.
    
> Succint text describing the reasons the hypothesis was discarded. Any previously filled field should remain filled for backtracking purposes.


------

# Evaluated

Evaluated hypothesis, grouped by **date of validation (or refute)**. 

## < Date of Evaluation >
...

------

# Backlog

Hypothesis backlog; work in progress is located here.

## Ongoing

Current hypothesis being evaluated.
...


## Ready

All hypothesis that are ready to be evaluated; sorted descendent by **business value**.
...


## Discovery

All incomplete hypothesis; their final **estimated business value** isn't written yet.

...


------

# Discarded

Discraded hypothesis, grouped by **date of discard**. 


## < Date of Discard >
...


