-- Pig script to search inputs file for hackathon, Dec, Chicago, Java
-- It counts the number of lines each of these term occur in

-- Loads the input file
LINES = LOAD 'class5/input.txt' AS (line:chararray);

-- Checks each search term for each line. Writes 1 if the term is existing, 0 otherwise. 
OCCURRENCES = FOREACH LINES GENERATE 'Dec' AS term:chararray, (UPPER(line) matches '.*DEC.*' ? 1 : 0) AS existing;
TEMP = FOREACH LINES GENERATE 'hackathon' AS term:chararray, (UPPER(line) matches '.*HACKATHON.*' ? 1 : 0) AS existing;
OCCURRENCES = UNION OCCURRENCES, TEMP;
TEMP = FOREACH LINES GENERATE 'Chicago' AS term:chararray, (UPPER(line) matches '.*CHICAGO.*' ? 1 : 0) AS existing;
OCCURRENCES = UNION OCCURRENCES, TEMP;
TEMP = FOREACH LINES GENERATE 'Java' AS term:chararray, (UPPER(line) matches '.*JAVA.*' ? 1 : 0) AS existing;
OCCURRENCES = UNION OCCURRENCES, TEMP;

-- Group the (term, 0/1) tuples by term, to sum all the 1s for a particular search term
OCCURRENCES_GROUP = GROUP OCCURRENCES BY term;
SOLUTION = FOREACH OCCURRENCES_GROUP GENERATE group AS term:chararray, SUM(OCCURRENCES.existing) AS lines:int;

-- Sorts the results by ascending order
SOLUTION = ORDER SOLUTION BY term ASC;

-- Displays and stores the results
DUMP SOLUTION;
STORE SOLUTION INTO '/user/qm301/class5/output';