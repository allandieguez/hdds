# Experiment Report:

## Source Hypothesis: 
[(H#) Hypothesis Name, as written in the Hypothesis Backlog](../readme.md#slugified-hypothesis-name)

## Work Planning
Support for creating the actual `analysis` workflow in the `experiment`, describing in depth what is expected do be done to validate or refute the source `hypothesis`.

### Milestones:
Mandatory field; macro steps to be completed before ending the `experiment`.
#### Milestone 1
> Description in one single block of text is preferred.
#### Milestone 2
> Ok to split into subtopics when too complex for a single block:
>  - Importante step to milestone
>  - Another step to milestone
>  ...
#### Milestone 3
> Examples of Milestones:
>  - Define Train/Dev/Test/Validation splits for the dataset
>  - Define best technical/business metrics for the model evaluation
#### ...
### Expected Outcomes:
Optional field; what is expected from the `experiment` besides the source `hypothesis` validation.
#### Expected Outcome 1:
> Description of what is expected after completing the `experiment`. 
#### Expected Outcome 2:
> If more outcomes are expected, each should have their own subsection.
#### Expected Outcome 3:
> Examples of expected outcomes:
> - A model pipeline for predicting Y from features extracted from dataset X;
> - Definition of groups of interest (clusters, cohorts, etc) in the dataset.
#### ...

## Takeaways:
Must answer questions raised by the Milestones, but not limited to them.
 
### Takeaway 1
Analysis Task: [yyyymmdd-xxx-analysis-task-one.ipynb](./yyyymmdd-xxx-analysis-task-one.ipynb)
> Description of the takeaway in which the work contained on a single `analysis`. The description should point out enough evidence to support the discoveries. When connected to a `milestone`, the text should point out how the evience changed the prior knowledge from when the `milestone` was first sketched.
### Takeaway 2 
Analysis Tasks:  
- [yyyymmdd-xxx-analysis-task-one.ipynb](./yyyymmdd-xxx-analysis-task-one.ipynb)
- [yyyymmdd-xxx-analysis-task-two.ipynb](./yyyymmdd-xxx-analysis-task-two.ipynb)
- [yyyymmdd-xxx-analysis-task-three.ipynb](./yyyymmdd-xxx-analysis-task-three.ipynb)
> A takeaway may reference more than one analysis notebook, specially when there are more complex EDA and modeling tasks involved. The `analysis` tasks should be described as a bullet-point list, as shown above. The text should remain as summarized as possible, pointing out the most relevant information. If a reader wishes to read further about a specific topic, the information should be easily accessible on the `analysis` notebook.
### ...
