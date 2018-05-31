#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def connect_to_DB(question):
    """" Fuction to connect to the news data base """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(question)
    answer = c.fetchall()
    db.close()
    return answer


def print_answers(answer):
    """ Function to print the answers in the terminal """
    for i in answer:
        print(str(i[0]) + ' with the result of ' + str(i[1]))
    print '\n'


def question_1():
    """ Return 3 most popular articles """
    question1 = """
                select title, count(*) as views from articles
                join log on log.path = concat('/article/', articles.slug)
                group by articles.title order by views desc limit 3;
                """

    answer1 = connect_to_DB(question1)
    print("Question 1. What are the most popular three articles of all time?")
    print '\n'
    print_answers(answer1)


def question_2():
    """ Return most popular article authors of all time """
    question2 = """
                select name, views from authors, top_view_art
                where authors.id = top_view_art.author;
                """
    answer2 = connect_to_DB(question2)
    print("Question 2. Who are the most popular article authors of all time?")
    print '\n'
    print_answers(answer2)


def question_3():
    """ Return inf on which days did more than 1% of requests lead to errors"""
    question3 = """
                select total_request.date,
                round(100 * cast(total_bad_request.bad_req as decimal) /
                cast(total_request.total_req as decimal), 2)
                as daily_error from total_request join total_bad_request
                on total_request.date = total_bad_request.date
                order by daily_error desc limit 1;
                """
    answer3 = connect_to_DB(question3)
    print("Question 3."
          " On which days did more than 1% of requests lead to errors?")
    print '\n'
    print_answers(answer3)

if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
