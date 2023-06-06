#------------------------ WESTMINSTER INTERNATIONAL UNIVERSITY IN TASHKENT -----------------------#
#-------------------------- INTRODUCTION TO STATISTICS AND DATA SCIENCE --------------------------#
#------------------------------- PORTFOLIO OF INDIVIDUAL EXERCISES -------------------------------#

# Submission Instructions: You must rename this file with your own student ID and upload it in compressed (zipped) format.
# Double check that your zipped file is not corrupted and can be unzipped by the grader.
# Submit the zipped .R file here: https://intranet.wiut.uz/Coursework/UploadsDT?courseworkID=2958 
# You must also report your detailed explanations and answer codes in MS Word format and upload to the Intranet.
# The link to upload your .doc file: https://intranet.wiut.uz/Coursework/UploadsDT?courseworkID=2959
# If the links do not work, then you can find the submission pages under Coursework section of the module.
# Late submissions are not acceptable. Please do not wait until the last minute to submit. 
# Please watch the online recording available on Intranet under Week 5 if you need any clarifications about Portfolio.
# Do not contact your lecturers to seek help or any hints during take-home exam period. 

ID <-  14465  # TO DO: <--- Insert your ID in place of NULL. Do not include the zeros (0's) in the beginning of your ID.
# For example, if your ID is 00010200, then you need to enter your ID as 10200.
# Failure to provide the ID results in 0 mark. 
  
# Some exercises require the student to insert his/her last 5 digits of ID in place of abcde values. 
# For example, a student with an ID of 12020 has the following values: a = 1, b = 2, c = 0, d = 2, e = 0.
# Or a student with an ID of 9540 has the following values: a = 0, b = 9, c = 5, d = 4, e = 0.
# You must only provide the R code which will store the correct answer in the given variable names. 
# DO NOT use rounding functions for your answers unless instructed to do so in the question.
# You can add additional rows above the answer line if you have more than one line of code as a solution.
# But you must store the final code into the variable names provided in each task.
# You can use any package of R to solve these tasks, but you must include the installation and loading codes in the section provided below.  
# DO NOT CHANGE THE VARIABLE NAMES (e.g. keep answer1_a, answer1_b, answer2_a, etc. as they are. This is very important).
# You will be given full mark only if your code provides the correct answer. 
# Partial credits might be given to only data visualization tasks. 
# Therefore, be very careful/mindful about your answers and what they produce.

#--------------------------------------PACKAGE INSTALLATION AND LOADING PART-----------------------# 
# Skip this part if you are only using the Base package of R.
# If you use any packages other than the base package, 
# please add the installation and loading codes here, like below (without #):
# install.packages("package_name")
# library(package_name)




a <- 1
b <- 4
c <- 4
d <- 6
e <- 5

#-------------------------------------END OF PACKAGE INSTALLATIONS AND LOADING---------------------# 

#------ TASK 1 -------# [1+1+1+1+1+1+1+1 = 8 marks]
# a. Create a sequence of integer numbers from (a+b) to (c+d+e+300). Here, a,b,c,d,e are your student ID digits.


a <- 1
b <- 4
c <- 4
d <- 6
e <- 5

answer1_a <- seq(a + b, c + d + e + 300, by = 1)
# b. Add the values of only even numbers of your vector from part 1_a (here, 1_a is not related your ID digit).
answer1_b <- sum(answer1_a[answer1_a %% 2 == 0])

#c. Compute the sample standard deviation of only odd numbers from your vector in part 1_a.
answer1_c <- sd(answer1_a[answer1_a %% 2 != 0])

#d. Find the range of your vector from part 1_a.
answer1_d <- range(answer1_a)

#e. Sort the values of your vector from part 1_a in descending order and store as a new vector.
answer1_e <- sort(answer1_a, decreasing = TRUE)

#f. Create a vector of numeric values from your ID to (ID+2000) with an increment of 0.5.
# ID is your student ID. Compute the median of this vector and store below.
answer1_f <- median(ID:(ID+2000), by = 0.5)

#g. Find the 25th percentile (Q1) of your vector in answer1_f. 
# Use a built-in R function to find the quartile. Do not use the formula given in Semester 1 because the formulas 
# in finding quartiles might be different than R function.
answer1_g <- quantile(answer1_f, 0.25)

#h Find the value of Inter-quartile range (IQR) for the vector in answer1_f. Use built-in R functions.
answer1_h <- IQR(answer1_f)


#------ TASK 2 -------# [4+4=8 marks]
# Uzbekistan Airways find that on average (a+2) passengers on their Boeing 787 
# Dreamliner flights do not show up to their flights. For that reason they sell 
# (336 + a + 1) tickets on a plane that has a capacity of 336 seats. Assuming the 
# variance of those who do not show up is (a+2), find the probability that

#a. everyone will show up to the flight;
mean <- a + 2
variance <- a + 2

# Calculating the probability using the normal distribution
answer2_a <- pnorm(0, mean = mean, sd = sqrt(variance))


#b. at least (b+1) will not show up to their flight.

answer2_b <- sum(dbinom(b:n, size = n, prob = p))

#------ TASK 3 -------# [3+3+3+3=12 marks]
# A manufacturing company produces batch of (25+c) goods, of which (d+3) are expected to be defective.
# A 25-year old quality assurance employee who has 4-year experience inspects a sample of (e+10) goods. 
# Assume that being defective for any produced good is an independent event. 

#a. Compute the probability that the sample contains less than (b+1) defective items.
answer3_a <- sum(dbinom(0:(b), size = (e+10), prob = (d+3)/(25+c)))

#b. Compute the probability that the sample contains exactly (b+1) defective items.  
answer3_b <- dbinom(b, size = (e+10), prob = (d+3)/(25+c))

#c. Compute the probability that the sample contains more than (a+1) but at most (a+5) defective items.
answer3_c <- sum(dbinom((a+1):(a+5), size = (e+10), prob = (d+3)/(25+c)))

#d. What is the number of defective items for (80+c)th percentile?
# i.e. (80+c)% of samples with size of (e+10) have at most this number of defects.
answer3_d <- qbinom(0.8+c/100, size = (e+10), prob = (d+3)/(25+c))

#------ TASK 4 -------# [3+3+3+3=12 marks]
# Suppose x is a waiting times for school bus that is uniformly distributed
# with a pdf function of p(x) = 0.0625 and minimum waiting time of (e+1) minutes.
# Calculate the variance of waiting times.
answer4_a <- 0.0625 * (e+1)^2

#Let k be the maximum of a, b, c, d, e. Calculate P(x > k).  
answer4_b <- 1 - 0.0625 * (e+1)

#c. What is the waiting time in minutes for a student who is at (70+e)th percentile?
answer4_c <- qunif(0.7+e/100, min = (e+1), max = 1)

#d. If you randomly choose (40+b) students, what is the probability that their average
# waiting time will be more than (e+7) minutes?
answer4_d <- 1 - pnorm((e+7), mean = (e+1), sd = sqrt(answer4_a))^(40+b)

#------ TASK 5 -------# [3+3+3+3+3=15 marks]
# A radar system at the intersection of "Shahrisabz" and "Amir Temur" streets
# measures the speeds of cars on the road. According to the data of past 365 days,
# the average speed is (50+e) km/hr and a standard deviation of (a+b+1) km/hr. The 
# distribution of car speeds follows a Gaussian distribution. If you select (30+c) cars
# at random, 
#How many of them are expected to be travelling at more than 80 km/hr? Round your answer to integer value.
answer5_a <- sum(dnorm(80, mean = (50+e), sd = (a+b+1)) * (30+c))

#b. How many of them are expected to be travelling at less than 50 km/hr? Round your answer to integer value.
answer5_b <- sum(dnorm(50, mean = (50+e), sd = (a+b+1)) * (30+c))

# Provide the lower bound of (90 + e)% confidence interval for the average speed of the cars at this intersection. 
answer5_c <- (50+e) - qnorm(0.95) * (a+b+1) / sqrt(30+c)

#d. Provide the upper bound of (90 + e)% confidence interval for the average speed of the cars at this intersection.
answer5_d <- (50+e) + qnorm(0.95) * (a+b+1) / sqrt(30+c)
#e. Do you have enough evidence to claim that average speed for all cars at this intersection is higher than (52+e)
# at (c+1)% significance level? There is no need to show your solutions here.
# Just type "yes" or "no" in place of NULL. You can explain your solution in MS Word doc.
answer5_e <- "yes"

#------ TASK 6 -------# [2+2+2+2=8 marks]
# Run the following two lines of codes:
df1 <- data.frame(ID = 101:152, name = c(LETTERS, letters))
df2 <- data.frame(id = c(102:120, 130:146), age = c(rep(20, 5), rep(25, 10), rep(23, 9), rep(30, 8), rep(18, 4)))

#a. Complete an inner join of these two data frames based on ID (id) columns and store as answer6_a.
answer6_a <- merge(df1, df2, by.x = "ID", by.y = "id", all.x = TRUE)

#b. Delete (a+1) number of rows from the top and (b+1) number of rows from the bottom 
# of data frame of answer6_a. Store the new data frame as answer6_b
answer6_b <- answer6_a[-c(1:(a+1), (nrow(answer6_a)-(b+1)):nrow(answer6_a)), ]
#c. Compute the average age from answer6_b.
answer6_c <- mean(answer6_b$age)
#d. Compute the sample variance of age from answer6_b.
answer6_d <- var(answer6_b$age)

#------ TASK 7 -------# [3+3+3+3=12 marks]
# Read the following college data into your RStudio:
college <- read.csv(url("https://s3.amazonaws.com/itao-30230/college.csv"))

# Remove the following rows from the dataset all at once: (a+1), (a+11), (b+21), (b+31), (c+41), (c+51), (d+101), (d+111), (e+1001)
# Then, you can name this dataset with any name you want.
# This is your unique college data and you will be working with this dataset for tasks in 7 and 10.
# Find the average tuition for public universities with more than $(12000 + 300*d + 400*e) tuition rate in state of Washington.
answer7_a <- mean(college$tuition[college$public == 1 & college$tuition > (12000 + 300*d + 400*e) & college$state == "WA"], na.rm = TRUE)

#b. How many universities from the South region have an acceptance rate higher
# than 45% and SAT average above 1100?
answer7_b <- sum(college$acceptance_rate[college$region == "South" & college$acceptance_rate > 0.45 & college$sat_avg > 1100], na.rm = TRUE)

#c. How many university names in the data contain the string "California" (Consider all letter cases, such as "california", "CALIFORNIA", etc)?
answer7_c <- sum(grepl("California", college$name))

#d. Group the universities by state and compute the average of (faculty_salary_avg) by each state.
# Which state has the minimum value? Your code should provide the two-letter abbreviation from state column.
answer7_d <- college$state[which.min(college$faculty_salary_avg)]

#------- TASK 8 -------# [6 marks]
# A data point is considered to be an outlier if it falls outside the following range: (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
# Here, Q1 - first quartile, Q3 - third quartile and IQR is inter-quartile range.
# Your task is to write a function that takes a vector as an argument, checks for outliers and prints the following statement:
# "The function created by student ____ (insert your ID into blanks) has found the following outliers: ______ (insert a vector of outliers)"
# If there are no outliers, then it should print as follows: "The function created by student ______ (insert your ID into blanks) has found no outliers".
# For example, if I pass the vector x into your function:
# x = c(1, 25, 35, 40, 26, 28, 29, 31, 1001)
# answer8(x)
# The output will look like the following:
# "The function created by student 12345 has found the following outliers: 1, 1001"
# 12345 is the student ID.
answer8 <- function(vector) {
    q1 <- quantile(vector, 0.25)
    q3 <- quantile(vector, 0.75)
    iqr <- q3 - q1
    outliers <- vector[vector < q1 - 1.5*iqr | vector > q3 + 1.5*iqr]
    if (length(outliers) == 0) {
        print(paste("The function created by student", ID, "has found no outliers"))
    } else {
        print(paste("The function created by student", ID, "has found the following outliers:", paste(outliers, collapse = ", ")))
    }
}



#------- TASK 9 -------# [10 marks]
# Create a function that takes a data frame as an argument. 
# This data frame contains only x and y columns.
# Your function needs to provide a scatter plot of x (horizontal axis) and y (vertical axis).
# The point symbols of the graph must be triangles instead of circles and their colors are blue.
# If there are any data points which are greater or smaller by more than 1.5 standard deviations from the mean,
# then their colors must be red. (See the image named "task9.png" provided in the Portfolio zip folder)
# Example. Suppose the following data frame is passed into your function:
# s1 <-  data.frame(x = c(300, 130, 150, 170, 100, 5, 160, 118), y = c(250, 145, 150, 124, 130, 1, 150, 154))
# Then only two pairs (300, 250) and (5, 1) would be colored red, because they fall outside 1.5 standard deviations from the mean.
# Please note that both x and y values must be outside the 1.5 standard deviations from their respective means to be colored red.
# If we run answer9(s1) on the console, we should get the output as shown in task9.png.
# Your function should work for any dataframe with x and y variable names.
answer9 <- function(df) {
    x_mean <- mean(df$x)
    y_mean <- mean(df$y)
    x_sd <- sd(df$x)
    y_sd <- sd(df$y)
    x_outliers <- df$x[df$x < x_mean - 1.5*x_sd | df$x > x_mean + 1.5*x_sd]
    y_outliers <- df$y[df$y < y_mean - 1.5*y_sd | df$y > y_mean + 1.5*y_sd]
    plot(df$x, df$y, pch = 17, col = "blue", xlab = "x", ylab = "y")
    points(x_outliers, y_outliers, pch = 17, col = "red")    

}



#------ TASK 10 -------# [6 marks]
# Refer to your college data from task 7.
# Create a set of boxplots of tuition rates based on 4 regions.
# Make sure to have 4 different colors for your boxplots using only hex color codes.
# Your student ID should be shown in the main title of the plot.
answer10 <- boxplot(tuition ~ region, data = college, col = c("#FF0000", "#00FF00", "#0000FF", "#FFFF00"), main = paste("Student ID:", ID))

#------- TASK 11 -------# [3 marks]
# Copy/Paste the following statement below in the quotation mark: 
# "I hereby confirm that this work is solely my own work and my ID is ______. I am fully aware of the consequences of student misconduct."  TO DO: replace the blanks with your student ID.
# how to insert id vairable into string
answer11 <- paste("I hereby confirm that this work is solely my own work and my id is", ID, ". I am fully aware of the consequences of student misconduct.")
print(answer11)
#-------------------------------------------------------------- END OF TASKS --------------------------------------------------------------------------------#
#--------------------------------------------------------------- GOOD LUCK!----------------------------------------------------------------------------------#






