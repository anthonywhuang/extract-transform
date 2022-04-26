# extract-transform

i have the title, company, estimated salary, and location of the job titles. what I'm trying to do is get all the requirements and qualifications of each of the jobs, clean the data with excel/sql or something, then put them into a data visualization tool to see what the most common requested skills and qualifications are for the job. it's for mechanical engineering for now because that's what my mentor wants to do so i can also slide that into job interviews that like 'oh ya i also volunteer look at me im a good person please hire me so i can gtfo of accounting'

sometimes the responsibilities and qualifications are nested in "<ul>" lines and then show up as "<li>" and sometimes they're in "<p>" and then "<b>" lines. they also don't have tags and just the letters so i'm having trouble pulling them. qualifications and responsibilities also aren't on every posting. sometimes it's one sometimes it's the other.
  
would i need to create some new code to pull specifically the div class of something like 'jobsearch-JobComponent' first? cause then i'm also having trouble pulling them because the next couple of characters are different which makes sense but i don't know how to put a wild card in the find statement
