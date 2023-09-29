This folder contains the files for RQ1. It has the source code and the taxonomy generation files. Below is a descriotion of all the files:

1. get_repositories.py extracts repositories with keywords: 'deep neural network' and 'deep learning' and star count >50. With that we get 6655 repositories. Then the downloaded csv files have these repositories where release > 1.

3. These files are in the folder github_repositories.

4. We combine these files to get 696 repositories. These are in 'Repositories - Owner and repo'.

5. We then mine issues with keywords: feature request and enhancement using get_issues.py. We get issues.csv containing 3997 issues.

6. We only consider issues with comments>0 to only get issues that are relevant and have been interacted with. We use get_issues_comments.ipynb to do this. We get filtered_issues.csv with 1860 issues.

7. We manually label to get model related changes by answering the question:Does the issue deal with requirement change in pre-trained model? We get 165 issues in 42 repositories.
   
9. Repositories.xlsx contains a comprehensive sheets of all the steps mentioned above as well as the final filetred repositories which are in the sheet named "final".
