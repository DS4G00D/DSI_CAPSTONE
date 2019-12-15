
# Project Proposal: Match career advice questions with professionals in the field


_Analytics Prediction Competition:_ Match career advice questions with professionals in the field



## 1. Introduction and Motivation


[careervillage.org](https://careervillage.org)'s mission is to democratise access to the career advice and guidance underserved youth need to create professional goals and understand their personal paths to those goals. We hope to use preprocessing combined with machine learning methods to improve career advice and enhance the communication of professionals with millions of online learners covering over 8,000 career topics. 


## 2. Problem Statment


The U.S. has almost 500 students for every guidance counsellor. Underserved youth lack the network to find their career role models, making CareerVillage.org the only option for millions of young people in America and around the globe with nowhere else to turn.
To date, 25,000 volunteers have created profiles and opted in to receive emails when a career question is a good fit for them. This is where your skills come in. To help students get the advice they need, the team at CareerVillage.org needs to be able to send the right questions to the right volunteers. The notifications sent to volunteers seem to have the greatest impact on how many questions are answered.

In this project we would like to show some approaches for a new recommendation engine at www.careervillage.org.

##### Our objective:
- develop a method to recommend relevant questions to the professionals who are most likely to answer them.

The Recommendation Engine itself should be answer the following questions
- When a student asks a question, are there already any similar questions that might help them?
- Which professionals are most expected to answer the new question
- Which questions should be forwarded to a professional to answer?
- Which hashtags might interest a user because of his previous activities?


## Project
### Methodology
We will begin by establishing simple baselines for answer extraction using machine comprehension of text:
- sliding window approach as well as distance based extension [
- logistic regression model using lexicalized features or dependency tree path features 

We will then explore scalable implementations of alternative NLP and deep learning techniques to enhance the model performance . 
We also aim to enhance the approach using open-domain question answering techniques by augmenting large-scale knowledge sources to extract relevant answers to the posed questions.


### Overview

As described in the Kaggle completion page: "_In this competition you'll notice there isn't a leaderboard, and you are not required to develop a predictive model. This isn't a traditional supervised Kaggle machine learning competition._

_CareerVillage.org is a nonprofit that crowdsources career advice for underserved youth. Founded in 2011 in four classrooms in New York City, the platform has now served career advice from 25,000 volunteer professionals to over 3.5M online learners. The platform uses a Q&A style similar to StackOverflow or Quora to provide students with answers to any question about any career._

_In this Data Science for Good challenge, CareerVillage.org, in partnership with Google.org, is inviting you to help recommend questions to appropriate volunteers. To support this challenge, CareerVillage.org has supplied five years of data._"

### Algorithms

- NLP
- Recommendation Engine
- NN
- Time Series 
- Supervised ML
- Unsupervised ML



### Data

Along with google.org, CarrerVillage.org has released years worth of data from their website including emails sent out to professionals, the questions, answers and comments exchanged, the professions, locations and school details of the student and professional members.

Data is for years 2012 though 2019 Feb. It has been provided in 13 csvs which are listed below with a short description of the csvs.


- answers.csv: Answers are what this is all about! Answers get posted in response to questions. Answers can only be posted by users who are registered as Professionals. However, if someone has changed their registration type after joining, they may show up as the author of an Answer even if they are no longer a Professional.
- comments.csv: Comments can be made on Answers or Questions. We refer to whichever the comment is posted to as the "parent" of that comment. Comments can be posted by any type of user. Our favourite comments tend to have "Thank you" in them :) 
- emails.csv: Each email corresponds to one specific email to one specific recipient. The frequency_level refers to the type of email template which includes immediate emails sent right after a question is asked, daily digests, and weekly digests. 
- group_memberships.csv: Any type of user can join any group. There are only a handful of groups so far.
- groups.csv: Each group has a "type". For privacy reasons we have to leave the group names off.
- matches.csv: Each row tells you which questions were included in emails. If an email contains only one question, that email's ID will show up here only once. If an email contains 10 questions, that email's ID would show up here 10 times. 
- professionals.csv: We call our volunteers "Professionals", but we might as well call them Superheroes. They're the grown ups who volunteer their time to answer questions on the site. 
- questions.csv: Questions get posted by students. Sometimes they're very advanced. Sometimes they're just getting started. It's all fair game, as long as it's relevant to the student's future professional success.
- school_memberships.csv: Just like group_memberships, but for schools instead.
- students.csv: Students are the most important people on CareerVillage.org. They tend to range in age from about 14 to 24. They're all over the world, and they're the reason we exist!
- tag_questions.csv: Every question can be hash-tagged. We track the hashtag-to-question pairings, and put them into this file.
- tag_users.csv: Users of any type can follow a hashtag. This shows you which hashtags each user follows.
- tags.csv: Each tag gets a name. 
question_scores.csv: "Hearts" scores for each question.
- answer_scores.csv: "Hearts" scores for each answer.


### Workflow|Timeline


- **Understanding data**
- **Preparation**
- **Feature Extraction**
- **EDA**
     * Time Series
     * Missing Values (Professionals)
     * Missing Values (Students)
     * Tags Matching
     * Question Response Time
     * Email Response Time
- Word Count

- **Models**

  - [will be update you soon]
  - Recommendation Engine
  - Get Similar Questions
  - Recommend User Tags

- **Evaluation**
  - Get Similar Questions
  - Recommend new Questions to Professionals
  - Recommend User Tags
- **Further Advice**
  - [will be update you soon]

## Report

[will be update you soon]


## Team

- Abdulla : hawkash
- Wejdan : wejdanalzhrani
- Amal: phymal

[Git page](https://git.generalassemb.ly/DS4Good)
## Sources for background learning:
[will be update you soon]
